

__author__ = 'ivo'

#import math
#import statistics


#Faecher

class Calc:          
    deutsch = 0               #Faechervariablen anlegen
    biologie = 0
    mathe = 0
    englisch = 0
    soziologie = 0
    geschichte = 0
    gotmarks = False         #noten abgefragt variable anlegen

inst = Calc()

def getmarks():             #Noten abfragen

    try:                                                #try weil leerer input=> Syntax Error

        inst.deutsch = input("deutschnote")             #abfrage der deutschnote

    except SyntaxError:                                 #Leerer input wird als 0 gewertet

        inst.deutsch = 0

    if inst.deutsch > 15:                               #alles über 15 wird als 15 gewertet
        inst.deutsch = 15
    elif inst.deutsch < 0:                              #negative einträge werden als null gewertet
        inst.deutsch = 0
        
    try:
        inst.biologie = int(input("biologienote"))      #bionote abfragen
    except SyntaxError:
        inst.biologie = 0
    if inst.biologie > 15:
        inst.biologie = 15
    elif inst.biologie < 0:
        inst.biologie = 0

    try:
        inst.mathe = input("mathenote")                #mathenote abfragen
    except SyntaxError:
        inst.mathe = 0
    if inst.mathe > 15:
        inst.mathe = 15
    elif inst.mathe < 0:
        inst.mathe = 0

    try:
        inst.englisch = input("englischnote")          #englischnote abfragen
    except SyntaxError:
        inst.englisch = 0
    if inst.englisch > 15:
        inst.englisch = 15
    elif inst.englisch < 0:
        inst.englisch = 0

    try:
        inst.soziologie = input("soziologienote")       #soziologienote abfragen
    except SyntaxError:
        inst.soziologie = 0
    if inst.soziologie > 15:
        inst.soziologie = 15
    elif inst.soziologie < 0:
        inst.soziologie = 0

    try:
        inst.geschichte = input("geschichtenote")        #geschichtsnote abfragen
    except SyntaxError:
        inst.geschichte = 0
    if inst.geschichte > 15:
        inst.geschichte = 15
    elif inst.geschichte < 0:
        inst.geschichte = 0

    inst.gotmarks = True

def calcandreturn():                                     #durchschnitt ausrechnen und ausgeben
    if inst.gotmarks is True:

        gesamt = float(inst.deutsch * 2 + inst.biologie * 2 + inst.mathe + inst.englisch + inst.soziologie + inst.geschichte)    #lk's doppelt werten float für kommazahlen

        durchschnittgesamt = float(gesamt / 8)      #durch die anzahl der kurse

        print str(durchschnittgesamt)               #ausgabe des durchschnittes

getmarks()

calcandreturn()
