# Input dictionary with names
name_dict = {1: "Rama", 2: "Raju", 3: "Ravi"}
# Define the position at which you want to sort the names (3rd character in this case)
position = 3
# Sort the names based on the character at the specified position
sorted_names = sorted(name_dict.values(), key=lambda x: x[position - 1])
# Print the sorted names
print(sorted_names)
