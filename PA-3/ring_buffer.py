"""
Author: Vishruth Bharath
Class: W2023 CSE 30
Objective: To build a class that class that implements the circular
buffer data structure which acts as a fixed-size buffer that stores a certain number of elements and discards the
oldest elements when it's full.
"""


class RingBuffer:
    def __init__(self, k: int):
        """
        Initialize the ring buffer with the given "k" to represent maximum size.
        """
        self.max_size = k
        self.buffer = []

    def en_queue(self, value: int) -> None:
        """
        Add a value to the buffer. If the buffer is full, the oldest value, or  will be removed to make room.
        """
        if len(self.buffer) == self.max_size:
            self.buffer.pop(0)
        self.buffer.append(value)

    def de_queue(self) -> bool:
        """
        Remove front value from the buffer. Return `True` if a value was removed or vice versa.
        """
        if self.is_empty():
            return False
        else:
            self.buffer.pop(0)
            return True

    def get_front(self) -> int:
        """
        Return the front integer value in the buffer. If buffer is empty, return -1 as instructed.
        """
        return self.buffer[0] if self.buffer else -1

    def get_rear(self) -> int:
        """
        Return last, or newest, value as an int in the buffer. If buffer is empty, return -1 as instructed.
        """
        return self.buffer[-1] if self.buffer else -1

    def is_empty(self) -> bool:
        """
        Return boolean `True` if the buffer is full, or vice versa.
        """
        return not bool(self.buffer)

    def is_full(self) -> bool:
        """
        Return boolean `True` if the buffer is full, or vice versa.
        """
        return True if len(self.buffer) == self.max_size else False

    def get_average(self) -> float:
        """
        Return average of all elements stored in the buffer. Return None if buffer is empty.
        """
        return sum(self.buffer) / len(self.buffer) if self.buffer else None
