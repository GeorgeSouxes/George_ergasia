def prime_number(x):   
    for i in range(2, x): #��� i ��� 2 ����� (x-1)
        if (x % i  == 0):
                return False
    return True
#� ��������� ���� ������� �� ������ ���� ������ ��� ������� ��� �����
#������ � ���, ������������� True � False ����������.
          
def main():
    flag=False
    for j in range(a,(b+1-d)):
        if (prime_number(j)):   #������ ��� � ������� i ����� ������ �������
            if (prime_number(j+d)):  #������ ��� ��� � ������� i+d = � �������
                # ��� ������ d ��� ��� i ����� ������
                flag = True
                break
            
    if flag==True:
        print('The numbers have been found and they are: ',(j,(j+d)))
    else:
        print("No numbers found")
                    
a,b = [int(x) for x in input("Parakalw dwste to diasthma [a,b]: ")]
d=int(input("parakalw dwste ton akeraio d pou exei diafora=|p-q|: "))
main()
