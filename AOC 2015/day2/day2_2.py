import re

total_area = 0  # Initialize the total area variable
with open("C:/Users/Acer/Desktop/AOC/AOC 2015/day2/input.txt", 'r') as f:
    while True:
        line = f.readline()
        if not line: 
            break
        
        # Find all numbers in the line
        numbers = re.findall(r'\d+', line)
        
        # Convert each number to an integer
        if len(numbers) == 3:
            l, b, h = map(int, numbers) 
            volume = l * b * h  # Calculate the volume of the box
            
            # Calculate the perimeter based on the largest dimension
            if l >= b and l >= h:
                perimeter = 2 * (b + h)  # If l is the largest, use b and h
            elif b >= l and b >= h:
                perimeter = 2 * (l + h)  # If b is the largest, use l and h
            else:  # h is the largest
                perimeter = 2 * (l + b)  # If h is the largest, use l and b
            
            # Add volume and perimeter to the total area
            total_area += volume + perimeter
            
            print(f"Length: {l}, Breadth: {b}, Height: {h}, Total Area: {volume + perimeter}")

print("Total area of cloth needed:", total_area)
