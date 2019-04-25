from random import shuffle
size = 1
width = 9
height = width
cells = []
initialWalls = []
finalWalls = []

#Build a list of cells, and another list of walls based on the dimensions of the maze.
for x in range(width):
    for y in range(height):
        #Make one cell for each x,y combination. The coordinates are wrapped in a list intentionally.
        cells.append([(x,y)])
        #Edge walls are a special case, which we simply exclude.
        if x != width-1:
            initialWalls.append((x,y,'e'))

        if y != height-1:
            initialWalls.append((x,y,'n'))

#This function determines which set any given cell belongs to, returning the index of said set.
def pathOf(cell):
    for path in cells:
        if cell in path:
            return cells.index(path)
    print("Path lookup failed. This shouldn't happen.")

#This function will effectively perform a union of two different paths (sets).
def unify(path1, path2):
    for cell in cells[path2]:
        cells[path1].append(cell)
    del cells[path2]

#We need to pick walls in a random order. For simplicity, we'll just shuffle the list.
shuffle(initialWalls)
#Now we iterate through the randomized list of walls...
for wall in initialWalls:
    #Name the two cells that will be up for consideration...
    primeCell = (wall[0], wall[1])
    if wall[2] == 'e':
        neighborCell = (wall[0]+1, wall[1])
        
    elif wall[2] == 'n':
        neighborCell = (wall[0], wall[1]+1)

    #If they are part of the same path, keep the wall. Otherwise...
    if pathOf(primeCell) == pathOf(neighborCell):
        finalWalls.append(wall)
    #Discard the wall and combine the paths of the two cells.
    else:
        unify(pathOf(primeCell), pathOf(neighborCell))

#Turtle spaghetti, please ignore:
import turtle
turtle.setworldcoordinates(-size,-size,size*width-(size/2),size*height-(size/2))
pen = turtle.Turtle()
pen.pensize(5)
pen.ht()
turtle.tracer(4)
pen.up()
pen.goto(-size,-size)
pen.pd()
pen.fd(size*width)
pen.left(90)
pen.fd(size*width)
pen.left(90)
pen.fd(size*width)
pen.left(90)
pen.fd(size*width)

def line(x,y,dirc):
    x *= size
    y *= size
    pen.up()
    pen.goto(x,y)
    pen.pd()
    if dirc == 'n':
        pen.goto(x-size, y)
    else:
        pen.goto(x, y-size)
for wall in finalWalls:
    line(wall[0],wall[1],wall[2])
