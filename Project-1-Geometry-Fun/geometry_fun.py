# Starter file

'''
Name:
Date:
Assignment:
Description:
'''

def square(side_length):
    """
    Prints the perimeter and area of a square
    
    Parameters
    ----------
    side_length:int - side length of square
    
    Return
    ------
    None
    """
    perimeter = 4*side_length
    print(f"\tThe perimeter of the square is {perimeter}")

def circle(diameter):
    print("")

def equilateral_triangle(side_length):
    print("")


def main():
    # call your functions here as needed
    user_number = int(input("Enter a number: "))
    square(user_number)
    circle(user_number)
    equilateral_triangle(user_number)
    # example:
    # square(user_number)

# don't change code below this line
if __name__ == '__main__':
    main()
