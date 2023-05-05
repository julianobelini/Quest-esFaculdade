#!/usr/bin/env oython
#-*- coding:utf-8 -*-

import turtle

n = int(input('Digite o número de pontas da estrela: '))

def desenhaEstrela(t, tamanho, nLados):

    totalA = 180 * (nLados - 2)
    angulo = (180 - (totalA / nLados)) * 2
    
    for i in range(nLados):
        t.forward(tamanho)
        t.right(angulo)
    



if n >= 3 and (n % 2) == 1:
    wn = turtle.Screen()

    wn.bgcolor('blue')

    tataruga = turtle.Turtle()

    desenhaEstrela(tataruga, 100, n)

    wn.exitonclick()

else:
    
    exit(0)