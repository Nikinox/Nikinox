# LDF
## Little Distrobox Fix
This is a little command to paste inside your container so that every time you log in it there's a label that shows it.

**Why I built this:**

Distrobox has a little problem (or at least there is this bug in my one):

Sometimes it doesn't print anything to confirm you're logged in the container, so you don't know if it crashed or something.

**What it does:**

It prints a little message every time you log in the container.

By doing this, there's no doubt the container launched successfully.

**How to use it:**

Follow these steps:

     - Go to the file fix.sh
     - Replace the [] with the name you prefer
     - Paste it inside the shell of the container
And now, every time you log in that container, the message will pop up.
