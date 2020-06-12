# coder: bobby
# channel: Believer 01 
# date_coded: 10/06/2020 
# Selection Sort
# Time Complexity: O(n*log(n))
# 3 2 6 5 8 7 1 4

def swap(arr,i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
def selection_sort(arr,n):
    for i in range(0,n-1):
        min_value=arr[i]
        min_value_index=i
        for j in range(i+1,n):
            if arr[j]<min_value:
                min_value=arr[j]
                min_value_index=j
        swap(arr,i,min_value_index)
def print_array(message,arr,n):
    print(message,end=" : ")
    for i in range(0,n):
        print(arr[i],end=" ")
    print()
def main():
    arr=[3,2,6,5,8,7,1,4]
    n=len(arr)
    print_array('Before Sorting',arr,n)
    selection_sort(arr,n)
    print_array('After Sorting',arr,n)
main()
