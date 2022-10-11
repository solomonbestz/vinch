

def function(input):
    return tuple(input.split(","))


if __name__=="__main__":
    first, second = function(input("Input Boundary: "))
    print(f"({first}, {second})")

