/*
 coder : bobby
 channel : Believer 01
 algorithm : Bubble sort
 date_coded: 10/06/2020
 time complexity : O(n*n)
*/
#include<stdio.h>
#include<stdlib.h>

void swap(int *arr,int i,int j)
{
    int temp=arr[i];
    arr[i]=arr[j];
    arr[j]=temp;
}
void bubble_sort(int *arr,int n)
{
    int i,j;
    for(i=0;i<n;i++)
    {
        for(j=0;j<n-i-1;j++)
        {
            if(arr[j]>arr[j+1])
                swap(arr,j,j+1);
        }
    }
}
void print_array(char *message,int *arr,int n)
{
    printf("%s : ",message);
    int i=0;
    for(i=0;i<n;i++)
        printf("%d ",arr[i]);
    printf("\n");
}
int main()
{
    int arr[]={4,8,1,7,5,2,6,3};
    int n=sizeof(arr)/sizeof(arr[0]);
    print_array("Before Sorting",arr,n);
    bubble_sort(arr,n);
    print_array("After Sorting",arr,n);
    return 0;
}
