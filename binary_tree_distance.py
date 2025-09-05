target = 5
distance = 2
cur_distance = 0
answer = []
while cur_distance != distance :
    target = target.next
    cur_distance += 1
answer.append(target.next)
cur_distance = 0
while cur_distance != distance :
    target = target.previous
    cur_distance += 1