#include "iostream"
#include "cmath"

using namespace std;

bool binarySearch(int array[4], int v)
{
    int lo = 0;
    int hi = 4;

    do
    {
        int m = floor(lo + (hi - lo) / 2);

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

int main()
{
    int a[4] = {2, 4, 5, 8};

    cout << binarySearch(a, 7);
}