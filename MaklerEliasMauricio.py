# Online Python - IDE, Editor, Compiler, Interpreter
wohnung = input("Bitte gib den Kundennamen ein!")
add = "ja"
roomDict = {}
totalArea = 0

def calcArea(x, y):
    return x * y 
while(add == "ja"):
    add = input("möchten Sie ein Zimmer ausmessen? (ja/nein)")
    print(""" Info: \n Wir berechnen die Fläche des Raumes, dazu bitten wir Sie, die Mittel der breitesten Wand und der längsten Wand einzugeben,\n wobei Folgendes zu berücksichtigen ist:
    wenn der Raum nicht viereckig ist, dann subtrahieren Sie die Fläche (a*b) von dem Raum.

breiteste Wand
 ___ ___
|         |
|__a__    |längsten Wand
|/////|b  | 
|/////|__ |

""")
    if(add.lower() == "ja"):
        room = input("Bitte gib den Namen des Zimmers ein")
 

        wallLength = float(input("Bitte geben Sie die Länge der längsten Wand in metern ein"))
        wallWidth = float(input("Bitte geben Sie die breiteste Wand in metern ein"))
    
        
        roomArea = calcArea(wallLength, wallWidth)    
        totalArea += roomArea
    
    
        roomDict.update({room: roomArea})
        minus = "ja"
        while(minus == "Ja" or minus == "ja"):
            minus = input ("Möchten Sie eine Fläche vom Raum subtrahieren ? ja oder Nein")
            if(minus == "Ja" or minus == "ja"):
                minusRoomLength = float(input("Bitte geben Sie a (die Wandlänge) in metern ein"))
                minusRoomWidth = float(input("Bitte geben Sie b (die Wandbreite) in metern ein"))
                minusRoomArea = calcArea(minusRoomLength, minusRoomWidth)
                roomDict[room] = roomArea - minusRoomArea
                totalArea -= minusRoomArea
            elif(minus == "Nein" or minus == "nein"):
                break
            else: 
                print("Du bist Doof")
                continue
    else:
        break
roomDict["Total"] = totalArea
print("Hallo, ", wohnung, " deine Messungen sind:\n", roomDict)


