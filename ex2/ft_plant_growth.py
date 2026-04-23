#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float,
                 age: int, growth_rate: float) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age_days = age
        self.growth_rate = growth_rate

    def show(self) -> None:
        h = round(self.height, 1)
        if (self.age == 0 or self.age == 1):
            print(f"{self.name}: {h}cm, {self.age_days} day old")
        else:
            print(f"{self.name}: {h}cm, {self.age_days} days old")

    def age(self) -> int:
        self.age_days += 1
        return self.age_days

    def grow(self) -> float:
        self.height += self.growth_rate
        return self.height


if __name__ == "__main__":
    rose = Plant("Rose", 25.0, 30, 0.8)
    print("=== Garden Plant Growth ===")
    rose.show()

    starting_height = rose.height
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age()
        rose.show()
    total_growth = round(rose.height - starting_height, 1)
    print(f"Growth this week: {total_growth}cm")
