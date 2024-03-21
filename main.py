def main():
    print("Welcome the Wild where you will fight for your life!")
    print()


class character:
    def __init__(self, Job, name):
        self.health = 10
        self.mana = 25
        self.stamina = 10
        self.name = name


class Job:
    def __init__(self):
        self.name = character.name
