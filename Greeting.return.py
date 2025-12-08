# Project 1: Function with Return Value

# Define the function 'get_greeting' which accepts one argument, 'name'.
def get_greeting(name):
    # Use the 'return' statement to send the calculated value (the greeting string)
    # back to the line of code that called this function.
    return f"Hello, {name}!"

# Call the function, and the returned value ("Hello, Cooper!") is stored in the 'message' variable.
message = get_greeting("Cooper")

# Print the final value stored in the 'message' variable.
print(message)