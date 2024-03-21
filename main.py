def main():
    print("Welcome the Wild where you will fight for your life!")
    print()
    print("What is your class?")


class character:
    def __init__(self, Job, name, race):
        self.health = 10
        self.mana = 25
        self.stamina = 10
        self.name = name


class Job:
    def __init__(self, name):
        self.name = character.name


class race:
    def __init__(self):
        self.health = 10


class iventory:
    def __init__(self, bag):
        self.bag = bag


main()
