import random as r


def get_computer_choice():
    options = ["rock", "paper", "scissors"]
    return r.choice(options)


def determine_verdict_v2(user_choice, computer_choice):
    win_conditions = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
    win_condition = win_conditions[computer_choice]
    if user_choice == computer_choice:
        return f"There is a draw ({computer_choice})"
    elif user_choice == win_condition:
        return f"Well done. The computer chose {computer_choice} and failed"
    else:
        return f"Sorry, but the computer chose {computer_choice}"


def determine_verdict(user_choice, computer_choice):
    if user_choice == computer_choice:
        return f"There is a draw ({computer_choice})"
    elif computer_choice == "rock":
        if user_choice == "paper":
            return f"Well done. The computer chose {computer_choice} and failed"
        return f"Sorry, but the computer chose {computer_choice}"
    elif computer_choice == "paper":
        if user_choice == "scissors":
            return f"Well done. The computer chose {computer_choice} and failed"
        return f"Sorry, but the computer chose {computer_choice}"
    elif computer_choice == "scissors":
        if user_choice == "rock":
            return f"Well done. The computer chose {computer_choice} and failed"
        return f"Sorry, but the computer chose {computer_choice}"


user_choice = input()
computer_choice = get_computer_choice()
verdict = determine_verdict_v2(user_choice, "paper")
print(verdict)
