#!/usr/bin/env python
#-*- coding:utf-8 -*-

import turtle

def desenhaEstrela(tam):
    rafa = turtle.Turtle()
    for i in range(5):
        rafa.forward(tam)
        rafa.right(144)

wn = turtle.Screen()
wn.bgcolor('blue')

desenhaEstrela(100)

wn.exitonclick()

exit(0)