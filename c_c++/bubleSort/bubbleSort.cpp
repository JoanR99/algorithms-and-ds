#include "iostream"

using namespace std;

int main()
{
    int a[5] = {2, 4, 2, 8, 1};
    int length = sizeof(a) / sizeof(a[0]);

    for (int i = 0; i < length; i++)
    {
        for (int j = 0; j < length - i - 1; j++)
        {
            if (a[j] > a[j + 1])
            {
                int temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
            }
        }
    }

    for (int i = 0; i < length; i++)
    {
        cout << a[i] << endl;
    }
}