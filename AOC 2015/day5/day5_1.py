'''
nice=0
combination_list=['ab','cd','pq','xy']
with open("C:\\Users\\Acer\\Desktop\\AOC\\AOC 2015\\day5\\input5.txt",'r') as f:
    while True:
        combinations = [None]
        count=0
        line = f.readline()
        if not line: 
            break
            for i in range(len(line)-1):
                 combinations.append(line[i]+line[i+1])
                 if line[i]+line[i+1]==line[i+1]+line[i]:
                        count+=1                                     
        vowels = set("aeiou")

# Use a list comprehension to get only vowels in the word
        vowel_list = [letter for letter in line if letter in vowels]
# Check if the length of the vowel list is at least 3
        if len(vowel_list) >= 3:
# Compare each item with every other item
            for i in range(len(combination_list)-1):
                for j in range(len(combinations)-1):  # Start from i+1 to avoid self-comparison and duplicates
                      if combination_list[i] == combinations[j]:
                          if count>0:
                            nice+=1

print(nice)

'''
nice = 0
combination_list = ['ab', 'cd', 'pq', 'xy']

with open("C:\\Users\\Acer\\Desktop\\AOC\\AOC 2015\\day5\\input5.txt", 'r') as f:
    while True:
        line = f.readline().strip()  # Read line and remove newline
        if not line:
            break

        # Generate all two-letter combinations in the line
        combinations = [line[i] + line[i + 1] for i in range(len(line) - 1)]

        # Count the occurrences of duplicate consecutive pairs (e.g., "aa")
        count = sum(1 for i in range(len(line) - 1) if line[i] == line[i + 1])

        # Check if line has at least three vowels
        vowels = set("aeiou")
        vowel_count = sum(1 for letter in line if letter in vowels)

        # Check if the line contains any forbidden combination
        contains_forbidden = any(pair in combinations for pair in combination_list)

        # Criteria to increment 'nice'
        if vowel_count >= 3 and not contains_forbidden and count > 0:
            nice += 1

print(nice)

