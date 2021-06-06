class GenerateRandomness:
    def __init__(self):
        self.number = ''
        self.profile = {"000": [0, 0], "001": [0, 0], "010": [0, 0], "011": [0, 0],
                        "100": [0, 0], "101": [0, 0], "110": [0, 0], "111": [0, 0]}
        self.money = 1000

    def get_number(self):
        print(f"The current data length is {len(self.number)}, {100 - len(self.number)} symbols left")
        data = input('Print a random string containing 0 or 1:\n\n')
        for x in data:
            if x == '0' or x == '1':
                self.number += x
        if len(self.number) < 100:
            self.get_number()
        else:
            self.generate_profile()

    def generate_profile(self):
        for y in range(len(self.number)):
            try:
                self.number[y + 3]
            except IndexError:
                break
            else:
                if self.number[y + 3] == "0":
                    self.profile[self.number[y:y + 3]][0] += 1
                elif self.number[y + 3] == "1":
                    self.profile[self.number[y:y + 3]][1] += 1
        print(f"\nFinal data string:\n{self.number}\n")
        print("")
        print("You have $1000. Every time the system successfully predicts your next press, you lose $1.")
        print('Otherwise, you earn $1. Print "enough" to leave the game.' +  "Let's go!")
        print("")


    def prediction(self):
        self.get_number()
        while True:
            try:
                test_string = input("Print a random string containing 0 or 1:\n\n")
                if test_string == "enough":
                    return False
                prediction_string = test_string[:3]
                total = len(test_string) - 3
                for number in range(total):
                    triad = test_string[number:number + 3]
                    prediction_string += '0' if self.profile[triad][0] >= self.profile[triad][1] else '1'
                correct = 0
                for x in range(total):
                    if prediction_string[x] == test_string[x]:
                        correct += 1
                print(f"prediction:\n{prediction_string}\n")
                print("Computer guessed right {} out of {} symbols ({:.2f} %)".format(correct,
                                                                                    total,
                                                                                    correct / total * 100))
                self.game(correct,total)
            except:
                pass

    def game(self,correct,total):
        incorrect = total-correct
        if correct > 0:
            self.money +=incorrect-correct
        else:
            self.money +=incorrect-correct
        print(f"Your capital is now ${self.money}")

print("Please give AI some data to learn...")
GenerateRandomness().prediction()
print("Game over!")


