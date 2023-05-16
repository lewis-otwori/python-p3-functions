#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name = "Guido!"):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    return(45 + 55)

def halve(number):
    if type(number) != "number":
        return number / 2
