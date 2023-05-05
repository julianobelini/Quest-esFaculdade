#!/usr/bin/env python
#-*- coding:utf-8 -*-

n = int(input("Digita ai namoral:"))

def somaAte(n):

    soma = 0

    for i in range(n):

        soma+= i+1

    return soma


print(somaAte(n))

exit(0)