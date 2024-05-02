def greedy_selection_sort(arr):
    n=len(arr)

    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    
input_str=input("Enter Numbers separated by space:")
input_list=list(map(int,input_str.split()))
print("Input Array",input_list)
greedy_selection_sort(input_list)
print("Sorted Array",input_list)

