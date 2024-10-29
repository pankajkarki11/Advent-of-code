with open("C:/Users/Acer/Desktop/AOC/AOC 2015/day1/input.txt",'r') as f:
    # your code here

    i=0
    j=0
    while True:
        j+=1
        char=f.read(1)
        if not char:      # If end of file is reached, break
            break
        if char == '(':   # Increase the counter if character is '('
            i += 1
        elif char == ')': # Decrease the counter if character is ')'
            i -= 1
        if i==-1:
            break
    print(j)