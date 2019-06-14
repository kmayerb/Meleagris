import numpy as np

def carve(a,b):
    """
    carve a sum

    :param a: int or float
    :param b: int or float
    :return: sum of a and b
    :example: carve(1,3)
    >4
    """
    return(np.sum([a,b]))

def carve3(a,b,c):
    """
    carve a sum of 3 parts

    :param a: int or float
    :param b: int or float
    :param c: int or float
    :return: sum of a and b
    :example: carve(1,3)
    >4
    """
    return(np.sum([a,b,c]))

def main(a,b):
    ab = carve(a,b)
    print(ab)

if __name__ == "__main__":
    main(1,3)