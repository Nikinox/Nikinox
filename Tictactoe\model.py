import random
from collections import deque, namedtuple
from typing import List
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

Transition = namedtuple("Transition", ("state", "action", "reward", "next_state", "done"))


class ReplayBuffer:
    def __init__(self, capacity: int = 10000):
        self.buffer = deque(maxlen=capacity)

    def push(self, *args):
        self.buffer.append(Transition(*args))

    def sample(self, batch_size: int):
        samples = random.sample(self.buffer, batch_size)
        batch = Transition(*zip(*samples))
        return batch

    def __len__(self):
        return len(self.buffer)


class QNetwork(nn.Module):
    def __init__(self, input_dim=9, hidden=128, output_dim=9):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden),
            nn.ReLU(),
            nn.Linear(hidden, hidden),
            nn.ReLU(),
            nn.Linear(hidden, output_dim),
        )

    def forward(self, x):
        return self.net(x)


class DQNAgent:
    def __init__(self, device=None, lr=1e-3, gamma=0.99, tau=0.005):
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.policy_net = QNetwork().to(self.device)
        self.target_net = QNetwork().to(self.device)
        self.target_net.load_state_dict(self.policy_net.state_dict())
        self.optimizer = optim.Adam(self.policy_net.parameters(), lr=lr)
        self.gamma = gamma
        self.tau = tau
        self.replay = ReplayBuffer()
        self.steps = 0

    def select_action(self, state: np.ndarray, legal_actions: List[int], epsilon: float):
        if random.random() < epsilon:
            return random.choice(legal_actions)
        self.policy_net.eval()
        with torch.no_grad():
            s = torch.tensor(state, dtype=torch.float32, device=self.device).unsqueeze(0)
            q = self.policy_net(s).cpu().numpy().ravel()
        q_invalid = -1e9 * np.ones_like(q)
        for a in legal_actions:
            q_invalid[a] = q[a]
        return int(q_invalid.argmax())

    def store(self, *args):
        self.replay.push(*args)

    def update(self, batch_size=64):
        if len(self.replay) < batch_size:
            return 0.0
        batch = self.replay.sample(batch_size)
        state = torch.tensor(np.array(batch.state), dtype=torch.float32, device=self.device)
        action = torch.tensor(batch.action, dtype=torch.long, device=self.device).unsqueeze(1)
        reward = torch.tensor(batch.reward, dtype=torch.float32, device=self.device).unsqueeze(1)
        next_state = torch.tensor(np.array(batch.next_state), dtype=torch.float32, device=self.device)
        done = torch.tensor(batch.done, dtype=torch.float32, device=self.device).unsqueeze(1)

        q_values = self.policy_net(state).gather(1, action)
        with torch.no_grad():
            q_next = self.target_net(next_state)
            max_q_next, _ = q_next.max(dim=1, keepdim=True)
            q_target = reward + (1.0 - done) * self.gamma * max_q_next

        loss = nn.functional.mse_loss(q_values, q_target)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
        self._soft_update()
        self.steps += 1
        return loss.item()

    def _soft_update(self):
        for param, target_param in zip(self.policy_net.parameters(), self.target_net.parameters()):
            target_param.data.copy_(self.tau * param.data + (1.0 - self.tau) * target_param.data)

    def save(self, path: str):
        torch.save(self.policy_net.state_dict(), path)

    def load(self, path: str):
        self.policy_net.load_state_dict(torch.load(path, map_location=self.device))
        self.target_net.load_state_dict(self.policy_net.state_dict())
