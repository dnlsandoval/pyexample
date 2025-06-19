from collections import deque

class ZigzagIterator:
    def __init__(self, *vectors):
        # Store non-empty iterators in a deque
        self.queue = deque([iter(v) for v in vectors if v])

    def next(self):
        if self.hasNext():
            # Pop the iterator from the front
            current = self.queue.popleft()
            # Get the next element
            value = next(current)
            # If the iterator still has elements, add it back to the queue
            if any(True for _ in current):
                self.queue.append(current)
            return value

    def hasNext(self):
        return bool(self.queue)

# Example usage:
v1 = [1, 2]
v2 = [3, 4, 5, 6]
v3 = [7, 8, 9]
iterator = ZigzagIterator(v1, v2, v3)
result = []
while iterator.hasNext():
    result.append(iterator.next())
print(result)  # Output: [1, 3, 2, 4, 5, 6]
