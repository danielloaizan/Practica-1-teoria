# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 14:01:26 2021

@author: Daniel
"""

class Automata:
    def __init__(self,cadena):
        self.cadena=cadena
        
    
    
    def leerArchivo(self):
        with open('prueba.txt', 'r') as f:
            for linea in f:
                linea=f.readline()
                

class nodoSimple:
    clase=0
    valor=0
    posicionMemoria=0
    liga=0
    
    def __init__(self,clase,valor,posicionMemoria,liga):
        self.clase=clase
        self.valor=valor 
        self.posicionMemoria=posicionMemoria
        self.liga=liga
    
    def retornaClase(self):
        return str(self.clase);
    
    def retornaValor(self):
        return str(self.valor);
    
    def retornaLiga(self):
        return str(self.liga);
    
    def retornPosicionMemoria(self):
        return str(self.posicionMemoria);
                



class listaSimpleLigada:
    nodoSimple=0
    primero=0
    ultimo=0
    
    def __init__(self,primero,ultimo):
        self.primero=0
        self.ultimo=0
        
    def esVacia(self,primero):
        if primero==0:
            return True
        else:
            return False
        
    def primerNodo(self):
        return str(self.primero)
    
    def ultimoNodo(self):
        return str(self.ultimo)
    
    def finDeRecorrido(self,nodoSimple ):
        if nodoSimple=="null":
            return True
        else: 
            return False
    
    def recorre (self):
        nodo=nodoSimple(0,0,1,0)
        while finDeRecorrido(nodo)==False:
            print(nodo.retornPosicionMemoria())
            print (nodo.retornaClase(),nodo.retornaValor())
    
    def insertar(self,listaSimpleLigada,nodoSimple):
        nodo=nodoSimple(0,0,ultimo,0)
        
    
    def conectar(self,nodoSimple,nodoSimple2):
        nodoSimple.asignaPosicionMemoria(nodoSimple2.retornPosicionMemoria())
        nodoSimple2.asignaPosicionMemoria(ultimoNodo)
        
        
        
        

    
    def asignaClase(tipo):
        clase=tipo
    def asignaValor(tipo):
        valor=tipo
    def asignaLiga(tipo):
        liga=tipo
    def asignaPosicionMemoria(tipo):
        posicionMemoria=tipo
        
class Pila:
     def __init__(self):
         self.items = []

     def estaVacia(self):
         return self.items == []

     def incluir(self, item):
         self.items.append(item)

     def extraer(self):
         return self.items.pop()

     def inspeccionar(self):
         return self.items[len(self.items)-1]

     def tamano(self):
         return len(self.items)