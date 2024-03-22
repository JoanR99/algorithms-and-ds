#include <iostream>
using namespace std;
 
int partition(int arr[], int lo, int hi)
{
    int pivot = arr[hi];
    int idx = lo - 1;

    for (int i = lo; i < hi; i++) {
        if (arr[i] <= pivot) {
            ++idx;
            int tmp = arr[i];
            arr[i] = arr[idx];
            arr[idx] = tmp;
        }
    }
 
   ++idx;
   arr[hi] = arr[idx];
   arr[idx] = pivot;
 
    return idx;
}
 
void quickSort(int arr[], int lo, int hi)
{
 
    // base case
    if (lo >= hi)
        return;
 
    // partitioning the array
    int p = partition(arr, lo, hi);
 
    // Sorting the left part
    quickSort(arr, lo, p - 1);
 
    // Sorting the right part
    quickSort(arr, p + 1, hi);
}
 
int main()
{
 
    int arr[] = { 9, 3, 4, 2, 1, 8 };
    int n = 6;
 
    quickSort(arr, 0, n - 1);
 
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
 
    return 0;
}