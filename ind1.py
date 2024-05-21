#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Pair:
    def __init__(self, first, second):
        if not isinstance(first, int) or first <= 0:
            raise ValueError("Поле first должно быть положительным целым числом.")
        if not isinstance(second, (int, float)) or second <= 0:
            raise ValueError("Поле second должно быть положительным числом.")
        self.first = first
        self.second = second

    def read(self):
        self.first = int(input("Введите калорийность 100 г продукта (целое положительное число): "))
        if self.first <= 0:
            raise ValueError("Поле first должно быть положительным целым числом.")
        self.second = float(input("Введите массу продукта в килограммах (дробное положительное число): "))
        if self.second <= 0:
            raise ValueError("Поле second должно быть положительным числом.")
    
    def display(self):
        print(f"Калорийность 100 г продукта: {self.first} ккал")
        print(f"Масса продукта: {self.second} кг")
    
    def power(self):
        return self.first * self.second * 10

    def __add__(self, other):
        if not isinstance(other, Pair):
            return NotImplemented
        return Pair(self.first + other.first, self.second + other.second)

    def __sub__(self, other):
        if not isinstance(other, Pair):
            return NotImplemented
        new_first = self.first - other.first
        new_second = self.second - other.second
        if new_first <= 0 or new_second <= 0:
            raise ValueError("Результат вычитания привёл к отрицательному или нулевому значению.")
        return Pair(new_first, new_second)

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        if scalar <= 0:
            raise ValueError("Множитель должен быть положительным числом.")
        return Pair(self.first * scalar, self.second * scalar)

    def __eq__(self, other):
        if not isinstance(other, Pair):
            return NotImplemented
        return self.first == other.first and self.second == other.second

def make_Pair(first, second):
    try:
        return Pair(first, second)
    except ValueError as e:
        print(e)
        return None

if __name__ == '__main__':
    pair1 = make_Pair(150, 0.5)
    pair2 = make_Pair(100, 1.0)

    if pair1 and pair2:
        pair1.display()
        pair2.display()
        
        pair3 = pair1 + pair2
        pair3.display()
        print(f"Общая калорийность продукта (pair3): {pair3.power()} ккал")
        
        try:
            pair4 = pair1 - pair2
            pair4.display()
            print(f"Общая калорийность продукта (pair4): {pair4.power()} ккал")
        except ValueError as e:
            print(e)
        
        pair5 = pair1 * 2
        pair5.display()
        print(f"Общая калорийность продукта (pair5): {pair5.power()} ккал")
        
        print(f"pair1 == pair2: {pair1 == pair2}")
        print(f"pair1 == pair1: {pair1 == pair1}")

    print("\nЧтение значений с клавиатуры:")
    pair = Pair(100, 1)
    pair.read()
    pair.display()
    print(f"Общая калорийность продукта: {pair.power()} ккал")