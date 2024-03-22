def partition(arr: list[int], lo: int, hi: int) -> int:
    pivot = arr[hi]
    idx = lo - 1
    
    for i in range(lo, hi):
        if(arr[i] <= pivot):
            idx += 1
            tmp = arr[i]
            arr[i] = arr[idx]
            arr[idx] = tmp
            
    idx += 1
    arr[hi] = arr[idx]
    arr[idx] = pivot
    
    return idx

def quick_sort(arr: list[int], lo: int, hi: int):
    if lo >= hi:
        return
    
    p = partition(arr, lo, hi)
    
    quick_sort(arr, lo, hi -1)
    quick_sort(arr, lo + 1, hi)
    

testArr = [8, 6, 2, 3, 9]

quick_sort(testArr, 0, len(testArr) - 1)

for item in testArr:
    print(item)