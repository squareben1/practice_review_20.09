
def wave_filter(arr, lower=10, upper=20):
    lower = lower
    upper = upper

    for i in range(len(arr)):
        if arr[i] < lower:
            arr[i] = lower
        if arr[i] > upper:
            arr[i] = upper
    return arr
