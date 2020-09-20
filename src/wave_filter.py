
def wave_filter(arr, lower=10, upper=20):
    return [lower if i < lower else upper if i > upper else i for i in arr]
