#makes the tool run in a loop until we want
ans_q="yes"
while ans_q=="yes":
    #saves all the answers
    role_q=str(input("Insert the role you wanna give the AI:\n"))
    context_q= str(input("Set the context and give the AI and some background to guide the response:\n"))
    task_q=str(input("Set the task clearly(be as specific as possible):\n"))
    format_q=str(input("Set the format for the answer(such as a spreadsheet, bullet list, a specific number of words etc.):\n"))
    rules_q=str(input("Set clear boundaries for the answer, the things you DON'T want in the answer:\n"))
    examples_q=str(input("Give the AI some examples(if they're in files, just attach them when you're going to paste the prompt):\n"))
    #asks if he wants to copy the prompt checking the answer
    while ans_q := str(input("Do you want to copy the prompt in the clipboard?\n").lower()) not in ["yes", "no", "y", "n", "s"]:
        print("error, insert again\n")
    #prints the final prompt
    print(role_q)
    print(context_q)
    print(task_q)
    print(format_q)
    print(rules_q)
    print(examples_q)
    while ans_q := str(input("Do you want to continue?\n").lower()) not in ["yes", "no", "y", "n", "s"]:
        print("error, insert again\n")
    if ans_q not in ["yes", "y", "s"]:
        ans_q=False
    else:
        ans_q="yes"
