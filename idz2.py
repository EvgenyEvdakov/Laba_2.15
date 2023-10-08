#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    # Создаем два пустых списка для слов, следующих правилу, и нарушающих его
    words0 = []
    words1 = []

    # Открываем файл для чтения
    with open('idz2.txt', 'r') as file:
        # Читаем файл построчно
        for line in file:
            # Разбиваем строку на слова
            words = line.split()

            # Перебираем каждое слово
            for word in words:
                # Проверяем, содержит ли слово буквы E и I, и они идут друг за другом
                if 'ei' in word.lower() or 'ie' in word.lower():
                    # Проверяем, соответствует ли слово правилу
                    if 'cie' not in word.lower() and 'cei' not in word.lower():
                        words1.append(word)
                    else:
                        words0.append(word)

    # Убираем повторяющиеся слова из списков
    words0 = list(set(words0))
    words1 = list(set(words1))

    # Выводим списки и их длину на экран
    print("Слова, следующие правилу:")
    print(words0)
    print("Длина списка:", len(words0))

    print("\nСлова, нарушающие правило:")
    print(words1)
    print("Длина списка:", len(words1))