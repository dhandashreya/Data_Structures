#include<stdio.h>
// rotating the array using another array
// time complexity is O(n)
// space complexity is O(d)
void rotate_one(int arr[], int n, int d)
{
    int temp[d];
    int k = n - d;
    for(int i = 0; i < n; i++)
    {
        if(i < d)
        {
            temp[i] = arr[i];
        }
        else
        {
            arr[i - d] = arr[i];
        }
    }
    for(int i = 0; i < d; i++)
    {
        arr[k] = temp[i];
        k++;
    }
}

// function to rotate the array by one element
void left_rotate_by_one(int arr[], int n)
{
    int temp = arr[0];
    for(int i = 0; i < n-1; i++)
    {
        arr[i] = arr[i+1];
    }
    arr[n-1] = temp;
}

// function to rotate the list d times
// time complexity is O(n*d)
// space complexity is O(1)
void left_rotate(int arr[], int n, int d)
{
    for(int i = 0; i < d; i++)
    left_rotate_by_one(arr, n);
}
// function to print an array
void print(int arr[], int n)
{
    for(int i = 0 ; i < n; i++)
    {
        printf("%d ", arr[i]);
    }
}

int main()
{
    int a[] = {1, 2, 3, 4, 5, 6, 7};
    int length = sizeof(a)/sizeof(int);
    int r =2;
    rotate_one(a, length, r);
    print(a, length);
    printf("\n");
    //Now, original array is {3, 4, 5, 6, 7, 1, 2}
    left_rotate(a, length, r);
    print(a, length);
    return 0;
}
