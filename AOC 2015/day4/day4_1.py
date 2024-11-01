import hashlib

history = []
input_string = "bgvyzdsv"

for num in range(10000000):
    # Create a new MD5 hash object for each iteration
    md5_hash = hashlib.md5()
    
    # Concatenate the input string and number
    no = input_string + str(num)
    
    # Update the hash object with the bytes of the concatenated string
    md5_hash.update(no.encode('utf-8'))
    
    # Get the hexadecimal representation of the hash
    hash_value = md5_hash.hexdigest()
    
    # Check if it has at least five leading zeros
    if hash_value.startswith("00000"):
        history.append(num)
        break  # Stop after finding the first match

# Print the smallest number found
print(min(history))
