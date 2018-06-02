def set_range(a, b, c):            # Defining Procedure which accepts 3 numerical inputs
    x = max (a, b, c)              # Variable X will initialise "max()" ,i.e, built-in function - looks for Greater value in (a, b, c)
    y = min (a, b, c)              # Variable Y will initialise "min()" ,i.e, built-in function - looks for Smaller value in (a, b, c)
    z = x - y                      # Variable Z will store value of Greater value from X minus Smaller value from Y
    return z                       # Return Z
    
print set_range(10,4,7)            # Print set_range by passing value as per your Preference

# CODED BY - GAURAV PADAWE
