"""
COMP.CS.100
Tekijä: Patrick Selin
Opiskelunumero: tuni.fi:151435647
Tehtävä: 8.4
"""

"""
This function prints the price of a product that user ask.
:param no params
:return: prints the result
"""

def print_box(width, height, mark):
    """Prints a square using three parameters. First is the width of the
    square, second is the desired height and lat is the mark used to print
    the square."""
    print()
    for i in range(height):
        print(f"{width * mark}")

def read_input(promt):
    """Reads the promt and checks if it is positive number.
     Ask so many times as needed and then it returns it. It also
     checks with try-except if the width and height inputs are
     integers."""
    flag = True

    while flag:
        try:
            x = int(input(f"{promt}"))
            if x > 0:
                return x

        except ValueError:
            flag = True

def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")

    mark = input("Enter a print mark: ")
    print_box(width, height, mark)

if __name__ == "__main__":
    main()
