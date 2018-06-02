def set_range(a, b, c):
    x = max (a, b, c)
    y = min (a, b, c)
    z = x - y
    return z
    
print set_range(10,4,7)