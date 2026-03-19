def reverse_my_name(name):
    # Conditional check 1: Validate that the input is actually a string and not empty
    if not isinstance(name, str) or len(name) == 0:
        return "Invalid input: Please provide a valid string."
        
    reversed_name = ""
    
    # Loop: Traverse the string from the last character down to the first
    # range(start, stop, step) -> start at last index, stop before -1, step backwards by 1
    for i in range(len(name) - 1, -1, -1):
        char = name[i]
        
        # Conditional check 2: Only append if it's a letter or a space
        # This shows the interviewer you are thinking about data validation
        if char.isalpha() or char.isspace():
            reversed_name += char
        else:
            print(f"Warning: Skipping invalid character '{char}'")
            
    return reversed_name

# Executing the function
my_name = "Nandini Saha"
result = reverse_my_name(my_name)

print(f"Reversed Name: {result}")