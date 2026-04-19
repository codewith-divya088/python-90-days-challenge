# Area calculations
def area_rectangle(l, b):
    return l * b

def area_cube(a):
    return 6 * a * a

def area_cuboid(l, b, h):
    return 2 * (l*b + b*h + h*l)

# Volume calculations
def volume_cube(a):
    return a ** 3

def volume_cuboid(l, b, h):
    return l * b * h

def volume_cylinder(r, h):
    return 3.14 * r * r * h

# Sample outputs
print("Area of Rectangle:", area_rectangle(5, 4))
print("Volume of Cube:", volume_cube(3))
print("Volume of Cylinder:", volume_cylinder(2, 5))
