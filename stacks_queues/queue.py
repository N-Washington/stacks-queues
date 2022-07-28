
INITIAL_QUEUE_SIZE = 20

class QueueFullException(Exception):
    pass

class QueueEmptyException(Exception):
    pass

class Queue:

    def __init__(self, capacity):
        self.store = [None] * capacity
        self.buffer_size = capacity
        self.front = -1
        self.rear = -1
        self.size = 0

    def enqueue(self, element):
        """ Adds an element to the Queue
            Raises a QueueFullException if all elements
            In the store are occupied
            returns None
        """
        # check if full -> if so raise exception
        if self.full():
            raise QueueFullException("Queue is full")

        # check if empty -> if so, set starting front and rear index
        if self.empty():
            self.front = 0
            self.rear = 0

        # add element to rear of queue
        self.store[self.rear] = element
        # update queue
        self.rear = (self.rear + 1) % self.buffer_size
        self.size += 1
        print("que size at the end of this round: ", self.size)
        print("que porgress", self.store)


    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
        """
        # check if empty -> if so, raise exception
        if self.empty():
            raise QueueEmptyException("Queue is empty")
        # get front element
        first_in_que = self.front_element()
        # update queue
        print("we were just supposed to remove front element, what is", self.front)
        self.front = (self.front + 1) % self.buffer_size
        self.size -= 1
        # Check if empty after removing element -> if so, re-set front and rear index variable
        if self.empty():
            self.front = -1
            self.rear = -1
        return first_in_que

    def front_element(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """
        if self.empty():
            return None
        return self.store[self.front]

    def size(self):
        """ Returns the number of elements in
            The Queue
        """
        return self.size

    def empty(self):
        """ Returns True if the Queue is empty
            And False otherwise.
        """
        if self.size <= 0:
            return True
        return False

    def full(self):
        """
        returns True id Queue is full
        and False otherwise
        """
        if self.size == self.buffer_size:
            return True
        return False

    def __str__(self):
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.
        """
        queue_values = self.store[self.front:self.rear]
        print(self.store)
        print("---------")
        print(self.front)
        print(self.rear)
        print("---------")
        return str(queue_values)

new_queue = Queue(20)
new_queue.enqueue(30)
new_queue.enqueue(11)
new_queue.enqueue(15)
new_queue.dequeue()
new_queue.dequeue()
print("does size belwo change , should be 2" )
new_queue.enqueue(10)

print("ok callinf the bog boys in now")
for num in [40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220]:
            new_queue.enqueue(num)

new_queue.__str__()