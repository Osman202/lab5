#!/usr/bin/env python3
# -*- config: utf-8 -*-

# Вариант 1
# Дано название футбольного клуба. Напечатать его на экране «столбиком».
if __name__ == '__main__':
    n = input("Введите название футбольного клуба")

    for i in n:
        print(f"{i}")
