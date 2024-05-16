#Minesweeper
import random
import json
import math

BOMB_AMOUNT =13
BOMB = 9 #bomb sign
SIZE_I = 10
SIZE_J = 10

def GenerateSeed(bombs_number,i,j):
    bomb_coords=[]
    while len(bomb_coords)<=bombs_number:
        rand_number = [random.randint(0,i-1),random.randint(0,j-1)]
        if rand_number not in bomb_coords:
            bomb_coords.append(rand_number)
            #print("Added:"+ str(rand_number))
        #else:
           # print("Not added:"+ str(rand_number))   
    return bomb_coords

def GenerateEmptyField(i,j):
    field = [[0 for column in range(i)] for row in range(j)]
    return field

def GenerateField(seed,i,j):
    field = GenerateEmptyField(i,j)
    for bomb in seed:
       field[bomb[0]][bomb[1]] = BOMB
    #for i in field:
     #   print(i)
    return field

   

def CalculateFieldCells(field):
    field_j_size = len(field[0])-1
    field_i_size = len(field)-1
    for i in range(field_i_size+1):
        for j in range(field_j_size+1):
            if(field[i][j]!=BOMB):             
                check_cells_list =[]
                if(j>0):
                    if field[i][j-1]==BOMB:
                        check_cells_list.append(field[i][j-1])
                if(j<field_j_size):
                    if field[i][j+1]==BOMB:
                        check_cells_list.append(field[i][j+1])
                if(i>0):
                    if field[i-1][j]==BOMB:
                        check_cells_list.append(field[i-1][j])
                    if(j>0):
                         if field[i-1][j-1]==BOMB:
                            check_cells_list.append(field[i-1][j-1])
                    if(j<field_j_size):
                         if field[i-1][j+1]==BOMB:
                            check_cells_list.append(field[i-1][j+1])
                if(i<field_i_size):
                    if field[i+1][j]==BOMB:
                        check_cells_list.append(field[i+1][j])
                    if(j>0):
                         if field[i+1][j-1]==BOMB:
                            check_cells_list.append(field[i+1][j-1])
                    if(j<field_j_size):
                         if field[i+1][j+1]==BOMB:
                            check_cells_list.append(field[i+1][j+1])
                field[i][j]=len(check_cells_list)
         
   # for i in field:
     #   print(i)
    return field              

def MakeTurn(i,j):
    minesweeper_info = GetMinesweeperInfo()
    real_field = CalculateFieldCells(GenerateField(GenerateSeed(BOMB_AMOUNT, minesweeper_info["size"][0],minesweeper_info["size"][1]),minesweeper_info["size"][0],minesweeper_info["size"][1]))
    if(minesweeper_info["playerfield"][i][j]==1):
        print("This field is already opened, try another one")
    else:
        if(real_field[i][j]==BOMB):
            status=False
            print("You lost!")
            WriteMinesweeperInfo(status,0,0,0)
        else:
            if(real_field[i][j]==0):
                #If the field is empty, it should open more cells
                NotImplemented
            else:
                #if the opened cell has number
                minesweeper_info["playerfield"][i][j]=1
                WriteMinesweeperInfo(minesweeper_info["status"],minesweeper_info["playerfield"],minesweeper_info["seed"],minesweeper_info["size"])
    win_counter = 0
    for i in player_field:
        for j in player_field:
            if(["playerfield"][i][j]==1) and (real_field[i][j != BOMB]):
                win_counter+=1
            if(win_counter==(SIZE_I*SIZE_J)-BOMB_AMOUNT):
                print("You won the game!")
                status=False
                WriteMinesweeperInfo(status,0,0,0)


def GetGameInfo():
    if ("gameinfo" in discord["storage"]["user"]):
        return discord["storage"]["user"]["gameinfo"]
    else:
        return {}
 
def SetGameInfo(gameinfo):
    if ("gameinfo" in discord["storage"]["user"]):
        discord["storage"]["user"]["gameinfo"]= gameinfo
    else:
        discord["storage"]["user"].update(gameinfo)

def GetMinesweeperInfo():
       gameinfo = GetGameInfo()
       if(gameinfo):
        minesweeper_info = gameinfo["minesweeper"]
        return minesweeper_info
       else:
           return {}

#minesweeper_info: 0 - status (True or false); 1 - playerfield, 2 - seed, 3 -[i,j]

def WriteMinesweeperInfo(status, playerfield, seed, size):
     gameinfo = GetGameInfo()
     print(gameinfo)
     if(gameinfo):
        gameinfo["minesweeper"]["status"]= status
        gameinfo["minesweeper"]["playerfield"]=playerfield
        gameinfo["minesweeper"]["seed"]=seed
        gameinfo["minesweeper"][size] = size
     else:
          message = {
                    "minesweeper":
          [
                         {
                        "status": status,
                         "playerfield": playerfield,
                         "seed": seed,
                         "size": size
                         }
          ]
          }
          SetGameInfo(message)
         

     #message[0]=status
     #message[1]=playerfield
     #message[2] = seed
     #message[3] = i_j
def GetArgs():
    args="{args}".split()
    if(len(args)==2):
        if(args[0]>=0) and (args[0]<=SIZE_I) and \
        (args[1]>=0) and (args[1]<=SIZE_J):
            MakeTurn(args[0],args[1])
        else:
            print("The parameters go out of range")
    else:
        print("Eror: Wrong number of args")




## there  should be 3 variants:
# 1 - game is created
#2 - game is finished
#3 game is not created and not finished (2-3 are the same)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





minesweeper_info = GetMinesweeperInfo()
if not(minesweeper_info) or (minesweeper_info["status"]==False):
    print("no info found")
    seed = GenerateSeed(BOMB_AMOUNT,SIZE_I,SIZE_J)
   # print(seed)
    real_field = CalculateFieldCells(GenerateField(seed,SIZE_I,SIZE_J))
    player_field = GenerateEmptyField(SIZE_I,SIZE_J)
    WriteMinesweeperInfo(True,player_field,seed,[SIZE_I,SIZE_J])
    #print(player_field)
elif(minesweeper_info["status"]==True):
    print("found info")
    player_field = minesweeper_info["playerfield"]
    real_field = CalculateFieldCells(GenerateField(minesweeper_info["seed"], minesweeper_info["size"][0], minesweeper_info["size"][1]))

