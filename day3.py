puzzle_in = 277678

x = 0
y = 0
#   0
# 1   3
#   2

direction = 3
iteration = 0
distance_target = 1
distance = 1

for i in range(1, puzzle_in):
    if direction == 1:
        x -= 1
    elif direction == 2:
        y -= 1
    elif direction == 3:
        x += 1
    else:
        y += 1
    
    distance -= 1
    if distance == 0:
        direction = (direction + 1) % 4
        if iteration == 1:
            distance_target += 1
            distance = distance_target
            iteration = 0
        else:
            iteration = 1
            distance = distance_target

print abs(x) + abs(y)
