# Minesweeper Game

import random
import os

# minesweeper code

def mapgen(dim,mines):
  mineloc = [] # sets blank value for all mine locations

  for x in range(mines): # iterates to make all of the mines
    x = random.randrange(1,dim+1) # gets x value for a mine
    y = random.randrange(1,dim+1) # gets y value for a mine
    mineloc0 = [x,y,'X','[ ]'] # sets x and y value to the mine
    if mineloc0 in mineloc: # checks for duplicate coordinates
      x -= 1 # restarts the iteration of duplicate is found
    else:
      mineloc.append(mineloc0) # adds coordinate to list of mine

  for xrand in range(1,dim+1): # iterates all x coords
    for yrand in range(1,dim+1): # iterates all y coords
      add = True # assumes position is available
      cnt = 0 # number of mines the square is touching
      if [xrand,yrand,"X",'[ ]'] in mineloc:
        add = False
      if [xrand-1,yrand-1,"X",'[ ]'] in mineloc:
        cnt += 1
      if [xrand,yrand-1,"X",'[ ]'] in mineloc:
        cnt += 1
      if [xrand+1,yrand-1,"X",'[ ]'] in mineloc:
        cnt += 1
      if [xrand-1,yrand,"X",'[ ]'] in mineloc:
        cnt += 1
      if [xrand+1,yrand,"X",'[ ]'] in mineloc:
        cnt += 1
      if [xrand-1,yrand+1,"X",'[ ]'] in mineloc:
        cnt += 1
      if [xrand,yrand+1,"X",'[ ]'] in mineloc:
        cnt += 1
      if [xrand+1,yrand+1,"X",'[ ]'] in mineloc:
        cnt += 1
      if add: # checks if available
        mineloc.append([xrand,yrand,str(cnt),'[ ]']) # adds non-mine spot

  mineloc.sort() # sorts all positions
  return mineloc # returns the mine locations

def expose(listname,indexpos,act):
  if act == "c":
    new = str(listname[indexpos][2])
  elif act == "f":
    new = act.upper()
  elif act == "u":
    new = ' '
  listname[indexpos][-1] = "[" + new + "]"

def minesweeper(dim,mines): # starts the game
  allLoc = mapgen(dim,mines)
  board.write(str(allLoc))
  run = True # runs the code
  turn = 0 # turn number
  action = True # sets action

  while run: # while game is running
    txt = ""
    screen = "" # sets variable for screen
    if action != False: # checks if the last turn was an error
      turn += 1 # turn count goes up
    print('\nMines left: {0}{1}Turn {2}'.format(mines,5*" ",turn)) # prints status of the game
    txt = txt + "Turn: " + str(turn) + "\n" + "Mines: " + str(mines) + "\n"
    for x in allLoc: # makes loop to append the hidden values for every location
      if int(x[1]) == 1: # if at a new row, create new row
        screen += "\n {:3s} ".format(str(x[0])) # creates the new row
      screen += str(x[-1]) # adds locations value to screen

    numX = " "*5 # makes number labels
    for x in range(1,dim+1): # makes number labels
      numX = numX + "{:3s}".format(str(x)) # makes number labels

    print(numX + screen) # prints out the screen
    inputtxt = "\nWhat would you like to do? \n\n"+3*dim*"-"+"\n\n(f)lag | (c)heck | (u)nflag\n\n> " # the text that is printed for you to enter action

    userInputAction = input(inputtxt).lower() # gets user input for action

    txt = txt + "User Action Input: " + userInputAction + "\n"

    if userInputAction == "f": # if action is flag
      action = "flag" # sets action to flag
    elif userInputAction == "c": # if action is check
      action = "check" # sets action to check
    elif userInputAction == "d": # if action is debug
      action = "debug" # sets action to debug
    elif userInputAction == "u": # if action is unflag
      action = "unflag" # sets action to unflag
    else: # if something else is entered
      action = False # sets action to False
      print("Please enter f or c") # tells user to enter a normal action

    loctxt = ("Where would you like to " + str(action) + "? Enter two numbers 1-" + str(dim) + ", seperated by a comma.\n\n"+dim*"-"+"\n\n> ") # the text that is printed for you to enter location

    if action == "flag" or action == "check" or action == "unflag": # if they didn't do anything weird
      print('If you would like to go back, enter "cancel" to cancel.\n')
      userInputLocation = input(loctxt) # asks for user to input location for their action
      txt = txt + "Location of action: " + userInputLocation + "\n"
      if userInputLocation != "cancel": # if they are not cancelling
        userInputLocation = userInputLocation.split(",") # splits coordinates
        indexpos = int(userInputLocation[1]) * dim + int(userInputLocation[0]) - dim - 1 # calculates coordinates based on user input
        txt = txt + "Location Value: " + str(allLoc[indexpos][2]) + "\n"
        if action == "flag":
          mines -= 1
          expose(allLoc,indexpos,userInputAction)
        elif action == "check":
          if allLoc[indexpos][2] == "X":
            run = False
            txt = txt + "Game Result: Lose"
          else:
            expose(allLoc,indexpos,userInputAction)
        elif action == "unflag":
          if allLoc[indexpos][3] != "[F]":
            action = False
          else:
            mines += 1
            expose(allLoc,indexpos,userInputAction)
      else: # if they are cancelling
        action = False # cancel the action, doesn't advance turns
    elif action != "debug": # if they are debugging
      action = False # do not advance the turns
         
    if action == "debug": # checks if the action is debug
      for x in allLoc: # iterates all positions
        x[-1] = "[" + x[2] + "]" # reveals all positions
    txt = txt + "\n\n"
    if run != False:
      log.write(txt)

# start
startuser = input("Would you like to play Minesweeper? (y/n)\n> ").lower() # self explanatory?
if startuser == "n": # if they dont want to play :(
  print("Goodbye!")
elif startuser == "y": # start game
    minesweepersettings = input("\nChoose your difficulty: \n\n(e)asy\n(m)edium\n(h)ard\n\n> ").lower() # asks user for preferred difficulty
    if minesweepersettings == "e": # easy settings
      dimensions = 10
      mines = 10
      run = True
    elif minesweepersettings == "m": # medium settings
      dimensions = 13
      mines = 50
      run = True
    elif minesweepersettings == "h": # hard settings
      dimensions = 24
      mines = 100
      run = True
    else:
      print("Error. Restart program and learn to type smh")
      run = False
    
    log = open('gamelog.txt','w')
    log.close()
    log = open('gamelog.txt','a')
    board = open('gameboard.txt','w')
    board.close()
    board = open('gameboard.txt','a')

    if run:
      minesweeper(dimensions,mines) # game function

board.close()
log.close()