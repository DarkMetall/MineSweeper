#Minesweeper
import random
import json
import math

BOMB = 9 #bomb sign
SIZE_I =10
SIZE_J =10

def GenerateSeed(bombs_number,i,j):
    bomb_coords=[]
    while len(bomb_coords)<bombs_number:
        rand_number = [random.randint(0,i),random.randint(0,j)]
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
         
    for i in field:
        print(i)
    return field              

def MakeTurn(i,j):
     NotImplemented

def LoadMinesweeperInfo():
       gameinfo = discord["storage"]["user"]#["gameinfo"]
       print(gameinfo)
       #minesweeper_info = json.loads(gameinfo)["minesweeper"]
       #print(minesweeper_info)
       #return minesweeper_info

#minesweeper_info: 0 - status (True or false); 1 - playerfield, 2 - seed, 3 -[i,j]


def WriteMinesweeperInfo():#status, playerfield, seed, i_j):
     gameinfo = discord["storage"]["user"]["gameinfo"]
     message =  gameinfo["minesweeper"] 
     print(message)
     #message[0]=status
     #message[1]=playerfield
     #message[2] = seed
     #message[3] = i_j




## there  should be 3 variants:
# 1 - game is created
#2 - game is finished
#3 game is not created and not finished





real_field = CalculateFieldCells(GenerateField(GenerateSeed(13)))
player_field = GenerateEmptyField(10,10)


