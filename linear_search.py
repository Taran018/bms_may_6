def linear_search(elements,search_ele):
    for i in range(len(elements)):
        if elements[i]==search_ele:
            return i
    return -1
elements=[]
n=int(input('enter the no of elements:'))
print(f'enter {n} elements:')
for i in range(n):
    element=float(input())
    elements.append(element)
search_ele=float(input('enter the element to be searched:'))

a=linear_search(elements,search_ele)
if a==-1:
    print(f'{search_ele} is not present')
else:
    print(f'{search_ele} found at {a+1}')