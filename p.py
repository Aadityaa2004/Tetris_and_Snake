# Hrishit Srivastava
# Aadityaa Rengaraj Sethuraman
from tkinter import *
import time
import random

class Pixel:
    color = ['black', 'white', 'yellow', 'red', 'blue','green', 'orange', 'purple', 'brown', 'cyan']

    # to complete

    def __init__(self,canvas,i,j,nrow,ncol,scale,c,vector=[0,0]):
        '''Under the __init__ fuction, we are defining 4 important attributes which are i(row), j(column),
        nrow(specic row),ncol(specific colum), c(colour of the pixel), vector(which is used to give direction 
        to the pixel.).We also create a rectangle using canvas.'''
        self.canvas = canvas
        self.i = i%nrow # i co-ordinate
        self.j = j%ncol # j co-ordinate
        self.nrows = nrow # nth row 
        self.ncols = ncol # nth column
        self.scale = scale #scale factor of the canvas dimentions
        self.color = self.color[c % len(self.color)] # accessing the colour array from above and implimenting it under Pixel class
        self.vector = vector #  direction vector for the pixel when it moves
        x0 = self.j*scale 
        y0 = self.i*scale
        x1 = (self.j+1)*scale
        y1 = (self.i+1)*scale
        self.rect = self.canvas.create_rectangle(x0,y0,x1,y1,fill=self.color,outline="black") # creating a rectangle pixel on the canvas.
        canvas.pack() # displays the rectangles

    def __str__(self):
        '''The __str__function is used to return all of the data regarding each row and column within the pixel.
        This function also helps us to identify the location of each pixel within the tkinker output. '''
        return f'({self.i%self.nrows},{self.j%self.ncols}) {self.color}' # returning str value for printing it   
    
    def next(self):
        '''This function is integrated with right,left,up,down functions. When the vector notations are passed, 
        the pixel moves in the specified direction according to the assigned value under this function. This program
        also ensures that if the pixel moves out of the nrows and ncolums, it must re-appear into the screen from the
        other direcrtion and thus the pixel doesnt continue to move infinitely.'''
        i = (self.i+self.vector[0]) % self.nrows # defining i value and associating it with the direction vector
        j = (self.j+self.vector[1]) % self.ncols # defining j value and associating it with the direction vector

        if i<0: # checks if pixel exits the row of the scaled canvas
            i = self.nrow-1 # making the pixel re-appear on the opposite side  
        if j<0: # checks if pixel exits the column of the scaled canvas
            j = self.ncols-1 # making the pixel re-appear on the opposite side
        self.canvas.move(self.rect,(j-self.j)*self.scale,(i-self.i)*self.scale) #moves the pixel
        self.i = i 
        self.j = j

        
    def right(self):
        '''This function defines the attribute self.vector, which assignes a specific value to 
        it, so that the pixel moves in that specific direction. In this case the object moves to the
        right side'''
        self.vector = [0, 1] # giving the direction vector 
      
    def left(self):
        '''This function defines the attribute self.vector, which assignes a specific value to 
        it, so that the pixel moves in that specific direction. In this case the object moves to the
        left side'''
        self.vector = [0, -1] # giving the direction vector
            
    def up(self):
        '''This function defines the attribute self.vector, which assignes a specific value to 
        it, so that the pixel moves in that specific direction. In this case the object moves upward'''
        self.vector = [-1, 0] # giving the direction vector
        
    def down(self):
        '''This function defines the attribute self.vector, which assignes a specific value to 
        it, so that the pixel moves in that specific direction In this case the object moves downward'''
        self.vector = [1, 0] # giving the direction vector

    def delete(self):
        '''This function deletes all of the pixels(data) which is executed in the program. This statement 
        is necessary to move between different test functions, so that they dont overlap each other.'''
        self.canvas.delete(self.rect) # deletes all the pixels 
        

#################################################################
# TESTING FUNCTION
#################################################################
def delete_all(canvas):
    canvas.delete("all")
    print("Delete All")


def test1(canvas, nrow, ncol, scale):
    print("Generate 10 points at random")
    random.seed(4)  # for reproducibility
    for k in range(10):
        i = random.randint(0, nrow-1)
        j = random.randint(0, ncol-1)
        c = random.randint(1, 9)    # color number
        pix = Pixel(canvas, i, j, nrow, ncol, scale, c)
        print(pix)


def test2(canvas, nrow, ncol, scale):
    print("Generate 10 points at random (using modulo)")
    random.seed(5)  # for reproducibility
    for k in range(10):
        i = random.randint(0, nrow-1)*34
        j = random.randint(0, ncol-1)*13
        ij = str(i)+","+str(j)
        c = random.randint(1, 9)    # color number
        pix = Pixel(canvas, i, j, nrow, ncol, scale, c)
        print(ij, "->", pix)


def test3(root, canvas, nrow, ncol, scale):
    print("Move one point along a square")

    pix = Pixel(canvas, 35, 35, nrow, ncol, scale, 3)
    pix.vector = [-1, 0]  # set up direction (up)
    for i in range(30):
        pix.next()       # next move in the simulation
        root.update()    # update the graphic
        time.sleep(0.05)  # wait in second (simulation)

    pix.vector = [0, -1]  # set up new direction (left)
    for i in range(30):
        pix.next()       # next move in the simulation
        root.update()    # update the graphic
        time.sleep(0.05)  # wait in second (simulation)

    pix.vector = [1, 0]   # set up new direction (down)
    for i in range(30):
        pix.next()       # next move in the simulation
        root.update()    # update the graphic
        time.sleep(0.05)  # wait in second (simulation)

    pix.vector = [0, 1]    # set up new direction (right)
    for i in range(30):
        pix.next()       # next move in the simulation
        root.update()    # update the graphic
        time.sleep(0.05)  # wait in second (simulation)

    # delete point
    pix.delete()


def test4(root, canvas, nrow, ncol, scale):
    print("Move four point along a square")

    pixs = []
    pixs.append(Pixel(canvas, 35, 35, nrow, ncol, scale, 3, [-1, 0]))
    pixs.append(Pixel(canvas, 5, 35, nrow, ncol, scale, 4, [0, -1]))
    pixs.append(Pixel(canvas, 5, 5, nrow, ncol, scale, 5, [1, 0]))
    pixs.append(Pixel(canvas, 35, 5, nrow, ncol, scale, 6, [0, 1]))

    print("Starting coords")
    for p in pixs:
        print(p)

    for i in range(30):
        for p in pixs:
            p.next()       # next move in the simulation
        root.update()      # update the graphic
        time.sleep(0.05)   # wait in second (simulation)

    print("Ending coords")
    for p in pixs:
        print(p)
        p.delete()


def test5(root, canvas, nrow, ncol, scale):
    print("Move one point any direction -use arrow commands")

    pix = Pixel(canvas, 20, 20, nrow, ncol, scale, 2)

    # binding used by test5
    root.bind("<Right>", lambda e: pix.right())
    root.bind("<Left>", lambda e: pix.left())
    root.bind("<Up>", lambda e: pix.up())
    root.bind("<Down>", lambda e: pix.down())

    # simulation
    while True:
        pix.next()
        root.update()     # update the graphic
        time.sleep(0.05)  # wait in second (simulation)


###################################################
#################### Main method ##################
###################################################


def main():

    # create a window, canvas
    root = Tk()  # instantiate a tkinter window
    nrow = 40
    ncol = 40
    scale = 20
    canvas = Canvas(root, width=ncol*scale, height=nrow*scale,
                    bg="black")  # create a canvas width*height
    canvas.pack()

    # general binding events to choose a testing function
    root.bind("1", lambda e: test1(canvas, nrow, ncol, scale))
    root.bind("2", lambda e: test2(canvas, nrow, ncol, scale))
    root.bind("3", lambda e: test3(root, canvas, nrow, ncol, scale))
    root.bind("4", lambda e: test4(root, canvas, nrow, ncol, scale))
    root.bind("5", lambda e: test5(root, canvas, nrow, ncol, scale))
    root.bind("<d>", lambda e: delete_all(canvas))

    root.mainloop()  # wait until the window is closed


if __name__ == "__main__":
    main()
