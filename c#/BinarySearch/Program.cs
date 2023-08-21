
using System;
int[] a = { 2, 4, 5, 8 };

bool BinarySearch(int[] array, int v)
{
    int lo = 0;
    int hi = array.Length;


    do
    {
        int m = (lo + hi) / 2;

        if (array[m] == v)
        {
            return true;
        }
        else if (array[m] > v)
        {
            hi = m;
        }
        else
        {
            lo = m + 1;
        }
    } while (lo < hi);

    return false;
}

bool result = BinarySearch(a, 7);

Console.WriteLine(result);