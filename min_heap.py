# -*- coding: utf-8 -*-
"""min_heap.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RBnu0KaobTIr7vwzmosS3eLs6KQAnPpR
"""

class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) >> 1

    def left(self, i):
        return (i << 1) + 1

    def right(self, i):
        return (i << 1) + 2

    def build_min_heap(self, array):
        self.heap = array
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(i)

    def heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        smallest = i
        if l < len(self.heap) and self.heap[l] < self.heap[i]:
            smallest = l
        if r < len(self.heap) and self.heap[r] < self.heap[smallest]:
            smallest = r
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    def pop(self):
        if not self.heap:
            return None
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify(0)
        return root

    def insert(self, key):
        self.heap.append(key)
        i = len(self.heap) - 1
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

# Example usage
heap = MinHeap()
heap.build_min_heap([3, 1, 6, 9, 5, 2, 4])
print("Heap after build:", heap.heap)

heap.insert(0)
print("Heap after inserting 0:", heap.heap)

print("Popped root:", heap.pop())
print("Heap after popping root:", heap.heap)

