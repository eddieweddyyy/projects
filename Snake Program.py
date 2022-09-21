import turtle, random

class Game:
    '''
    Purpose: 
        run the game created
    Instance variables: 
        self.player: call class Snake
        self.food: call class Food
    Methods: 
        __init__: creates instance variables and the game board which snake will travel around
        gameloop: when game-ending factor occurred, end game or loop the game so that game can be continued
    '''
    def __init__(self):
        #Setup 700x700 pixel window
        turtle.setup(700, 700)

        #Bottom left of screen is (-40, -40), top right is (640, 640)
        turtle.setworldcoordinates(-40, -40, 640, 640)
        cv = turtle.getcanvas()
        cv.adjustScrolls()

        #Ensure turtle is running as fast as possible
        turtle.hideturtle()
        turtle.delay(0)
        turtle.tracer(0, 0)
        turtle.speed(0)

        #Draw the board as a square from (0,0) to (600,600)
        for i in range(4):
            turtle.forward(600)
            turtle.left(90)
        
        self.player = Snake(315, 315, 'green')
        self.food = Food()
        self.gameloop()
        

        turtle.onkeypress(self.player.go_down, 'Down')
        turtle.onkeypress(self.player.go_right, 'Right')
        turtle.onkeypress(self.player.go_left, 'Left')
        turtle.onkeypress(self.player.go_up, 'Up')
        turtle.listen()
        turtle.mainloop()

    def gameloop(self):
        if self.player.end() == True:
            turtle.penup()
            turtle.setpos(300, 300)
            turtle.pendown()
            turtle.write('Game over', False, 'center', font=('Arial', 50, 'normal'))
        else:
            self.player.move(self.food)
            turtle.ontimer(self.gameloop, 200) 
        turtle.update()
        
# Game()

class Snake:
    '''
    Purpose: 
        creates snake shape with turtle that moves it based on key press.
    Instance variables: 
        self.x: x axis position
        self.y: y axis position
        self.color: color of the snake
        self.segments: list stores the square segement that make up the snake, initally set as empty list
        self.vx: velocity of the snake in x axis
        self.vy: velocity of the snake in y axis
    Methods: 
        __init__: creates instance variavles
        grow: make another square element right after the first element, haed, so that it can be as snake grew
        move: move the snake and use grow when it consumes food
        go_down: make the snake go down
        go_left: make the snake go left
        go_right: make the snake go right
        go_up: make the snake go up
        end: decide game-ending factors
    '''

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.segments = []

        self.grow()
        self.vx = 30
        self.vy = 0
        

    def grow(self):
        head = turtle.Turtle()
        head.speed(0)
        head.fillcolor(self.color)
        head.shape('square')
        head.shapesize(1.5, 1.5)
        head.penup()
        head.setpos(self.x, self.y)
        self.segments.append(head)
    
    def move(self, pellet):
        self.x += self.vx
        self.y += self.vy

        if self.x == pellet.x and self.y == pellet.y:
            self.grow()
            pellet.move()
        else:
            for i in range(len(self.segments[:-1])):
                xpos = self.segments[i + 1].xcor()
                ypos = self.segments[i + 1].ycor()
                self.segments[i].setpos(xpos, ypos)

            self.segments[-1].setpos(self.x, self.y)
        
    def go_down(self):
        self.vx = 0
        self.vy = -30
    
    def go_left(self):
        self.vx = -30
        self.vy = 0

    def go_right(self):
        self.vx = 30
        self.vy = 0

    def go_up(self):
        self.vx = 0
        self.vy = 30

    def end(self):
        for i in range(len(self.segments[:-1])):
            if self.segments[-1].xcor() == self.segments[i].xcor() and self.segments[-1].ycor() == self.segments[i].ycor():
                return True
        if self.segments[-1].xcor() > 600 or self.segments[-1].xcor() < 0 or self.segments[-1].ycor() > 600 or self.segments[-1].ycor() < 0:
            return True
        else:
            return False

# Game()
class Food(Snake):
    '''
    Purpose: 
        creates food shape on the game board
    Instance variables: 
        self.food: food shape
        self.x: x axis position of the food
        self.y: y axis position of the food
    Methods: 
        __init__: creates food on the game board
        move: remove and move the food if the previous food is consumed by the snake
    '''
    def __init__(self):
        self.food = turtle.Turtle()
        self.food.speed(0)
        self.food.fillcolor('red')
        self.food.shape('circle')
        self.food.penup()
        self.x = 15 + 30 * random.randint(0, 19)
        self.y = 15 + 30 * random.randint(0, 19)
        self.food.setpos(self.x, self.y)

    def move(self):
        self.x = 15 + 30 * random.randint(0, 19)
        self.y = 15 + 30 * random.randint(0, 19)
        self.food.setpos(self.x, self.y)
Game()