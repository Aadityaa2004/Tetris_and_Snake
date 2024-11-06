# Hrishit Srivastava
# Aadityaa Rengaraj Sethuraman
from tkinter import *
from p import Pixel
import random
import time
import numpy as np


class Grid:
    # To complete

    def __init__(self, root, nrow, ncol, scale):
        '''The __init__ here defines some of the main attributes nrow, ncol and scale.
        we also define self.matrix which is set to all zeros. This self.matrix helps us to identify
        every box in the grid. This is very helpful in the later part of the code to derive the colour
        of the cell and match it with the colour in the pixel. In the constructor, we also write a program 
        to draw the grid'''
        self.nrow = nrow # nth row
        self.ncol = ncol # nth column
        self.scale = scale # scale factor of the grid
        self.matrix = np.zeros((nrow, ncol),dtype=int) # sets all the values to zeros
        self.canvas = Canvas(root,width=ncol*scale,height=nrow*scale,bg="Gray")
        self.canvas.pack() 
        self.grid = []
        for row in range(nrow):
            for col in range(ncol):
                self.canvas.create_rectangle(col * scale,row * scale,(col * scale)+scale,(row * scale)+scale, fill="black", outline='white') #draws the grid


    def random_pixels(self,n,c):
        '''This function is used to generate random i(row) and j(column) values on the grid. This function 
        later calls self.addij which adds a white pixel to the grid at the specified matrix value.'''
        for k in range(n):
            while True:
                i,j = np.random.randint(0, self.nrow),np.random.randint(0, self.ncol) #generates random row and column values on the grid
                for pix in self.grid:
                    if pix.i == i and pix.j == j:
                        break
                else:
                    self.addij(i,j,c) # adds a white matrix to the random generated cells
                    break 

    def addij(self,i,j,c):
        '''This function has two conditions. This is also being caled in snake.py to add obstacles and fruits into
        the grid. The first condition checks if that the colour number is greater than zero. If it is, then adds that specific colour to 
        the grid. The second one checks of the colour value is 1, which refers to black and later adds black pixel into the grid. '''
        if c>0:
            pix = Pixel(self.canvas,i,j,self.nrow,self.ncol,self.scale,c) # calling Pixel class
            self.grid.append(pix) # addding the pixel to the grid
            self.matrix[i,j] = c # addding the specific colour to the grid

        elif c==0:
            pix = Pixel(self.canvas,i,j,self.nrow,self.ncol,self.scale,c) # calling Pixel class
            self.grid.append(pix) # adding black to the grid
            self.matrix[i,j] = c # addding black colour to the grid
            
    def addxy(self,x,y):
        '''This function is called in the main program. This integrates and is used to add a white pixel into the grid
        with the i and j values. This function is also used to print i , j , x and y values as output. '''
        i,j = y // self.scale,x // self.scale # getting the exact value of each pixel cell
        self.addij(i,j,1) # adding a white pixel to the grid
        print("insert %s %s %s %s 0"%(x,y,j,i)) # printing the specified values
        

    def delxy(self,x,y):
        '''This function is called in the main program. This integrates and is used to remove a white pixel from the grid
        with the i and j values. This function is also used to print i , j , x and y values as output with two conditions
        stating that 1) if the cell clicked is white, then it removes the white pixel and 2) if clicked on the black square,
        then it flushes out an entire row. '''
        i,j = y // self.scale,x // self.scale # getting the exact value of each pixel cell
        c = self.matrix[i,j] # identifying the colour of each pixel
        if (0 <= i <= self.nrow) and (0 <= j <= self.ncol):
            if c!=0:
                self.matrix[i,j]=0
                self.delij(i,j,1) # deleting the white pixel in the grid
                print("delete %s %s %s %s 1"%(x,y,j,i)) # printing the specified values
            else:
                self.delij(i,j,0) # deleting the complete row 
                print("delete %s %s %s %s 0"%(x,y,j,i)) # printing the specified values

    def delij(self,i,j,c):
        '''This function checks the condition passed through self.delxy. It matches the colour to self.matrix.
        If the colour clicked is black(0), then it executes self.flushrow() and otherwise it just sets a black square 
        value to the grid which makes the white square black.'''
        if c == 0:
            self.flush_row(i) # calling flush row to delete the complete row
        else:
            self.addij(i,j,0)
            self.matrix[i, j] = 0 # setting all the values in the cell to black
            self.reset() # calling reset() to redraw the grid
    
    def reset(self):
        '''This function is used to delete all the pixels in the grid.It also runs a for loop condition to redraw all the 
        remaining white squares in the grid'''
        for i in self.grid:
            i.delete() # deleting all the pixels in the grid
        d = self.nrow
        t = self.ncol
        for i in range(d):
            for j in range(t):
                c = self.matrix[i, j]
                if c != 0:
                    self.addij(i, j, c) # redrawing of the grid with random generated values

    def flush_row(self, row):
      '''This function deletes all the function in a row when a black square is clicked. It also contain an animation 
      for tetris which consists of two purple shapes colliding and deleting the row. '''
      if row < 50:  # checks that the click is on the canvas
        pixels = [Pixel(self.canvas, row, 0, self.nrow, self.ncol, self.scale, 7, [0, 1]),
            Pixel(self.canvas, row, 1, self.nrow, self.ncol, self.scale, 7, [0, 1]),
            Pixel(self.canvas, row, 2, self.nrow, self.ncol, self.scale, 7, [0, 1]),
            Pixel(self.canvas, row, self.ncol - 1, self.nrow, self.ncol, self.scale, 7, [0, -1]),
            Pixel(self.canvas, row, self.ncol - 2, self.nrow, self.ncol, self.scale, 7, [0, -1]),
            Pixel(self.canvas, row, self.ncol - 3, self.nrow, self.ncol, self.scale, 7, [0, -1])]  # list of pixels created, 3 on the left and 3 on the right of the row right-clicked
        
        
        
        for x in range(12):
            for p in pixels:
                p.next()  # move the pixel by the step distance
            self.canvas.update()  # update the graphic
            time.sleep(0.02)  # wait for the specified duration
            
        for p in pixels:
            p.delete()  # deletes the pixels from the array

        self.matrix[1:row + 1, :] = self.matrix[0:row, :]  # re-assigns all the pixels to 1 row higher
        self.matrix[0, :] = 0  # makes sure that the top row is always empty
        self.reset()
#########################################################
############# Main code #################################
#########################################################


def main():

    # create a window, canvas
    root = Tk()                # instantiate a tkinter window
    mesh = Grid(root, 50, 30, 20)  # instantiate a Grid object
    mesh.random_pixels(25, 1)  # generate 25 random (white) pixels in the Grid

    # Tkinter binding mouse actions
    root.bind("<Button-1>", lambda e: mesh.addxy(e.x, e.y))
    root.bind("<Button-3>", lambda e: mesh.delxy(e.x, e.y))

    root.mainloop()  # wait until the window is closed


if __name__ == "__main__":
    main()
