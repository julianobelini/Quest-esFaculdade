#!/usr/bin/env oython
#-*- coding:utf-8 -*-

import turtle

n = int(input('Digite o número de pontas: '))
t = int(input('Digite o tamanho: '))

def desenhaEstrela(t, tamanho, nLados):

    angulo = 360 / nLados
    
    for i in range(nLados):
        t.forward(tamanho)
        t.backward(tamanho)
        t.right(angulo)



wn = turtle.Screen()

wn.bgcolor('blue')

tataruga = turtle.Turtle()

desenhaEstrela(tataruga, 100, n)

wn.exitonclick()


    
exit(0)