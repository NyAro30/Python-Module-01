#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, starting_age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age_days = starting_age

    def show(self) -> None:
        h = round(self.height, 1)
        if self.age_days == 0 or self.age_days == 1:
            print(f"{self.name}: {h}cm, {self.age_days} day old")
        else:
            print(f"{self.name}: {h}cm, {self.age_days} days old")

    def age(self) -> int:
        self.age_days += 1
        return self.age_days


if __name__ == "__main__":
    rose = Plant("rose", 25.0, 30)
    oak = Plant("oak", 200.0, 365)
    cactus = Plant("cactus", 5.0, 90)
    sunflower = Plant("sunflower", 80.0, 45)
    fern = Plant("fern", 15.0, 120)

    plants = [rose, oak, cactus, sunflower, fern]

    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ", end ="")
        plant.show()
