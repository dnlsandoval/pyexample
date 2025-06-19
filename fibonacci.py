def fibonacci_iterative(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    sequence = fibonacci_recursive(n - 1)
    sequence.append(sequence[-1] + sequence[-2])
    return sequence

def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Example usage
print(fibonacci_iterative(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Example usage
print(fibonacci_recursive(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Example usage
print(list(fibonacci_generator(10)))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]