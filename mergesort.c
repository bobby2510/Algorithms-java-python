/*
 coder : bobby
 channel : Believer 01
 algorithm : Merge sort
 date_coded: 08/06/2020
 time complexity : O(n*log(n))
*/
#include<stdio.h>
#include<stdlib.h>

void merge(int *arr,int * l_arr,int * r_arr,int l_size,int r_size,int n)
{
    int i=0,j=0,k=0;
    while(i<l_size && j<r_size)
    {
        if(l_arr[i]<r_arr[j])
        {
            arr[k]=l_arr[i];
            i++;
        }
        else
        {
            arr[k]=r_arr[j];
            j++;
        }
        k++;
    }
    while(i<l_size)
    {
        arr[k]=l_arr[i];
        i++;
        k++;
    }
    while(j<r_size)
    {
        arr[k]=r_arr[j];
        j++;
        k++;
    }
}
void merge_sort(int *arr,int n)
{
    if(n>1)
    {
        int l_size=n/2,r_size=n-l_size;
        int *l_arr=(int*)malloc(sizeof(int*)*l_size);
        int *r_arr=(int*)malloc(sizeof(int*)*r_size);
        int i=0,j=0;
        for(i =0;i<l_size;i++)
        {
            l_arr[i]=arr[j];
            j++;
        }
        for(i=0;i<r_size;i++)
        {
            r_arr[i]=arr[j];
            j++;
        }
        merge_sort(l_arr,l_size);
        merge_sort(r_arr,r_size);
        merge(arr,l_arr,r_arr,l_size,r_size,n);
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
    merge_sort(arr,n);
    print_array("After Sorting",arr,n);
    return 0;
}
