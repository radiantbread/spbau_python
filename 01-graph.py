#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math # Часть стандартной библиотеки с математическими функциями
import numpy # Сторонняя библиотека с огромным количеством математических функций
import matplotlib.pyplot as mpp # Библиотека для графиков

# Эта программа рисует график функции, заданной выражением ниже

if __name__=='__main__':
    arguments = numpy.arange(0, 400, 0.1) # Разбиение на равные отрезки
    mpp.plot(
        arguments, # Точки оси x
        [math.sin(a) * math.sin(a/20.0) / (a + 0.1) for a in arguments] # Соответствующие значения на оси y
    )
    mpp.show() # Отображение графика :)
