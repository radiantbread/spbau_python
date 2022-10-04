#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Часть стандартной библиотеки с математическими функциями
import math
# Сторонняя библиотека с огромным количеством математических функций
import numpy
# Библиотека для графиков
import matplotlib.pyplot as mpp

# Похоже на функцию main в C-подобных языках.
if __name__ == '__main__':
    # Разбиение на равные отрезки
    arguments = numpy.arange(0, 400, 0.1)
    # Функция, задающая график
    mpp.plot(
        # Точки оси x
        arguments,
        # Соответствующие значения на оси y
        [math.sin(a) * math.sin(a/20.0) / (a + 0.1) for a in arguments]
    )
    mpp.show()  # Отображение графика :)
