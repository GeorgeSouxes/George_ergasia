def prime_number(x):   
    for i in range(2, x): #για i από 2 μέχρι (x-1)
        if (x % i  == 0):
                return False
    return True
#Η συνάρτηση αυτή δέχεται ως όρισμα έναν αριθμό και ελέγχει εάν είναι
#πρώτος ή όχι, επιστρέφοντας True ή False αντίστοιχα.
          
def main():
    flag=False
    for j in range(a,(b+1-d)):
        if (prime_number(j)):   #δηλαδή εάν ο αριθμός i είναι πρώτος αριθμός
            if (prime_number(j+d)):  #δηλαδή εάν και ο αριθμός i+d = ο αριθμός
                # που απέχει d από τον i είναι πρώτος
                flag = True
                break
            
    if flag==True:
        print('The numbers have been found and they are: ',(j,(j+d)))
    else:
        print("No numbers found")
                    
a,b = [int(x) for x in input("Parakalw dwste to diasthma [a,b]: ")]
d=int(input("parakalw dwste ton akeraio d pou exei diafora=|p-q|: "))
main()
