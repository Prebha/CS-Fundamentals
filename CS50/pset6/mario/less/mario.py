# Taking user input
# python 3.x doesn't evaluate and convert data type so adding int explicitly

while True:
    try:
        height = int(input("Height: "))
        if height >= 1:
            break
    except ValueError:
        print ("Please enter a number greater than 0")

for i in range(1, height+1):
    for j in range(height-i):
        print(" ", end="")
    for k in range(i):
        print("#", end="")
    print("\n", end="")
