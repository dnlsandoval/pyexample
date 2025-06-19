class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        # Initialize the current pointer to 0 to start with the first vector
        self.current = 0
        # The size variable indicates the number of vectors (always 2 in this case)
        self.size = 2
        # Create a list to keep track of the current index in each vector
        self.indices = [0] * self.size
        # Store the two input vectors
        self.vectors = [v1, v2]

    def next(self) -> int:
        # Identify the current vector and its index
        vector = self.vectors[self.current]
        index = self.indices[self.current]
        # Retrieve the next element from the current vector
        result = vector[index]
        # Increment the index for the current vector
        self.indices[self.current] = index + 1
        # Move to the next vector for the following call
        self.current = (self.current + 1) % self.size
        # Return the retrieved element
        return result

    def hasNext(self) -> bool:
        # Store the starting point to avoid infinite loops
        start = self.current
        # Check if the current vector is exhausted and move to the next one if necessary
        while self.indices[self.current] == len(self.vectors[self.current]):
            # Move to the next vector
            self.current = (self.current + 1) % self.size
            # If we loop back to the start, that means all vectors are exhausted
            if self.current == start:
                return False
        # If we haven't returned yet, there's still at least one element left
        return True


v1 = [1, 2]
v2 = [3, 4, 5, 6]
iterator = ZigzagIterator(v1, v2)
result = []
while iterator.hasNext():
    result.append(iterator.next())
print(result)  # Output: [1, 3, 2, 4, 5, 6]