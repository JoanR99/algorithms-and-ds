int[] a = { 2, 4, 2, 8, 1 };

for (int i = 0; i < a.Length; i++)
{
    for (int j = 0; j < a.Length - i - 1; j++)
    {
        if (a[j] > a[j + 1])
        {
            int tmp = a[j];
            a[j] = a[j + 1];
            a[j + 1] = tmp;
        }
    }
}

for (int i = 0; i < a.Length; i++)
{
    Console.WriteLine(a[i]);
}