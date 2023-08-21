#include "iostream"

using namespace std;

int main()
{
    int a[6] = {31, 41, 59, 26, 41, 58};
    int length = sizeof(a) / sizeof(a[0]);

    for (int i = 1; i < length; i++)
    {
        int key = a[i];
        int j = i - 1;

        while (j >= 0 && a[j] > key)
        {
            a[j + 1] = a[j];
            j--;
        }

        a[j + 1] = key;
    }

    for (int i = 0; i < length; i++)
    {
        cout << a[i] << endl;
    }

    cout << "reverse \n"
         << endl;

    for (int i = 1; i < length; i++)
    {
        int key = a[i];
        int j = i - 1;

        while (j >= 0 && a[j] < key)
        {
            a[j + 1] = a[j];
            j--;
        }

        a[j + 1] = key;
    }

    for (int i = 0; i < length; i++)
    {
        cout << a[i] << endl;
    }
}