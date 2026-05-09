import bubble_sort as bs

elements=[]
n=int(input('enter the no of elements:'))
print(f'enter {n} unsorted elements:')
for i in range(n):
    element=float(input())
    elements.append(element)

bs.bubble_sort(elements,n)
bs.bubble_sort_optimised(elements,n)