puzzle_in = 277678

x = 0
y = 0
memboard = {(0, 0): 1}
#   0
# 1   3
#   2

def make_value(mb, x, y):
    result = 0
    for i in range(x-1, x+2):
        for j in range (y-1, y+2):
            if (i,j) in mb:
                result += mb[(i,j)]
    return result

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
    
    value = make_value(memboard, x, y)
    memboard[(x,y)] = value
    if value > puzzle_in:
        print value
        break

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
