a = 0
b = 0
while True:
    try:
        x = int(input("Введите год: "))
        if int(x)>0:
            break
        else:
            print("Ошибка.")
            continue
    except ValueError:
        continue
a = x % 100
if int(a) == 0:
       
    a = x % 400
          
    if int(a) == 0:
        print("Високосный год.")
        b = x//100+1
        print(str(b) + " век.") 
    else:
        print("Невисокосный год.")
        b = x//100+1
        print(str(b) + " век.") 
       
else:
        
    a = x % 4
            
    if int(a)==0:
        print("Високосный год.")
        b = x//100+1
        print(str(b) + " век.") 
    else:
        print("Невисокосный год.")
        b = x//100+1
        print(str(b) + " век.")  

