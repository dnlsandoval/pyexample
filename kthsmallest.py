import random

def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]
    
    pivot = random.choice(arr)
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]
    
    if k <= len(lows):
        return quickselect(lows, k)
    elif k <= len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots))

# Example usage
array = [7, 10, 4, 3, 20, 15]
k = 3
print(quickselect(array, k))  # Output: 7
