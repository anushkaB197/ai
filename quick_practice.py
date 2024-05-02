def quick_sort(arr):
    if len (arr)<=1:
        return arr
    else:
        pivot=arr[0]
        less=[x for x in arr[1:] if x<=pivot]
        greater=[x for x in arr[1:] if x>pivot]
        return quick_sort(less)+[pivot]+quick_sort(greater)
    
# example:
my_list=[3,89,1,1,3,]
sorted_list=quick_sort(my_list)
print(sorted_list)