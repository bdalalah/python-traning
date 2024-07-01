# exercise2.py

# Define the file name
file_name = 'user_input.txt'

# Open the file in append mode ('a+')
with open(file_name, 'a+') as file:
    while True:
        user_input = input("Enter some text (enter 'stop' to quit): ")
        if user_input.lower() == 'stop':
            break
        file.write(user_input + "\n")

print(f"User input has been appended to '{file_name}'.")