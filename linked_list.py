class Node :
    def __init__(self, value) :
        self.value = value
        self.next = None
        self.prev = None
class Linked_List :
    def _init(self) :
        self.left = Node(0)
        self.right = Node(0)
        self.left.next = self.right
        self.right.prev = self.left
    def get(self, pos) :
        current = self.left.next
        while current and current and pos > 0 :
            current = current.next
            pos -= 1
        if current != self.right and pos == 0 :
            return current.value
        return -1
    def add_first(self, value) :
        node, next, prev = Node(value), self.left.next, self.left
        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next
    def add_last(self, value) :
        node, next, prev = Node(value), self.right, self.right.prev
        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next
    def add_pos(self, value, pos) :
        current = self.left.next
        while current <= pos :
            current = current.next
        node, next, prev = Node(value), current.next, current.prev
        next.prev = node
        prev.next = node
        node.next = next
        node.prev = prev
    def delete_pos(self, pos) :
        current = self.left.next
        while current and current <= pos :
            current = current.next
        next, prev = current.next, current.prev
        next.prev = prev
        prev.next = next
        
