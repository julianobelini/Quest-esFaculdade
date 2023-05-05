#!/usr/bin/env python
#-*- coding:utf-8 -*-

import turtle

tataruga = turtle.Turtle()

def desenhaEstrela(nome,tam):

    for i in range(5):
        nome.forward(tam)
        nome.right(144)

wn = turtle.Screen()
wn.bgcolor('blue')


for i in range(5):
    
    desenhaEstrela(tataruga , 100)
    tataruga.up()
    tataruga.forward(350)
    tataruga.right(144)
    tataruga.down()





wn.exitonclick()

exit(0)