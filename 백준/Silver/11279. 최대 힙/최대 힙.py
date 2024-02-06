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
        while curIndex != 1 and self.queue[curIndex] > self.queue[parentIndex]:
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
        leftChildIndex = self.getLeftChildIndex(index)
        rightChildIndex = self.getRightChildIndex(index)

        while leftChildIndex < len(self.queue):
            maxChildIndex = leftChildIndex

            if rightChildIndex < len(self.queue) and self.queue[rightChildIndex] > self.queue[leftChildIndex]:
                maxChildIndex = rightChildIndex

            if self.queue[curIndex] >= self.queue[maxChildIndex]:
                break

            self.swap(curIndex, maxChildIndex)
            curIndex = maxChildIndex
            leftChildIndex = self.getLeftChildIndex(curIndex)
            rightChildIndex = self.getRightChildIndex(curIndex)
    # def whenPop(self, index):
    #     curIndex = index
    #     leftChildIndex = maxPQ.getLeftChildIndex(index)
    #     rightChildIndex = maxPQ.getRightChildIndex(index)
    #
    #     if leftChildIndex >= len(self.queue):
    #         return
    #
    #     while self.queue[curIndex] <= self.queue[leftChildIndex] and self.queue[curIndex] <= self.queue[rightChildIndex]:
    #         print(self.queue)
    #         if self.queue[curIndex] >= self.queue[leftChildIndex] >= self.queue[rightChildIndex]:
    #             break
    #         if len(self.queue) == 3 and self.queue[1] < self.queue[2]:
    #             self.swap(curIndex, leftChildIndex)
    #             break
    #         if self.queue[leftChildIndex] >= self.queue[rightChildIndex] > self.queue[curIndex]:
    #             print("왼쪽으로이동")
    #             self.swap(curIndex, leftChildIndex)
    #             curIndex = leftChildIndex
    #             leftChildIndex = maxPQ.getLeftChildIndex(curIndex)
    #             rightChildIndex = maxPQ.getRightChildIndex(curIndex)
    #             continue
    #         if self.queue[rightChildIndex] > self.queue[leftChildIndex] >= self.queue[curIndex]:
    #             print("오른쪽으로이동")
    #             self.swap(curIndex, rightChildIndex)
    #             curIndex = rightChildIndex
    #             leftChildIndex = maxPQ.getLeftChildIndex(curIndex)
    #             rightChildIndex = maxPQ.getRightChildIndex(curIndex)
    #             continue

        # whenOnlyLeftChild = False
        # onlyLeftChildBig = False
        # onlyRightChildBig = False
        # whenBothBigger = False
        # curIndexBigger = True
        #
        # if len(self.queue) == 3 and self.queue[1] < self.queue[2]:
        #     whenOnlyLeftChild = True
        #
        # if leftChildIndex < len(self.queue) and rightChildIndex < len(self.queue):
        #     onlyLeftChildBig = self.queue[leftChildIndex] > self.queue[index] >= self.queue[rightChildIndex]
        #     onlyRightChildBig = self.queue[rightChildIndex] > self.queue[index] >= self.queue[leftChildIndex]
        #     curIndexBigger = self.queue[index] >= self.queue[leftChildIndex] >= self.queue[rightChildIndex]
        #     whenBothBigger = self.queue[leftChildIndex] > self.queue[index] and self.queue[rightChildIndex] > \
        #                      self.queue[index]
        #
        # if whenOnlyLeftChild:
        #     self.swap(leftChildIndex, index)
        #     return self.whenPop(leftChildIndex)
        # if onlyLeftChildBig:
        #     self.swap(leftChildIndex, index)
        #     return self.whenPop(leftChildIndex)
        # if onlyRightChildBig:
        #     self.swap(rightChildIndex, index)
        #     return self.whenPop(rightChildIndex)
        # if whenBothBigger:
        #     if self.queue[leftChildIndex] >= self.queue[rightChildIndex]:
        #         self.swap(leftChildIndex, index)
        #         return self.whenPop(leftChildIndex)
        #     if self.queue[rightChildIndex] > self.queue[leftChildIndex]:
        #         self.swap(rightChildIndex, index)
        #         return self.whenPop(rightChildIndex)
        # if curIndexBigger:
        #     return

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

