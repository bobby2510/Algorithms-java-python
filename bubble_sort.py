# coder: bobby
# channel: Believer 01 
# date_coded: 10/06/2020 
# Bubble Sort
# Time Complexity: O(n*log(n))
# 4 8 1 7 5 2 6 3

def swap(arr,i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
def bubble_sort(arr,n):
    for i in range(0,n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                swap(arr,j,j+1)
def print_array(message,arr,n):
    print(message,end=" : ")
    for i in range(0,n):
        print(arr[i],end=" ")
    print()
def main():
    arr=[4,8,1,7,5,2,6,3]
    n=len(arr)
    print_array('Before Sorting',arr,n)
    bubble_sort(arr,n)
    print_array('After Sorting',arr,n)
main()
