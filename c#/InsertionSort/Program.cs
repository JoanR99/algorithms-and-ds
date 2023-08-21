int[] a = { 31, 41, 59, 26, 41, 58 };

for (int i = 1; i < a.Length; i++)
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

for (int i = 0; i < a.Length; i++)
{
    Console.WriteLine(a[i]);
}