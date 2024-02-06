import heapq, sys

def sInput():
  return sys.stdin.readline()

T = int(sInput())

maxHeap = []
for i in range(T):
  inputValue = int(sInput())
  if len(maxHeap) == 0 and inputValue == 0:
    print(0)
    continue
  if len(maxHeap) != 0 and inputValue == 0:
    print(heapq.heappop(maxHeap))
    continue
  if inputValue != 0:
    heapq.heappush(maxHeap, inputValue)
    continue