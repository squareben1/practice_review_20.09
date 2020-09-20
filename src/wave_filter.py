
def wave_filter(arr):
    for i in range(len(arr)):
        if arr[i] < 10:
            arr[i] = 10
    return arr
