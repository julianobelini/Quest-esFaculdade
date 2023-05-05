#!/usr/bin/env python
#-*- coding:utf-8 -*-

import turtle

def desenhaPoli(t, tam, numlados):
    a = 360/numlados
    for i in range(numlados):
        t.forward(tam)
        t.left(a)

def desenhaTrianguloEqui(turtle, tamanho):
    desenhaPoli(turtle, tamanho, 3)

wn = turtle.Screen()
wn.bgcolor('pink')

tataruga = turtle.Turtle()

desenhaTrianguloEqui(tataruga, 200)

wn.exitonclick()

exit(0)