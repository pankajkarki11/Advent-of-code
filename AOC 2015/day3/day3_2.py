# Open and read the directions from the input file
with open('C:\\Users\\Acer\\Desktop\\AOC\\AOC 2015\\day3\\input_3.txt', 'r') as f:
    directions = f.read()

# Initialize history with the starting position
history = [(0, 0),(0,0)]

# Iterate over each direction in the directions input
for direction in directions:
    last = history[-2]
    if direction == 'v':
        history.append((last[0], last[1] - 1))
    elif direction == '^':
        history.append((last[0], last[1] + 1))
    elif direction == '>':
        history.append((last[0] + 1, last[1]))
    elif direction == '<':
        history.append((last[0] - 1, last[1]))

# Count the unique positions visited
print(len(set(history)))
