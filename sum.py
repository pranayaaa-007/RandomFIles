def main():
    numbers = input("Enter a series of single-digit numbers: ")

    total = 0
    for number in numbers:
        total += int(number)

    print(f"The total is: {total}")


if __name__ == "__main__":
    main()
