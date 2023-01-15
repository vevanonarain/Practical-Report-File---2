#Task 42 - 10/1/2023
#Vevan O Narain S6-C

"""WAPP to process QUEUE (FIFO) operations on a Python LIST of names"""

queue = []
  
queue.append('a')
queue.append('b')
queue.append('c')
  
print("Initial queue")
print(queue)
  
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
  
print("\nQueue after removing elements")
print(queue)