class Cat:
    def __init__(self, name, cat_type, color, age, steps_per_walk, steps_per_run):
        self.name = name
        self.cat_type = cat_type
        self.color = color
        self.age = age
        self.steps_per_walk = steps_per_walk
        self.steps_per_run = steps_per_run

    def run(self):
        return f"{self.name} runs at {self.steps_per_run} steps per second."

    def walk(self):
        return f"{self.name} walks at {self.steps_per_walk} steps per second."

    def meow(self):
        return f"{self.name} says 'Meow!'"
