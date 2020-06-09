/*
 coder : bobby
 channel : Believer 01
 algorithm : Insertion sort
 date_coded: 09/06/2020
 time complexity : O(n*n)
*/
#include<stdio.h>
#include<stdlib.h>

void insertion_sort(int *arr,int n)
{
   int i,j,key;
   for(i=1;i<n;i++)
   {
       key=arr[i];
       j=i-1;
       while(j>=0 && arr[j]>key)
       {
           arr[j+1]=arr[j];
           j--;
       }
       arr[j+1]=key;
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
    int arr[]={4,8,1,7,2,6,5,3};
    int n=sizeof(arr)/sizeof(arr[0]);
    print_array("Before Sorting",arr,n);
    insertion_sort(arr,n);
    print_array("After Sorting",arr,n);
    return 0;
}
