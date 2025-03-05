#Print all the numbers between the two numbers.
x = int(input("input number: "))
y = int(input("input another: "))
  
if x>y:
    x = y
    y = x
    
print(f'{x}')
for i in range(x + 1, y):
    print(i)
print(y)
           
        
        
        
            
        

