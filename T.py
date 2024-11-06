# Hrishit Srivastava
# Aadityaa Rengaraj Sethuraman
from tkinter import *
from g import Grid
from T_base import Tetrominoes
import numpy as np
import time
     
class Tetris(Grid):
    '''In this we define under the __intit__, 4 main attributes. We also use boolean logics to check specific conditions'''
    def __init__(self, canv, nrow, ncol, scale, block=None):
        super().__init__(canv, nrow, ncol, scale)
        self.pauseit=False
        self.name = None
        self.block= block
        self.inplace=False
        self.game_over=False

        if self.inplace == True:
             Tetrominoes.delete()  
        
    
    def next(self):
         '''This function calls class Tetrominoes and implements it in the grid. This function also flushes
         the entire row if it is filled with colours.'''
         if self.block is  None:
              self.block= Tetrominoes.random_select(self.canvas, self.nrow, self.ncol, self.scale)
              self.block.activate()
         self.block.down()
         i,j =self.block.i,self.block.j
         if self.block.i+self.block.h >= self.nrow:
              self.inplace= True
         elif self.isoverlapping(i+1, j):
              self.inplace= True
         if self.inplace is True:
            pix= self.block.pixel_list
            self.block.delete()
            for pixel in pix:
                if pixel.color != 0:
                    self.addij(pixel.i, pixel.j, pixel.c)
                    for row in range(3):                            
                        for col in range(self.ncol): 
                            if self.matrix[row,col] != 0:
                                self.is_game_over()
                                self.game_over = True
                                self.canvas.create_text(self.canvas.winfo_width()//3,self.canvas.winfo_height()//3,text = "GAME OVER",fill = "white",font=('Helvetica', 40))
                                
                                

            for x in range(self.nrow): 
                flush = True
                for y in range(self.ncol):
                    if self.matrix[x, y] == 0:
                        flush = False
                if flush == True:
                    self.flush_row(x)
        

            self.block = None   #resetting block
            self.in_place = False

                               
    def isoverlapping(self, ii, jj):
        '''This function checks the overlapping conditions for the patterns.'''
        pattern = self.block.get_pattern()  # Get the pattern of the current block
        matrix = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]) 
        for x in range(3):  
            for y in range(3):
                matrix[x, y] = self.matrix[ii + x, jj+ y]
        for x in range(3):
            for y in range(3):
                if (matrix[x, y] != 0) and (pattern[x, y] != 0): #check if the block pattern is overlapping with any matrix cells
                    return True
        return False           
   
    def up(self):
        '''this functions rotates the block'''
        if self.block is None:
              self.block.rotate()
    
    def down(self):
        '''This function makes th eblock move downward'''
        while(self.block != None):
            self.next()
    
    def right(self):
        '''This function moves the block rightward'''
        if self.block is None:
              self.block.right()

    def left(self):
        '''this function moves the block leftward'''
        if self.block is None:
              self.block.left()


    def is_game_over(self):
        '''This function checks the condition for game over '''
        return self.game_over
        
    def pause(self): 
        '''This function is used to pause and resume the game'''                              #Pause and game over functions
        self.pauseit = not self.pauseit
        self.is_pause()

    def is_pause(self):
        '''This function is used to pause and resume the game'''  
        return self.pauseit
    
                   

#########################################################
############# Main code #################################
#########################################################
    

    
def main():
    ##### create a window, canvas 
        root = Tk() # instantiate a tkinter window
        game=Tetris(root,36,12,25) 
        
        ####### Tkinter binding mouse actions
        root.bind("<Up>",lambda e:game.up())
        root.bind("<Left>",lambda e:game.left())
        root.bind("<Right>",lambda e:game.right())
        root.bind("<Down>",lambda e:game.down())
        root.bind("<p>",lambda e:game.pause())        

        while True:
            #if not game.is_pause():
            game.next()
            root.update()   # update the graphic
            time.sleep(0.25)  # wait few second (simulation)
            if game.is_game_over(): break
        
        root.mainloop() # wait until the window is closed


        

if __name__=="__main__":
    main()