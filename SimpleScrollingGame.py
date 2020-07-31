# Project: Simple Scrolling Game
# Ashley Stojak

import turtle
import math
import random

screen = turtle.Screen()
t = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
t5 = turtle.Turtle()

# make game objects as Python dictionary objects
player = {"t": turtle.Turtle(), "x": -200, "y": -200, "radius": 30, "color": "blue"}

harm = {"t4": turtle.Turtle(), "x": -250, "y": random.randint(-200, 100), "radius": 40, "color": "red"}

benefit = {"t2": turtle.Turtle(), "x": -250, "y": random.randint(-200, 100), "radius": 25, "color": "green"}

# make dictionary for the game itself
game = {"lives": 3, "points gained": 1, "background color": "light grey", "width": 500, "height": 500}

# draw a circle
def draw_circle(t, x, y, pencolor, fillcolor, radius):
  t.penup()
  t.goto(x, y)
  t.pendown()
  t.pencolor(pencolor)
  t.fillcolor(fillcolor)
  t.begin_fill()
  t.circle(radius)
  t.end_fill()
  t.penup()

# define game_lives and points
game_lives = game["lives"]
points = 0

# function to display score and lives on screen
def score_and_lives_display():
  t3.penup()
  t3.sety(215)
  t3.setx(-230)
  t3.write("Lives: " + str(game_lives), True, align= "left", font=("Arial", 20, "bold"))
  t3.sety(185)
  t3.setx(-230)
  t3.write("Score: " + str(points), True, align= "left", font=("Arial", 20, "bold"))
  screen.update()

# function to display "Game Over" and score when game is over
def game_over_and_score_display():
  t4.penup()
  t4.sety(0)
  t4.write("Game Over", True, align= "center", font=("Cooper Black", 60, "bold"))
  t5.penup()
  t5.sety(-50)
  t5.write("Score: " + str(points), True, align= "center", font=("Cooper Black", 30, "bold"))
  screen.update()

# handle up merely changes the y variable
def handle_up():
  global player
  player["y"] += 30
  screen.update()

# handle down merely changes the y variable
def handle_down():
  global player
  player["y"] -= 30
  screen.update()

# function that detects collisions
# function returns true if the objects are touching, false otherwise
def objects_are_in_collision (player, game_piece):
  result = False
  dx = player["x"] - game_piece["x"]
  dy = (player["y"] + player["radius"]) - (game_piece["y"] + game_piece["radius"])
  distance = math.sqrt((dx * dx) + (dy * dy))
  if (distance <= (player["radius"] + game_piece["radius"])):
    game_piece["x"] = 250
    game_piece["y"] = random.randint(-200, 100)
    result = True

  return result

# main function that sets background size and color, runs animation, and calls to function that displays score and game lives
def main():

  # set screen size
  screen.setup(game["width"], game["height"], 0, 0)
  # set screen color
  screen.bgcolor(game["background color"])

  # turn off continuous updating
  screen.tracer(0) 

  # hide turtles
  player["t"].hideturtle();
  harm["t4"].hideturtle();
  benefit["t2"].hideturtle();
  t.hideturtle();
  t2.hideturtle();
  t3.hideturtle();
  t4.hideturtle();
  t5.hideturtle();

  # handle the up and down key events
  screen.onkey(handle_down, "Down")
  screen.onkey(handle_up, "Up")
  # listen for events
  screen.listen()

  # define game_lives and points in loop
  global game_lives
  global points 

  # call display scores and lives function
  score_and_lives_display()

  # continous loop to do animation
  while (game_lives > 0):
    # update scrolling character positions
    harm["x"] -= 8
    benefit["x"] -= 6

    # handle edge condition
    if harm["x"] < -250:
      harm["x"] = 250
      harm["y"] = random.randint(-200, 100)
    if benefit["x"] < -250:
      benefit["x"] = 250
      benefit["y"] = random.randint(-200, 100)

    # clear any prior drawing for the turtles
    player["t"].clear()         
    harm["t4"].clear()
    benefit["t2"].clear()
  
    # draw the characters (circles)
    draw_circle(player["t"], player["x"], player["y"], player["color"], player["color"], player["radius"])    
    draw_circle(harm["t4"], harm["x"], harm["y"], harm["color"], harm["color"], harm["radius"])     
    draw_circle(benefit["t2"], benefit["x"], benefit["y"], benefit["color"], benefit["color"], benefit["radius"])

    screen.update()

    # check and handle collision between player and harm
    if objects_are_in_collision(player, harm) == True:
      # reduce game lives when player hits harm character
      game_lives = game_lives - 1
      # show live count of score on screen
      t3.clear() 
      score_and_lives_display()
    # check and handle collision between player and benefit
    if objects_are_in_collision(player, benefit) == True:
      # gain points when players hits benefit character
      points = points + game["points gained"] 
      # show live count of game lives on screen
      t3.clear()
      score_and_lives_display()
 
    screen.update()   # repaint the screen
  
  #hide player, harm, and benefit when game is over
  player["t"].clear()         
  harm["t4"].clear()
  benefit["t2"].clear()
  game_over_and_score_display()

main()
