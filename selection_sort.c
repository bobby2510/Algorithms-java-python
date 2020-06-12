/*
 coder : bobby
 channel : Believer 01
 algorithm : Selection sort
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
void selection_sort(int *arr,int n)
{
    int i,j,min_value,min_value_index;
    for(i=0;i<n-1;i++)
    {
        min_value=arr[i];
        min_value_index=i;
        for(j=i+1;j<n;j++)
        {
            if(arr[j]<min_value)
            {
                min_value=arr[j];
                min_value_index=j;
            }
        }
        swap(arr,i,min_value_index);
    }
}
void print_array(char *message,int *arr,int n)
{
    printf("%s : ",message);
    int i;
    for(i=0;i<n;i++)
        printf("%d ",arr[i]);
    printf("\n");
}
int main()
{
    int arr[]={3,2,6,5,8,7,1,4};
    int n=sizeof(arr)/sizeof(arr[0]);
    print_array("Before Sorting",arr,n);
    selection_sort(arr,n);
    print_array("After Sorting",arr,n);
}
