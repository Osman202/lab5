#!/usr/bin/env python3
# - *- config: utf-8 -*-

# Вариант 12
# Путем вставок и удаления символов исправить ошибки:
# в слове прроцесор;
# во фразе теекстовыйфайл;
# во фразе програма и аллгоритм;
# во фразе процесор и паммять.
if __name__ == '__main__':
    s1 = 'пррцесор'
    s2 = 'теекстовыйфайл'
    s3 = 'програма и аллгоритм'
    s4 = 'процесор и паммять'

    s11 = s1.find('пр')
    s12 = s1.find('цес')
    s13 = s1.find('ор')
    s21 = s2.find('екстовый')
    s22 = s2.find('файл')
    s31 = s3.find('програм')
    s32 = s3.find('а и а')
    s33 = s3.find('лгоритм')
    s41 = s4.find('процес')
    s42 = s4.find('ор и')
    s43 = s4.find('мять')

    s1 = s1[s11:s12-1] + 'o' + s1[s12:s13] + 'c' + s1[s13:]
    s2 = s2[s21-2] + s2[s21:s22] + ' ' + s2[s22:]
    s3 = s3[s31:s32] + 'м' + s3[s32:s33-1] + s3[s33:]
    s4 = s4[s41:s42] + 'c' + s4[s42:s43-1] + s4[s43:]

    print(
          f"пррцесор = {s1}\n"
          f"теекстовыйфайл = {s2}\n"
          f"програма и аллгоритм = {s3}\n"
          f"процесор и паммять = {s4}\n"
    )
