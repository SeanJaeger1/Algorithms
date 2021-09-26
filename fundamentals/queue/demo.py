from queue import Queue

# instantiate queue, add some values, show that they're added and popped in the right order
new_queue = Queue()

print(new_queue)

new_queue.enqueue(1)
new_queue.enqueue(4)
new_queue.enqueue(67)
new_queue.enqueue(3)

print(new_queue)


print(new_queue.dequeue())

print(new_queue)

new_queue.dequeue()
new_queue.dequeue()
new_queue.dequeue()

print(new_queue)
