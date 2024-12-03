#? https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python
#Du lebst in der Stadt Cartesia, wo alle Straßen in einem perfekten Raster angeordnet sind. 
# Du bist zehn Minuten zu früh zu einem Termin gekommen, also hast du beschlossen, 
# die Gelegenheit für einen kurzen Spaziergang zu nutzen. Die Stadt bietet ihren Bürgern eine “Spaziergangs-Generator-App” 
# auf ihren Handys an – jedes Mal, wenn du den Button drückst, erhältst du ein Array mit einzelnen Buchstaben, 
# die die Gehrichtungen angeben (z. B. ['n', 's', 'w', 'e']).

#Du gehst immer nur einen einzigen Block pro Buchstaben (Richtung), 
# und du weißt, dass es genau eine Minute dauert, einen Block zu durchqueren.

#Aufgabe:
#Erstelle eine Funktion, die true zurückgibt, wenn der Spaziergang, den die App vorschlägt:
#	1.	Genau zehn Minuten dauert und
#	2.	Dich wieder an deinen Ausgangspunkt zurückführt.

#Gibt die Funktion false zurück, falls eine der beiden Bedingungen nicht erfüllt ist.

#                       N
#
#             W                     e
#
#                       S

#! Eigene Lösung
walk = ['w','e','w','e','w','e','w','e','w','e','w','e']
def is_valid_walk(walk):
    richtungen =[0,0]
    loesung = False
    z = 0
    for i in walk:
        if i == "n":
            richtungen[0] += 1
        elif i == "s":
            richtungen[0] -= 1
        elif i == "e":
            richtungen[1] += 1
        elif i == "w":
            richtungen[1] -= 1
    if richtungen[0] == 0 and richtungen[1]== 0:
        z += 1 
    if len(walk) == 10:
        z += 1
    if z == 2:
        loesung = True
    else: loesung = False
    return loesung        
print(is_valid_walk(walk))

#! So einfach kann es gehen :)
def isValidWalk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')
        
    

