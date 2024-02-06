from collections import deque
import sys


class maxPQ(object):
    @staticmethod
    def getParentIndex(index):
        return index // 2

    @staticmethod
    def getLeftChildIndex(index):
        return index * 2

    @staticmethod
    def getRightChildIndex(index):
        return (index * 2) + 1

    def __init__(self):
        self.queue = deque()
        self.queue.append([])

    def add(self, value):
        self.queue.append(value)
        self.sorting(len(self.queue) - 1)

    def sorting(self, index):
        curIndex = index
        parentIndex = maxPQ.getParentIndex(index)
        while curIndex != 1 and self.queue[curIndex] < self.queue[parentIndex]:
            self.swap(curIndex, parentIndex)
            curIndex = parentIndex
            parentIndex = maxPQ.getParentIndex(parentIndex)
    def pop(self):
        popped = self.queue[1]
        self.queue[1] = self.queue[-1]
        self.queue.pop()
        self.whenPop(1)
        return popped

    def whenPop(self, index):
        curIndex = index
        leftChildIndex = maxPQ.getLeftChildIndex(index)
        rightChildIndex = maxPQ.getRightChildIndex(index)

        while leftChildIndex < len(self.queue):
            maxChildIndex = leftChildIndex

            if rightChildIndex < len(self.queue) and self.queue[rightChildIndex] < self.queue[leftChildIndex]:
                maxChildIndex = rightChildIndex

            if self.queue[curIndex] <= self.queue[maxChildIndex]:
                break

            self.swap(curIndex, maxChildIndex)
            curIndex = maxChildIndex
            leftChildIndex = maxPQ.getLeftChildIndex(curIndex)
            rightChildIndex = maxPQ.getRightChildIndex(curIndex)

    def swap(self, i, j):
        temp = self.queue[i]
        self.queue[i] = self.queue[j]
        self.queue[j] = temp


def sInput():
  return sys.stdin.readline()


T = int(sInput())

maxHeap = maxPQ()
for i in range(T):
  inputValue = int(sInput())
  if len(maxHeap.queue) == 1 and inputValue == 0:
    print(0)
    continue
  if len(maxHeap.queue) != 1 and inputValue == 0:
    print(maxHeap.pop())
    continue
  if inputValue != 0:
    maxHeap.add(inputValue)
    continue