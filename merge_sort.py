def divide_array(numbers,low,high):
    if low<high:
        mid = (low+high)//2
        divide_array(numbers, low, mid-1)
        divide_array(numbers, mid+1,high=1)
