class Face():

    def __init__(self, left, right, above, below):

        self.left = left
        self.right = right
        self.above = above
        self.below = below

        self.squaresV = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
        self.squaresH = [[self.squaresV[0][0], self.squaresV[1][0], self.squaresV[2][0]], [self.squaresV[0][1], self.squaresV[1][1], self.squaresV[2][1]], [self.squaresV[0][2], self.squaresV[1][2], self.squaresV[2][2]]]

    def push(self, direction, row, rowNum, vertical):

        direction.pull(row, rowNum, vertical)
    
    def pull(self, row, rowNum, vertical):

        if vertical:
            self.squaresV[rowNum] = row
            self.squaresH = [[self.squaresV[0][0], self.squaresV[1][0], self.squaresV[2][0]], [self.squaresV[0][1], self.squaresV[1][1], self.squaresV[2][1]], [self.squaresV[0][2], self.squaresV[1][2], self.squaresV[2][2]]]
        else:
            self.squaresH[rowNum] = row
            self.squaresV = [[self.squaresV[0][0], self.squaresV[1][0], self.squaresV[2][0]], [self.squaresV[0][1], self.squaresV[1][1], self.squaresV[2][1]], [self.squaresV[0][2], self.squaresV[1][2], self.squaresV[2][2]]]