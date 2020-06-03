# coder: bobby2510
# channel: Believer 01 
# date_coded: 03/06/2020 
# Quick sort
# Time Complexity: O(n*log(n))
# 2 1 3 9 4 7 5 8 6

def swap(arr,i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp

def get_pivot_index(arr,start,end):
    pivot=arr[end]
    j=start
    for i in range(start,end):
        if arr[i]<pivot:
            swap(arr,i,j)
            j+=1
    swap(arr,j,end)
    return j
def quick_sort(arr,start,end):
    if end-start>0:
        pivot_index=get_pivot_index(arr,start,end)
        quick_sort(arr,start,pivot_index-1)
        quick_sort(arr,pivot_index+1,end)

def print_array(message,arr,n):
    print(message,end=" : ")
    for i in range(0,n):
        print(arr[i],end=' ')
    print()

#starting
def main():
    arr=[2,1,3,9,4,7,5,8,6]
    n=len(arr)
    print_array('Before Sorting',arr,n)
    quick_sort(arr,0,n-1)
    print_array('After Sorting',arr,n)
main()
