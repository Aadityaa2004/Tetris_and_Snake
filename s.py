# Hrishit Srivastava
# Aadityaa Rengaraj Sethuraman
from tkinter import *
from g import Grid
from p import Pixel
import time


### complete class Snake
class Snake(Grid):
    '''we define the __init__ function with 2 major attributes the are obstacles and fruits. We also
    superimpose the grid function to impliment the grid in the snake. '''
    def __init__(self, root, obstacles, fruits, vector=[0,1]):
        super().__init__(root, nrow=50, ncol=30, scale=20)
        self.obstacles = obstacles # number of obstacles
        self.fruits = fruits # number of fruits
        self.random_pixels(self.obstacles,1) # using Grid's function and generating random obstacles on the grid
        self.random_pixels(self.fruits-1,3) # using Grid's function and generating random fruits on the grid
        self.pixels=[] # creating an empty array
      
        self.gameover= False # Private attribute to indicate if the game is over
        self.pause= False # Private attribute to indicate if the game is paused 
        self.turn= False
        for x in range(3):
            self.pixels += [Pixel(self.canvas, 25, 15+x, self.nrow, self.ncol, self.scale, 5, [0,1])]
        self.pixels += [Pixel(self.canvas, 25, 18, self.nrow, self.ncol, self.scale, 4, [0,1])]
        self.y= len(self.pixels)
        self.c=1
        self.head_pixel=self.pixels[-1]

    def is_game_over(self):
        '''This function is used to end the snake game '''
        return self.gameover

    def game_state(self, bool):
        '''this is used to return a boolean value to self.next(), where this function has been called.'''
        self.gameover = bool

    def pause_or_not(self):
        '''This function is passed on from the main program to pause and continue the game.'''
        return self.pause
    
    def is_pause(self):
        '''This function is passed on from the main program to pause and continue the game.'''
        self.pause = not self.pause

    def left(self):
        '''This function is used to move the snake towards left direction when key is pressed.'''
        self.head_pixel = self.pixels[-1] 
        if self.head_pixel.vector[1] == 0 and not self.turn:
            self.turn = True
            self.head_pixel.left()
            self.matrix[self.head_pixel.i][self.head_pixel.j] = -3
           

    def right(self):
        '''This function is used to move the snake towards right direction when key is pressed.'''
        self.head_pixel = self.pixels[-1] 
        if self.head_pixel.vector[1] == 0 and not self.turn:
         self.head_pixel.right()
         self.turn = True
         
         self.matrix[self.head_pixel.i][self.head_pixel.j] = -1

    def down(self):
        '''This function is used to move the snake towards downward direction when key is pressed.'''
        self.head_pixel = self.pixels[-1] #storing the head of the snake
        if self.head_pixel.vector[0] == 0 and not self.turn:
         self.turn = True
         self.head_pixel.down()
         self.matrix[self.head_pixel.i][self.head_pixel.j] = -4

    def up(self):
           '''This function is used to move the snake towards upward direction when key is pressed.'''
           self.head_pixel = self.pixels[-1] 
           if self.head_pixel.vector[0] == 0 and not self.turn:
            self.turn = True
            self.head_pixel.up()
            self.matrix[self.head_pixel.i][self.head_pixel.j] = -2  
           
    def next(self):
     for x in reversed(self.pixels):   # go through the snake pixels in reverse
       new_i, new_j = x.i, x.j
       matrix_value = self.matrix[new_i][new_j]

       if matrix_value == -1:  # if it is a right turn
        x.vector = [0, 1]
       elif matrix_value == -2:  # if it is an up turn
        x.vector = [-1, 0]
       elif matrix_value == -3:  # if it is a left turn
        x.vector = [0, -1]
       elif matrix_value == -4:  # if it is a down turn
        x.vector = [1, 0]

       if x == self.pixels[0]:  # if you are in the last iteration of the for loop
        self.matrix[new_i][new_j] = 0  # make that neg value 0 in the matrix 
       x.next()
       self.turn= False
    
     head_pixel = self.pixels[-1]
     if self.matrix[head_pixel.i][head_pixel.j] == 3:#check if it is the red fruit
        tail = self.pixels[0]
        dir = tail.vector#direction of the tail
        self.pixels=  [Pixel(self.canvas, tail.i - dir[0], tail.j - dir[1], self.nrow, self.ncol, self.scale, 5, dir)] + self.pixels
        self.delij(head_pixel.i, head_pixel.j, 3)#for the deletion of the fruit
        self.fruits -= 1
        self.next()
        
     if self.matrix[head_pixel.i][head_pixel.j] == 1:
        self.canvas.create_text(self.canvas.winfo_height()//3, self.canvas.winfo_width()//3, text="GAME OVER", fill="white", font=('Helvetica 40 bold'))
        print("GAME OVER")
        self.game_state(True)
     s = self.pixels
     for x in range(len(s)-1):
        if s[x].i == s[-1].i and s[x].j == s[-1].j:
            print("GAME OVER")
            self.canvas.create_text(self.canvas.winfo_height()//3, self.canvas.winfo_width()//3 , text="GAME OVER", fill="white", font=('Helvetica 40 bold'))
            self.game_state(True)
     if self.fruits == 0:
        print("YOU WIN!")
        self.canvas.create_text(self.canvas.winfo_height()//3, self.canvas.winfo_width()//3 , text="YOU WIN", fill="white", font=('Helvetica 40 bold'))
        self.game_state(True)
      
     
     
             

        
       



#########################################################
############# Main code #################################
#########################################################
    

  
def main(): 
        
        ##### create a window, canvas 
        root = Tk() # instantiate a tkinter window
        python = Snake(root,20,20) #20 obstacles, and 20 fruits
        #python = Snake(root,5,5,25,25,30) # 5 obstacles/fruits, 25 row, 25 column, 30 scale
        
        
        ####### Tkinter binding mouse actions
        root.bind("<Right>",lambda e:python.right())
        root.bind("<Left>",lambda e:python.left())
        root.bind("<Up>",lambda e:python.up())
        root.bind("<Down>",lambda e:python.down())
        root.bind("<p>",lambda e:python.pause())
       
        while True:
            if not python.is_pause(): python.next()
            root.update()
            time.sleep(0.15)  # wait few second (simulation)
            if python.is_game_over(): break
            
        
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

