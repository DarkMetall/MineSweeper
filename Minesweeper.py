#Minesweeper
import random
import math

def GenerateSeed(bombs_number):
    bomb_coords=[]
    while len(bomb_coords)<bombs_number:
        rand_number = [random.randint(0,9),random.randint(0,9)]
        if rand_number not in bomb_coords:
            bomb_coords.append(rand_number)
            #print("Added:"+ str(rand_number))
        #else:
           # print("Not added:"+ str(rand_number))   
    return bomb_coords

def GenerateField(seed):
    field = [[0 for column in range(10)] for row in range(10)]
    for bomb in seed:
       field[bomb[0]][bomb[1]] = "bomb"
    for i in field:
        print(i)
    CalculateFieldCells(field)
   

def CalculateFieldCells(field):
    field_j_size = len(field[0])-1
    field_i_size = len(field)-1

    for i in range(field_i_size):
        for j in range(field_j_size):
            if(j!="bomb"):             
                check_cells_list =[]
                if(j>0):
                    if field[i][j-1]=="bomb":
                        check_cells_list.append(field[i][j-1])
                if(j<field_j_size):
                    if field[i][j+1]=="bomb":
                        check_cells_list.append(field[i][j+1])
                if(i>0):
                    if field[i-1][j]=="bomb":
                        check_cells_list.append(field[i-1][j])
                    if(j>0):
                         if field[i-1][j-1]=="bomb":
                            check_cells_list.append(field[i-1][j-1])
                    if(j<field_j_size):
                         if field[i-1][j+1]=="bomb":
                            check_cells_list.append(field[i-1][j+1])
                if(i<field_i_size):
                    if field[i+1][j]=="bomb":
                        check_cells_list.append(field[i+1][j])
                    if(j>0):
                         if field[i+1][j-1]=="bomb":
                            check_cells_list.append(field[i+1][j-1])
                    if(j<field_j_size):
                         if field[i+1][j+1]=="bomb":
                            check_cells_list.append(field[i+1][j+1])
                field[i][j]=len(check_cells_list)
         
    for i in field:
        print(i)
                
            


GenerateField(GenerateSeed(13))