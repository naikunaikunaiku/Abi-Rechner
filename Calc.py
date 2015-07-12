

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

    inst.deutsch = str(input("deutschnote"))
    if inst.deutsch > 15:
        inst.deutsch = 15
    elif inst.deutsch < 0:
        inst.deutsch = 0
    inst.biologie = int(input("biologienote"))
    if inst.biologie > 15:
        inst.biologie = 15
    elif inst.biologie < 0:
        inst.biologie = 0
    inst.mathe = input("mathenote")
    if inst.mathe > 15:
        inst.mathe = 15
    elif inst.mathe < 0:
        inst.mathe = 0
    inst.englisch = input("englischnote")
    if inst.englisch > 15:
        inst.englisch = 15
    elif inst.englisch < 0:
        inst.englisch = 0
    inst.soziologie = input("soziologienote")
    if inst.soziologie > 15:
        inst.soziologie = 15
    elif inst.soziologie < 0:
        inst.soziologie = 0
    inst.geschichte = input("geschichtenote")
    if inst.geschichte > 15:
        inst.geschichte = 15
    elif inst.geschichte < 0:
        inst.geschichte = 0
    inst.gotmarks = True

def calcandreturn():
    if inst.gotmarks is True:

        gesamt = float(inst.deutsch * 2 + inst.biologie * 2 + inst.mathe + inst.englisch + inst.soziologie + inst.geschichte)

        durchschnittgesamt = float(gesamt / 8)

        print str(durchschnittgesamt)

getmarks()

calcandreturn()
