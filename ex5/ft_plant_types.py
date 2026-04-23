#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, starting_age: int) -> None:
        self._name = name.capitalize()
        if height < 0:
            self._height = 0.0
        else:
            self._height = height
        if starting_age < 0:
            self._age_days = 0
        else:
            self._age_days = starting_age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_days

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
        else:
            self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
        else:
            self._age_days = age

    def show(self) -> None:
        h = round(self._height, 1)
        if self._age_days == 0 or self._age_days == 1:
            print(f"{self._name}: {h}cm, {self._age_days} day old")
        else:
            print(f"{self._name}: {h}cm, {self._age_days} days old")

    def age(self) -> int:
        self._age_days += 1
        return self._age_days

