# let's try mario again

while True:
    try:
        height = int(input("Height:"))
        if height >= 1 and height <= 8:
            break
    except ValueError:
        continue

# starting with the number of levels
for i in range(height):
    # loop for the indent from starting point
    for s in range(height-(i+1)):
        print(" ", end="")
    # loop for the '#' on the left
    for m in range(i+1):
        print("#", end="")
    print("  ", end="")
    # loop for the '#' on the right
    for k in range(i+1):
        print("#", end="")
    print()






