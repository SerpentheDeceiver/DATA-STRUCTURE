# Example of a dictionary
my_dict = {
    "apple": 1,
    "banana": 2,
    "cherry": 3,
    "date": 4,
    "elderberry": 5
}

# Function to add elements to the dictionary
def add_elements(n):
    for i in range(n):
        my_dict[f"fruit_{i}"] = i

# Adding 1000 elements to the dictionary
add_elements(100)

# Checking the length of the dictionary
print(len(my_dict))
print(my_dict)

#HERE THE SPACE COMPLEXITY IS --> O(N)