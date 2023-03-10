from random import randint, choice
from PyQt5 import QtCore
from guiConstruction import Main_Window, Button, Label, Image, Grid

class Face():

    def __init__(self, left = None, right = None, above = None, below = None, opposite = None):

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
            self.above.setSquares(False)
            self.opposite.setSquares(False)
            self.below.setSquares(False)
        
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
            self.left.setSquares(True)
            self.opposite.setSquares(True)
            self.right.setSquares(True)

def scramble(face1, face2, face3, face4, face5, face6):

    faceList = [face1, face2, face3, face4, face5, face6]
    directionList = ["L", "R", "U", "D"]

    for i in range(0, 6):
        faceList[i].squaresH = [[i, i, i], [i, i, i], [i, i, i]]
        faceList[i].setSquares(True)

    for i in range(0, 100):
        faceChose = choice(faceList)
        directionChose = choice(directionList)
        rowChose = randint(0, 2)

        faceChose.push(directionChose, rowChose)
    
    print(" ")

class Rubix_Face():

    def __init__(self, parent, gridmap, baseFace):
        self.parent = parent
        self.grid = Grid(self.parent)
        self.grid.setSpacing(3)

        self.gridmap = gridmap
        self.baseFace = baseFace

        self.faceToPush = baseFace

        self.add_Grid_Elements()

    def add_Grid_Elements(self):
        for i in range(1, 4):
            for t in range(1, 4):
                gridItem = Image(self.grid, f"rubix-cube/images/{self.gridmap[i-1][t-1]}.png", 100, 100, True, "L")
                self.grid.addWidget(gridItem, i, t)

        button = Button(self.grid, lambda: self.button_Push("U", 0), "PUSH")
        self.grid.addWidget(button, 0, 1, alignment=QtCore.Qt.AlignBottom)

        button2 = Button(self.grid, lambda: self.button_Push("U", 1), "PUSH")
        self.grid.addWidget(button2, 0, 2, alignment=QtCore.Qt.AlignBottom)

        button3 = Button(self.grid, lambda: self.button_Push("U", 2), "PUSH")
        self.grid.addWidget(button3, 0, 3, alignment=QtCore.Qt.AlignBottom)

        button4 = Button(self.grid, lambda: self.button_Push("L", 0), "PUSH")
        self.grid.addWidget(button4, 1, 0, alignment=QtCore.Qt.AlignRight)

        button5 = Button(self.grid, lambda: self.button_Push("L", 1), "PUSH")
        self.grid.addWidget(button5, 2, 0, alignment=QtCore.Qt.AlignRight)

        button6 = Button(self.grid, lambda: self.button_Push("L", 2), "PUSH")
        self.grid.addWidget(button6, 3, 0, alignment=QtCore.Qt.AlignRight)

        button7 = Button(self.grid, lambda: self.button_Push("D", 0), "PUSH")
        self.grid.addWidget(button7, 4, 1, alignment=QtCore.Qt.AlignTop)

        button8 = Button(self.grid, lambda: self.button_Push("D", 1), "PUSH")
        self.grid.addWidget(button8, 4, 2, alignment=QtCore.Qt.AlignTop)

        button9 = Button(self.grid, lambda: self.button_Push("D", 2), "PUSH")
        self.grid.addWidget(button9, 4, 3, alignment=QtCore.Qt.AlignTop)

        button10 = Button(self.grid, lambda: self.button_Push("R", 0), "PUSH")
        self.grid.addWidget(button10, 1, 4, alignment=QtCore.Qt.AlignLeft)

        button11 = Button(self.grid, lambda: self.button_Push("R", 1), "PUSH")
        self.grid.addWidget(button11, 2, 4, alignment=QtCore.Qt.AlignLeft)

        button12 = Button(self.grid, lambda: self.button_Push("R", 2), "PUSH")
        self.grid.addWidget(button12, 3, 4, alignment=QtCore.Qt.AlignLeft)

        button13 = Button(self.grid.parent, self.button_Change_Face, "CHANGE FACE")
        self.grid.addWidget(button13, 5, 2, alignment=QtCore.Qt.AlignCenter)

    
    def button_Push(self, direction, colrow):
        self.faceToPush.push(direction, colrow)
        
        nullNotFound = False

        while nullNotFound:
            deleter = self.grid.findChild()
            if deleter == None:
                nullNotFound = False
            else:
                deleter.delete()
        
        self.add_Grid_Elements()
    
    def button_Change_Face(self):

        global selectedFaceNum
        global selectedFace
        global faceOrder

        selectedFaceNum += 1
        if selectedFaceNum == 5:
            selectedFaceNum = 0
        
        selectedFace = faceOrder[selectedFaceNum]
        self.gridmap = selectedFace.squaresH
        self.baseFace = selectedFace

        nullNotFound = False

        while nullNotFound:
            deleter = self.grid.findChild()
            if deleter == None:
                nullNotFound = False
            else:
                deleter.delete()
            
        self.add_Grid_Elements()

faceOrder = []

face1 = Face()
faceOrder.append(face1)
face2 = Face()
faceOrder.append(face2)
face3 = Face()
faceOrder.append(face3)
face4 = Face()
faceOrder.append(face4)
face5 = Face()
faceOrder.append(face5)
face6 = Face()
faceOrder.append(face6)

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

mainWin = Main_Window("Rubik's Cube!", 500, 500)
selectedFaceNum = 0
selectedFace = faceOrder[selectedFaceNum]

mainFace = Rubix_Face(mainWin.lay, selectedFace.squaresH, selectedFace)

mainWin.app.exit(mainWin.app.exec_())