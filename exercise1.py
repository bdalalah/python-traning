# exercise1.py

# Define the file name
file_name = 'numbers.txt'

# Open the file in write mode ('w')
with open(file_name, 'w') as file:
    # Write numbers from 1 to 10, each on a new line
    for number in range(1, 11):
        file.write(f"{number}\n")

print(f"Numbers from 1 to 10 have been written to '{file_name}'.")