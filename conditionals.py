#
# Example file for working with conditional statements
# LinkedIn Learning Python course by Joe Marini
#


def main():
    x, y = 10, 100

    # conditional flow uses if, elif, else
    if x < y:
        print("x is less than y")
    elif x == y:
        print("x is equal to y")
    else:
        print("x is greater than y")

    # conditional statements let you use "a if C else b"
    result = "x is less than y" if (x < y) else "x is greater than or equal to y"
    print(result)

    # match-case makes it easy to compare multiple values
    value = "three"

    match value:
        case "one":
            print(1)
        case "two":
            print(2)
        case "three" | "four":
            print(3, 4)
        case _:
            print(-1)


if __name__ == "__main__":
    main()
