# Project 2: Local vs Global Scope

# This variable is defined outside any function, making it a GLOBAL variable.
score = 10
print(f"Score before function call: {score}")

# Define the function 'increase_score'.
def increase_score():
    # The 'global' keyword explicitly tells Python that we intend to modify 
    # the existing 'score' variable in the global scope, not create a new local one.
    global score
    
    # Modify the global 'score' variable.
    score += 5
    print(f"Score inside function: {score}")

# Call the function, which executes the modification.
increase_score()

# The global 'score' value has been permanently updated by the function.
print(f"Score after function call: {score}")


