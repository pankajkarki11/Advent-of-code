# Open the file in read mode

with open("input.txt", 'r') as f:
    i = 0  # Initialize the counter variable
    while True:
        char = f.read(1)  # Read one character
        if not char:      # If end of file is reached, break
            break
        if char == '(':   # Increase the counter if character is '('
            i += 1
        elif char == ')': # Decrease the counter if character is ')'
            i -= 1
           

    print('floor', i)  # Print the final result


