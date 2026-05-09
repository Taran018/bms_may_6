def bubble_sort(elements,n):
    for i in range(n-1):
    
        for j in range(n-1-i):
            if elements[j] > elements[j+1]:
                elements[j+1] , elements[j] = elements[j] , elements[j+1]
                
       
    print(elements)


def bubble_sort_optimised(elements,n):
    for i in range(n-1):
        sorted=True
        for j in range(n-1-i):
            if elements[j] > elements[j+1]:
                elements[j+1] , elements[j] = elements[j] , elements[j+1]
                sorted=False
        if sorted:
            break
    print(elements)

'''elements=[]
n=int(input('enter the no of elements:'))
print(f'enter {n} unsorted elements:')
for i in range(n):
    element=float(input())
    elements.append(element)

bubble_sort(elements,n)
bubble_sort_optimised(elements,n)'''
         
