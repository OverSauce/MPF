
#################################################################################################################
##################################################  DEFINITIONS  ################################################
#################################################################################################################


import numpy as np                                                                 



################  readtxt is pretty strightforward, takes number sequences from text files and  #################
################  turns them into a useful python array to work with. Input must be txt         #################
################  Sequence in the file must have order like: '1 2 4 5 8 6', no commas           #################   

def readtxt(filename):                                  
    sqn = []
    
    with open(filename, "r") as infile:
        
        for line in infile:
            line = line.replace("\n", "")
            sqn.extend(line.split(" "))
    
    return sqn



################  Only job of the primeFinder is to find if given integer is a prime or not  ####################  


def primeFinder(n):
    
    if n <= 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False

    halfway_n = int(np.floor(np.sqrt(n)))

    for i in range(3, halfway_n + 1, 2):
        
        if n % i == 0:
            return False

    return True


########################  tobinaryv is to turn decimals into binaries, but with a twist   ########################
########################  that dimension(s) of the square matrix must be known.           ########################



def tobinaryv(num,dimension):                            
    
    toReturn=[]
    
    while num >= 1:
        toReturn.append(num%2)
        num = num // 2
    
    toReturn.reverse()
    
    return [0]*(dimension - len(toReturn)) + toReturn



###################  sqn2Matrix takes numbers from an 1d array an places them into lower half  ################### 
###################  of a lower triangular matrix. Other important job of this function is to  ###################
###################  add -1000000 to every prime number.                                       ###################


def sqn2Matrix(sequence):
    
    dimension = 0
    total = 0
    
    while total != len(sequence):
        dimension += 1
        total += dimension
    
    lowTriMatrix = np.tri(dimension, dimension, 0)
    i = 0
    
    for row in range(0, dimension, 1):
        
        for column in range(0, dimension, 1):
            
            if lowTriMatrix[row][column] == 1:
                
                if primeFinder(int(sequence[i]))==False:
                    lowTriMatrix[row][column] = int(sequence[i])
                
                else:
                    lowTriMatrix[row][column] = -1000000
                
                if i < len(sequence) - 1:
                    i += 1
    
    return  lowTriMatrix.astype(int)



##############  pathFinder  is to find the path with highest sum, it uses tobinaryv to calculate   ##############
##############  paths of walking. Previously it was running on random paths, and it took a lot of  ##############
##############  time to find the highest sum every attempt.                                        ##############


def pathFinder(matrix):
    
    dimension = len(matrix)
    possible_paths = []
    
    for _ in range(2**(dimension - 1)):
        choices = tobinaryv(_, dimension - 1)
        temp = []
        temp.append(matrix[0][0])
        
        col = 0
        
        for row in range(len(choices)):
            col += choices[row]
            number = int(matrix[row + 1][col])
            
            if number > 1:
                temp.append(number)
            
            else:
                break
        
        if len(temp) == dimension:
            possible_paths.append(sum(temp))
    
    return  (max(possible_paths))


#################################################################################################################
############################################ END OF THE DEFINITIONS #############################################
#################################################################################################################




import time                   # time has time() function, I used to calculate the runtime,   
                              # my previous attempts of this program had significantly higher runtime

t0 = time.time()

S = readtxt("data.txt")            # Pyramid from text file "data.txt"
S = sqn2Matrix(S)                  # Transforming 1d array of numbers to a pyramid like shape,
                                   # which is a lower triangular matrix

SUM = pathFinder(S)                                                  
t1 = time.time()                  

print("\nTime: ", t1 - t0, "seconds\n")
print("GREATEST SUM:", SUM)


