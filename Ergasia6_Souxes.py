import random

A=["X","X","X","X","X","X","X"]
B=["X","X","X","X","X","X","X"]
C=["X","X","X","X","X","X","X"]
D=["X","X","X","X","X","X","X"]
E=["X","X","X","X","X","X","X"]
F=["X","X","X","X","X","X","X"]
G=["X","X","X","X","X","X","X"]


print("", A, "\n ", B, "\n" , C, "\n" , D, "\n" , E, "\n" ,
      F, "\n" , G, "\n")
print("\n select row starting from top = 1 and column from left = 0")
number1 = random.randint(1,7)
number2 = random.randint(0,6)
bomb = "@"

row=9
column = 9
one = "1"
blank = "-"

while row != number1 or column != number2:
    print("", A, "\n" , B, "\n" , C, "\n" , D, "\n" , E, "\n" ,
      F, "\n" , G, "\n")
    print(number1 , "" , number2) 
    row = int(input("\nEnter row: "))
    column = int(input("\nEnter column: "))
    columnA = column + 1
    columnB = column - 1
    rowA = row + 1
    rowB = row - 1
    if rowA == number1 or column  == number2:
        if row ==1:
            del A[column]
            A.insert(column, one)
        if row ==2:
            del B[column]
            B.insert(column, one)     
        if row ==3:
            del C[column]
            C.insert(column, one)   
        if row ==4:
            del D[column]
            D.insert(column, one) 
        if row ==5:
            del E[column]
            E.insert(column, one)         
        if row ==6:
            del F[column]
            F.insert(column, one)  
        if row ==7:
            del G[column]
            G.insert(column, one)
    elif rowB == number1 and column  == number2:
        if row ==1:
            del A[column]
            A.insert(column, one)
        if row ==2:
            del B[column]
            B.insert(column, one)        
        if row ==3:
            del C[column]
            C.insert(column, one)   
        if row ==4:
            del D[column]
            D.insert(column, one) 
        if row ==5:
            del E[column]
            E.insert(column, one)         
        if row ==6:
            del F[column]
            F.insert(column, one)  
        if row ==7:
            del G[column]
            G.insert(column, one)       
    elif row == number1 and columA  == number2: 
        if row ==1:
            del A[column]
            A.insert(column, one)
        if row ==2:
            del B[column]
            B.insert(column, one)     
        if row ==3:
            del C[column]
            C.insert(column, one)   
        if row ==4:
            del D[column]
            D.insert(column, one) 
        if row ==5:
            del E[column]
            E.insert(column, one)         
        if row ==6:
            del F[column]
            F.insert(column, one)  
        if row ==7:
            del G[column]
            G.insert(column, one)
    elif row  == number1 and columB == number2:
        if row ==1:
            del A[column]
            A.insert(column, one)
        if row ==2:
            del B[column]
            B.insert(column, one)     
        if row ==3:
            del C[column]
            C.insert(column, one)   
        if row ==4:
            del D[column]
            D.insert(column, one) 
        if row ==5:
            del E[column]
            E.insert(column, one)         
        if row ==6:
            del F[column]
            F.insert(column, one)  
        if row ==7:
            del G[column]
            G.insert(column, one)        
    else:
        if row ==1:
            del A[column]
            A.insert(column, blank)
        if row ==2:
            del B[column]
            B.insert(column, blank)     
        if row ==3:
            del C[column]
            C.insert(column, blank)   
        if row ==4:
            del D[column]
            D.insert(column, blank) 
        if row ==5:
            del E[column]
            E.insert(column, blank)         
        if row ==6:
            del F[column]
            F.insert(column, blank)  
        if row ==7:
            del G[column]
            G.insert(column, blank) 



if row ==1:
    del A[column]
    A.insert(column, bomb)
if row ==2:
    del B[column]
    B.insert(column, bomb)     
if row ==3:
    del C[column]
    C.insert(column, bomb)   
if row ==4:
    del D[column]
    D.insert(column, bomb) 
if row ==5:
    del E[column]
    E.insert(column,bomb )         
if row ==6:
    del F[column]
    F.insert(column, bomb)  
if row ==7:
    del G[column]
    G.insert(column, bomb)
print("", A, "\n" , B, "\n" , C, "\n" , D, "\n" , E, "\n" ,
      F, "\n" , G, "\n")
print("GAME OVER!")

input("Press SPACE to quit")
