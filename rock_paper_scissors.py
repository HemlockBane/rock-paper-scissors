import random as r


class RockPaperScissors:
    def __init__(self):
        self.rating = 0
        self.game_options = ["rock", "paper", "scissors"]

    def get_computer_choice(self):
        options = ["rock", "paper", "scissors"]
        r.seed()
        return r.choice(options)

    def shift(self, diff):
        if diff < 0:
            diff = -diff
            return self.game_options[diff:] + self.game_options[:diff]  # left shift
        elif diff > 0:
            return self.game_options[-diff:] + self.game_options[:-diff]  # right shift

    def determine_verdict_v2(self, user_choice, computer_choice):
        mid_idx = len(self.game_options)//2  # middle of array
        user_input_idx = self.game_options.index(user_choice)
        diff = mid_idx - user_input_idx
        if diff != 0:
            self.game_options = self.shift(diff)

        loss_conditions = self.game_options[:mid_idx]
        win_conditions = self.game_options[mid_idx + 1:]
        # print(self.game_options)
        # print(loss_conditions)
        # print(win_conditions)

        if computer_choice == user_choice:
            self.update_rating(50)
            return f"There is a draw ({computer_choice})"
        elif computer_choice not in win_conditions:
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

        user_game_options = input()
        if len(user_game_options) != 0:
            self.game_options = user_game_options.split(",")

        print("Okay, let's start")
        while True:
            user_choice = input().lower()

            if user_choice == "!exit":
                print("Bye!")
                break
            elif user_choice == "!rating":
                self.display_rating()
            elif user_choice in self.game_options:
                computer_choice = self.get_computer_choice()
                verdict = self.determine_verdict_v2(
                    user_choice, computer_choice)
                print(verdict)
            else:
                print("Invalid input")


rock_paper_scissors = RockPaperScissors()
rock_paper_scissors.play()