#Minesweeper
import random
import json
import math

BOMB_AMOUNT =13
BOMB = 9 #bomb sign
SIZE_I = 10
SIZE_J = 10

#discord emojis
EMPTY =  ":blue_square:"
ONE = ":one:"
TWO = ":two:"
THREE = ":three:"
FOUR = ":four:"
FIVE = ":five:"
SIX = ":six:"
SEVEN = ":seven:"
EIGHT = ":eight:"
NINE = ":nine:"
ZERO = ":zero:"


##############\

#f = open('sample.json') 
#discord = json.load(f) 
#if not (discord):
   # discord =  {}
  #  discord["storage"]={}
 #   discord["storage"]["user"]={}
#    discord["storage"]["user"]["gameinfo"]={}
#####################



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


def PrintField(playerfield, realfield):
    show_field =[]
    for i in range(SIZE_I):
        for j in range(SIZE_J):
            if(player_field[i][j]):
                match real_field[i][j]:
                    case 0:
                        show_field[i][j]= ZERO
                    case 1:
                        show_field[i][j]= ONE
                    case 2:
                        show_field[i][j]= TWO
                    case 3:
                        show_field[i][j]= THREE
                    case 4:
                        show_field[i][j]= FOUR
                    case 5:
                        show_field[i][j]= FIVE
                    case 6:
                        show_field[i][j]= SIX
                    case 7:
                        show_field[i][j]= SEVEN
                    case 8:
                        show_field[i][j]= EIGHT
                    case 9:
                        show_field[i][j]= NINE
            else:
                show_field[i][j]=EMPTY
    for row in show_field:
        print(row)

def MakeTurn(i,j):
    minesweeper_info = GetMinesweeperInfo()
    real_field = CalculateFieldCells(GenerateField(GenerateSeed(BOMB_AMOUNT, minesweeper_info["size"][0],minesweeper_info["size"][1]),minesweeper_info["size"][0],minesweeper_info["size"][1]))
    if(minesweeper_info["playerfield"][i][j]==1):
        print("This field is already opened, try another one")
    else:
        if(real_field[i][j]==BOMB):
            minesweeper_info["playerfield"][i][j]=1
            status=False
            print("You lost!")
            PrintField(minesweeper_info["playerfield"], real_field)
            WriteMinesweeperInfo(status,0,0,0)
        else:
            if(real_field[i][j]==0):
                #If the field is empty, it should open more cells
                 minesweeper_info["playerfield"][i][j]=1
                 PrintField(minesweeper_info["playerfield"], real_field)
                 WriteMinesweeperInfo(minesweeper_info["status"],minesweeper_info["playerfield"],minesweeper_info["seed"],minesweeper_info["size"])
            else:
                #if the opened cell has number
                minesweeper_info["playerfield"][i][j]=1
                PrintField(minesweeper_info["playerfield"], real_field)
                WriteMinesweeperInfo(minesweeper_info["status"],minesweeper_info["playerfield"],minesweeper_info["seed"],minesweeper_info["size"])
    win_counter = 0
    for i in player_field:
        for j in player_field:
            if(["playerfield"][i][j]==1) and (real_field[i][j != BOMB]):
                win_counter+=1
            if(win_counter==(SIZE_I*SIZE_J)-BOMB_AMOUNT):
                print("You won the game!")
                PrintField(minesweeper_info["playerfield"], real_field)
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
        discord["storage"]["user"]["gameinfo"]= gameinfo
        #discord["storage"]["user"].update(gameinfo)

   # with open("sample.json", "w") as outfile: 
        #json.dump(discord, outfile)


def GetMinesweeperInfo():
       gameinfo = GetGameInfo()
       if(gameinfo):
        minesweeper_info = json.loads(gameinfo)["minesweeper"]
        #minesweeper_info = gameinfo["minesweeper"]
        return minesweeper_info
       else:
           return {}

#minesweeper_info: 0 - status (True or false); 1 - playerfield, 2 - seed, 3 -[i,j]

def WriteMinesweeperInfo(status, playerfield, seed, size):
     gameinfo = GetGameInfo()
     if(gameinfo):
        gameinfo["minesweeper"]["status"]= status
        gameinfo["minesweeper"]["playerfield"]=playerfield
        gameinfo["minesweeper"]["seed"]=seed
        gameinfo["minesweeper"][size] = size
     else:
          message = {
                    "minesweeper":
          {
                         
                        "status": status,
                         "playerfield": playerfield,
                         "seed": seed,
                         "size": size
          } 
          
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
    elif(len(args)==0):
        PrintField(minesweeper_info["playerfield"], CalculateFieldCells(GenerateField(minesweeper_info["seed"],SIZE_I,SIZE_J)))
    else:
        print("Eror: Wrong number of args")




## there  should be 3 variants:
# 1 - game is created
#2 - game is finished
#3 game is not created and not finished (2-3 are the same)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#print(GetMinesweeperInfo())
minesweeper_info = GetMinesweeperInfo()
if not(minesweeper_info) or (minesweeper_info["status"]==False):
    print("no info found")
    seed = GenerateSeed(BOMB_AMOUNT,SIZE_I,SIZE_J)
   # print(seed)
    real_field = CalculateFieldCells(GenerateField(seed,SIZE_I,SIZE_J))
    player_field = GenerateEmptyField(SIZE_I,SIZE_J)
    WriteMinesweeperInfo(True,player_field,seed,[SIZE_I,SIZE_J])
    #print(player_field)
    GetArgs()
elif(minesweeper_info["status"]==True):
    print("found info")
    GetArgs()


    #real_field = CalculateFieldCells(GenerateField(minesweeper_info["seed"],SIZE_I,SIZE_J))
    #player_field = minesweeper_info["playerfield"]
    #real_field = CalculateFieldCells(GenerateField(minesweeper_info["seed"], minesweeper_info["size"][0], minesweeper_info["size"][1]))
    
