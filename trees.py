from collections import deque
class tree_imp :
    def __init__(self, value, right=None, left=None) :
        self.value = value
        self.left = left
        self.right = right
    def __str__(self) :
        return str(self.value)
A = tree_imp(1)
B = tree_imp(2)
C = tree_imp(3)
D = tree_imp(4)
E = tree_imp(5)
F = tree_imp(6)
G = tree_imp(7)
L = tree_imp(10)
M = tree_imp(12)
A.right = C
A.left = B
B.right = E
B.left = D
C.right = G
C.left = F
F.left = L
E.right = M
def maxDepth(A) :
    q = deque()
    if A :
        q.append(A)
    level = 0
    while q :
        for i in range(len(q)) :
            node = q.popleft()
            if node.right :
                q.append(node.right)
            if node.left :
                q.append(node.left)
        level += 1
    return level
print(maxDepth(A))