# coder: bobby
# channel: Believer 01 
# date_coded: 08/06/2020 
# Merge Sort
# Time Complexity: O(n*log(n))
# 4 8 1 7 2 6 5 3

def merge(arr,first_array,second_array,first_part,second_part,n):
    i=0
    j=0
    k=0
    while i<first_part and j<second_part:
        if first_array[i]<second_array[j]:
            arr[k]=first_array[i]
            i+=1
        else:
            arr[k]=second_array[j]
            j+=1
        k+=1
    while i<first_part:
        arr[k]=first_array[i]
        i+=1
        k+=1
    while j<second_part:
        arr[k]=second_array[j]
        j+=1
        k+=1
def merge_sort(arr,n):
    if n>1:
        first_part=n//2
        second_part=n-first_part
        first_array=[]
        second_array=[]
        j=0
        for i in range(0,first_part):
            first_array.append(arr[j])
            j+=1
        for i in range(0,second_part):
            second_array.append(arr[j])
            j+=1
        merge_sort(first_array,first_part)
        merge_sort(second_array,second_part)
        merge(arr,first_array,second_array,first_part,second_part,n)
def print_array(message,arr,n):
    print(message,end=" : ")
    for i in range(0,n):
        print(arr[i],end=" ")
    print()
def main():
    arr=[4,8,1,7,2,6,5,3]
    n=len(arr)
    print_array('Before Sorting',arr,n)
    merge_sort(arr,n)
    print_array('After Sorting',arr,n)
main()
