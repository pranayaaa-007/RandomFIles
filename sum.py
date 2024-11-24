def main():
    digits = input("Enter a series of single-digit numbers: ")

    total = sum(int(digit) for digit in digits)

    print(f"Sum: {total}")


if __name__ == "__main__":
    main()
