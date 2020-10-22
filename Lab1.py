def main():
    while True:
        try:
            side = float(input("Input the side of an equilateral triangle: "))
            if side <= 0:
                print("Such a triangle doesn't exist")
            else:
                break  # input successful
        except ValueError:  # not a number
            print("Incorrect value!")
    area = 3 ** 0.5 * side ** 2 / 4
    print("The area of the triangle: {:.2f}".format(area))


if __name__ == "__main__":
    main()
