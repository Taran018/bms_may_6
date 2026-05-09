import insertion_sort as IS
import sys

numbers=[]
for i in range(1,len(sys.argv)):
    numbers.append(float(sys.argv[i]))
print('number before soorting:\n',numbers)
print('number after soorting:\n',IS.insertion_sort(numbers))


