
def wave_filter(arr):
    for i in range(len(arr)):
        if arr[i] < 10:
            arr[i] = 10
        if arr[i] > 20:
            arr[i] = 20
    return arr
