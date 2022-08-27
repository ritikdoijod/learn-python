def main():
    x = 0

    # define while loop
    while x < 5:
        print(x)
        x += 1

    # define a for loop
    for i in range(5, 10):
        print(i)

    # use a for loop over a collection
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for day in days:
        print(day)

    # use the break and continue statements
    for i in range(1, 10):
        if i == 3:
            break
        print(i)

    for i in range(1, 10):
        if i == 3:
            continue
        print(i)

    # using enumerate() function to get index
    for i, day in enumerate(days):
        print(i, day)


if __name__ == "__main__":
    main()
