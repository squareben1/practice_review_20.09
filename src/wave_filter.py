
def wave_filter(arr, lower=10):
    lower = lower
    upper = 20

    for i in range(len(arr)):
        if arr[i] < lower:
            arr[i] = lower
        if arr[i] > upper:
            arr[i] = upper
    return arr
