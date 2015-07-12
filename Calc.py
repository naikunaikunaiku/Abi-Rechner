__author__ = 'ivo'

#import math
#import statistics


#Faecher

class Calc:
    deutsch = 0
    biologie = 0
    mathe = 0
    englisch = 0
    soziologie = 0
    geschichte = 0
    gotmarks = False

inst = Calc()

def getmarks():
    inst.deutsch = input("deutschnote")
    inst.biologie = input("biologienote")
    inst.mathe = input("mathenote")
    inst.englisch = input("englischnote")
    inst.soziologie = input("soziologienote")
    inst.geschichte = input("geschichtenote")
    inst.gotmarks = True

def calcandreturn():
    if inst.gotmarks is True:

        gesamt = float(inst.deutsch * 2 + inst.biologie * 2 + inst.mathe + inst.englisch + inst.soziologie + inst.geschichte)

        durchschnittgesamt = float(gesamt / 8)

        print str(durchschnittgesamt)

getmarks()

calcandreturn()
