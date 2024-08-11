# Which Function Returns the Larger Number?

# Your function will be passed two functions, f and g, that don't take any parameters.
# Your function has to call them, and return 
# a string which indicates which function returned the larger number.

#     If f returns the larger number, return the string f.
#     If g returns the larger number, return the string g.
#     If the functions return the same number, return the string neither.

# Examples

# which_is_larger(lambda: 5, lambda: 10) ➞ "g"

# which_is_larger(lambda: 25,  lambda: 25) ➞ "neither"

# which_is_larger(lambda: 505050, lambda: 5050) ➞ "f"

def which_is_larger(f, g):
    # Get the return values of the functions
    value_f = f()
    value_g = g()
    
    # Compare the values and return the appropriate result
    if value_f > value_g:
        return "f"
    elif value_g > value_f:
        return "g"
    else:
        return "neither"

# Examples
print(which_is_larger(lambda: 5, lambda: 10))         # ➞ "g"
print(which_is_larger(lambda: 25, lambda: 25))        # ➞ "neither"
print(which_is_larger(lambda: 505050, lambda: 5050))  # ➞ "f"

