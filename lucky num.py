input_number=int(input("enter a number to find your lucky digit"))
print(f'number you input is {input_number}')
s=0
while input_number!=0:
    r=input_number%10
    input_number=input_number//10
    s+=r
    if s>9 and input_number==0:
        input_number = s
        s=0
print('your lucky number is:',s)