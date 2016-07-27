class Queue(object):

    def __init__(self):
        "Initializes 1 attribute: a list to keep track of the queue's elements"
        self.vals = []

    def insert(self, e):
        "Adds an element to the attribute list using append"
        self.vals.append(e)

    def remove(self):
        try:
            return self.vals.pop()
        except:
            raise ValueError( 'List empty')
"""
queue = Queue()
queue.insert(5)
queue.insert(6)
queue.remove()
queue.insert(7)
queue.remove()
queue.remove()
queue.remove()
"""
q1 = Queue()
q2 = Queue()
q1.insert(17)
q2.insert(20)
q1.remove()
q2.remove()
