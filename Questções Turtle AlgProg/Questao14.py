#!/usr/bin/env python
#-*- coding:utf-8 -*-

raiz = int(input("Digita a raiz:"))



def tentaRaiz(n):

    testeantigo = n/2

    testeatual = ((testeantigo + n)/testeantigo)/2

    nteste = 0

    verifi = "sim"

    while verifi == "sim":

        if testeantigo ** 2 == n:
            print("Resultado bateu, numero do teste %d, valor %2f = rais quadrada de %d"%(nteste , testeantigo, n))
            verifi = "nao"
        else:
            print("Numero do teste %d, valor %2f != rais quadrada de %d"%(nteste , testeatual, n))
            testeantigo = testeatual
            testeatual = (testeantigo + n/testeantigo)/2
            nteste +=1
            verifi = (input("Quer continuar? Digite sim ou nao"))





tentaRaiz(raiz)

exit(0)