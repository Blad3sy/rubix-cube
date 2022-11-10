from random import randint, choice

class Face():

    def __init__(self, left, right, above, below):

        self.left = left
        self.right = right
        self.above = above
        self.below = below
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

    def push(self, direction, row, rowNum, vertical):

        direction.pull(row, rowNum, vertical)
    
    def pull(self, row, rowNum, vertical):

        if vertical:
            self.squaresV[rowNum] = row
            self.setSquares(False)
        else:
            self.squaresH[rowNum] = row
            self.setSquares(True)

def scramble(face1, face2, face3, face4, face5, face6):
    # generates 9 coordinates for each colour and allocates them
    # if coord is already occupied (not 0, which is white), generate new one
    # order is faceNum, rowNum, cellNum

    faceList = [face1, face2, face3, face4, face5, face6]

    for i in range(1, 6):
        for t in range(0, 9):
            allocatedFalse = True
            while allocatedFalse:
                faceSelect = choice(faceList)
                rowNum = randint(0, 2)
                cellNum = randint(0, 2)

                if faceSelect.squaresH[rowNum][cellNum] == 0:
                    faceSelect.squaresH[rowNum][cellNum] = i
                    faceSelect.squaresV[cellNum][rowNum] = i
                    allocatedFalse = False

face1 = Face(None, None, None, None)
face2 = Face(None, None, None, None)
face3 = Face(None, None, None, None)
face4 = Face(None, None, None, None)
face5 = Face(None, None, None, None)
face6 = Face(None, None, None, None)

face1.__init__(face2, face3, face4, face5)
face2.__init__(face6, face1, face4, face5)
face3.__init__(face1, face6, face4, face5)
face4.__init__(face2, face3, face6, face1)
face5.__init__(face2, face3, face1, face6)
face6.__init__(face2, face3, face5, face4)

scramble(face1, face2, face3, face4, face5, face6)

print(face1.squaresH)
print(face2.squaresH)
print(face3.squaresH)
print(face4.squaresH)
print(face5.squaresH)
print(face6.squaresH)