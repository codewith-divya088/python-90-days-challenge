# Day 28 - Stack and Queue using List

# -------- STACK (LIFO) --------
stack = []

# Push (add element)
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after push:", stack)

# Pop (remove last element)
stack.pop()
print("Stack after pop:", stack)


# -------- QUEUE (FIFO) --------
queue = []

# Enqueue (add element)
queue.append(10)
queue.append(20)
queue.append(30)

print("Queue after enqueue:", queue)

# Dequeue (remove first element)
queue.pop(0)
print("Queue after dequeue:", queue)
