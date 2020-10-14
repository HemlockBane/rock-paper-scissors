import random as r


class RockPaperScissors:
    def __init__(self):
        self.rating = 0

    def get_computer_choice(self):
        options = ["rock", "paper", "scissors"]
        r.seed()
        return r.choice(options)

    def determine_verdict_v2(self, user_choice, computer_choice):
        win_conditions = {"rock": "paper",
                          "paper": "scissors", "scissors": "rock"}
        win_condition = win_conditions[computer_choice]
        if user_choice == computer_choice:
            self.update_rating(50)
            return f"There is a draw ({computer_choice})"
        elif user_choice == win_condition:
            self.update_rating(100)
            return f"Well done. The computer chose {computer_choice} and failed"
        else:
            return f"Sorry, but the computer chose {computer_choice}"

    def update_rating(self, point):
        self.rating += point

    def display_rating(self):
        print(f"Your rating: {self.rating}")

    def init_rating(self, user_name):
        with open('rating.txt', 'r') as file:
            for line in file:
                name, score_str = line.strip('\n').split(" ")
                if name == user_name:
                    self.rating = int(score_str)
                    break

    def determine_verdict(self, user_choice, computer_choice):
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

    def play(self):
        user_name = input("Enter your name: ")
        print(f"Hello, {user_name}")

        self.init_rating(user_name)

        while True:
            user_choice = input().lower()
            if user_choice == "!exit":
                print("Bye!")
                break
            elif user_choice == "!rating":
                self.display_rating()
            elif user_choice in ["rock", "paper", "scissors"]:
                computer_choice = self.get_computer_choice()
                verdict = self.determine_verdict_v2(
                    user_choice, computer_choice)
                print(verdict)
            else:
                print("Invalid input")


rock_paper_scissors = RockPaperScissors()
rock_paper_scissors.play()
