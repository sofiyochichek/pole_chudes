#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random

words = ["абривиатура", "Авоська", "Подросток", "Разочаровываться", "Послушание", "Сковорода", "Болтливость", "Гавкает", "Правда", "Чихание", "Теща", "Буревестник", "Алкогольный", "Одиночество", "Уверенность", "Война", "Чемодан", "Багаж", "Бесплодие", "Походка", "Сарафан"]
for i in range(len(words)):
    words[i] = words[i].lower()
hearts = 0
level_choice = input("Введите уровень 1-easy; 2-normal; 3-hard\n Введите end, если хотите выйти: ").lower()

def pole_chudes(words, hearts, level_choice):
    while True:
        while True:
            random_word = random.choice(words)
            squares = ['\u25A0' for number in range(len(random_word))]
            squares = "".join(squares)
            if level_choice == "1":
                hearts = 8
                break
            elif level_choice == "2":
                hearts = 5
                break
            elif level_choice == "3":
                hearts = 3
                break
            elif level_choice == "end":
                return 0
            else:
                level_choice = input("Введите уровень 1-easy; 2-normal; 3-hard\n Введите end, если хотите выйти: ").lower()

        words.remove(random_word)
        print(f"{squares}    | ♥ x {hearts}")
        words_choice = input("Введите букву или слово целиком\n Введите end, если хотите выйти: ").lower()
        while True:
            if hearts == 1:
                print("Ой, кажется у тебя закончились сердца \n")
                print(f"Верный ответ: {random_word}")
                level_choice = input("Введите уровень 1-easy; 2-normal; 3-hard\n Введите end, если хотите выйти: ").lower()
                break
            elif words_choice == random_word:
                print("Поздравляю, ты победил!\n")
                level_choice = input("Введите уровень 1-easy; 2-normal; 3-hard\n Введите end, если хотите выйти: ").lower()
                break
            elif len(words_choice) == 1 and words_choice in random_word:
                random_word = list(random_word)
                squares = [i for i in squares]
                for letterIndex in range(len(random_word)):
                    if squares[letterIndex] == "\u25A0" and random_word[letterIndex] == words_choice:
                        squares[letterIndex] = words_choice
                random_word = "".join(random_word)
                squares = "".join(squares)
                if squares == random_word:
                    print("Поздравляю, ты победил!\n")
                    level_choice = input("Введите уровень 1-easy; 2-normal; 3-hard\n Введите end, если хотите выйти: ").lower()
                    break
                else:
                    print(f"{squares}    | ♥ x {hearts}")
                    words_choice = input("Введите букву или слово целиком\n Введите end, если хотите выйти: ").lower()
                    continue
            elif len(words_choice) == 1 and words_choice not in random_word:
                hearts -= 1
                print(f"{squares}    | ♥ x {hearts}")
                words_choice = input("Введите букву или слово целиком\n Введите end, если хотите выйти: ").lower()
                continue
            elif words_choice == "end":
                return 0
            else:
                hearts -= 1
                print(f"{squares}    | ♥ x {hearts}")
                words_choice = input("Введите букву или слово целиком\n Введите end, если хотите выйти: ").lower()
                continue


print(pole_chudes(words, hearts, level_choice))