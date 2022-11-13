from random import randint, choice

class Face():

    def __init__(self, left, right, above, below, opposite):

        self.left = left
        self.right = right
        self.above = above
        self.below = below
        self.opposite = opposite
        self.squaresH = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.squaresV = [[None, None, None], [None, None, None], [None, None, None]]

        self.setSquares(True)
    
    def setSquares(self, vertical):

        if vertical:
            for i in range(0, 3):
                for t in range(0, 3):
                    self.squaresV[i][t] = self.squaresH[t][i] 
        else:
            for i in range(0, 3):
                for t in range(0, 3):
                    self.squaresH[i][t] = self.squaresV[t][i]          

    def push(self, direction, rowNum):

        if direction == "U" or direction == "D":

            # TODO : FIX BUG THAT CAUSES DUPLICATION / DELETION OF NUMBERS WHEN PUSHING UP OR DOWN
            
            original = self.squaresV[rowNum]
            above = self.above.squaresV[rowNum]
            opposite = self.opposite.squaresV[rowNum]
            below = self.below.squaresV[rowNum]

            if direction == "U":
                self.squaresV[rowNum] = below
                self.above.squaresV[rowNum] = original
                self.opposite.squaresV[rowNum] = above
                self.below.squaresV[rowNum] = opposite
            else:
                self.squaresV[rowNum] = above
                self.above.squaresV[rowNum] = opposite
                self.opposite.squaresV[rowNum] = below
                self.below.squaresV[rowNum] = original
        
            self.setSquares(False)
        
        else:
            original = self.squaresH[rowNum]
            left = self.left.squaresH[rowNum]
            opposite = self.opposite.squaresH[rowNum]
            right = self.right.squaresH[rowNum]

            if direction == "L":
                self.squaresH[rowNum] = right
                self.left.squaresH[rowNum] = original
                self.opposite.squaresH[rowNum] = left
                self.right.squaresH[rowNum] = opposite
            else:
                self.squaresH[rowNum] = left
                self.left.squaresH[rowNum] = opposite
                self.opposite.squaresH[rowNum] = right
                self.right.squaresH[rowNum] = original
            
            self.setSquares(True)

def scramble(face1, face2, face3, face4, face5, face6):

    faceList = [face1, face2, face3, face4, face5, face6]
    directionList = ["L", "R", "U", "D"]

    t = 0

    for i in range(0, 6):
        faceList[i].squaresH = [[t, t, t], [t, t, t], [t, t, t]]
        faceList[i].setSquares(True)

        t += 1

        print(f"face{t} set")
        print(faceList[i].squaresH)
        print(faceList[i].squaresV)

    for i in range(0, 21):
        faceChose = choice(faceList)
        directionChose = choice(directionList)
        rowChose = randint(0, 2)

        faceChose.push(directionChose, rowChose)
    
    print(" ")

face1 = Face(None, None, None, None, None)
face2 = Face(None, None, None, None, None)
face3 = Face(None, None, None, None, None)
face4 = Face(None, None, None, None, None)
face5 = Face(None, None, None, None, None)
face6 = Face(None, None, None, None, None)

# ORDER IS LEFT RIGHT ABOVE BELOW OPPOSITE
# REFERENCE IS HOLDING CUBE LOOKING AT FACE1
# FACE1 IS WHITE, FACE2 IS GREEN, FACE3 IS YELLOW, FACE4 IS BLUE, FACE5 IS ORANGE, FACE6 IS RED

face1.__init__(face2, face4, face5, face6, face3)
face2.__init__(face3, face1, face5, face6, face4)
face3.__init__(face4, face2, face5, face6, face1)
face4.__init__(face1, face3, face5, face6, face2)
face5.__init__(face2, face4, face3, face1, face6)
face6.__init__(face2, face4, face1, face3, face5)

scramble(face1, face2, face3, face4, face5, face6)

print(face1.squaresH)
print(face2.squaresH)
print(face3.squaresH)
print(face4.squaresH)
print(face5.squaresH)
print(face6.squaresH)

face1.push("L", 2)
print("PUSHED")

print(face1.squaresH)
print(face2.squaresH)
print(face3.squaresH)
print(face4.squaresH)
print(face5.squaresH)
print(face6.squaresH)