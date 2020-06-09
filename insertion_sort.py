# coder: bobby
# channel: Believer 01 
# date_coded: 09/06/2020 
# Insertion Sort
# Time Complexity: O(n*n)
def insertion_sort(arr,n):
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key

def print_array(message,arr,n):
    print(message,end=" : ")
    for i in range(0,n):
        print(arr[i],end=" ")
    print()
def main():
    arr=[5,8,2,6,1,7,3,4]
    n=len(arr)
    print_array('Before Sorting',arr,n)
    insertion_sort(arr,n)
    print_array('After Sorting',arr,n)
main()
