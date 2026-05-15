class Player:
    team = "Paxtakor"

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def show_info(self):
        print(f"Ism: {self.name}")
        print(f"Raqam: {self.number}")


p1 = Player("Jasur", 10)
p2 = Player("Ali", 7)

p1.show_info()
print("----------")
p2.show_info()
