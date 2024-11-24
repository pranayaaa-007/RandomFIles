def main():
    full_name = input("Enter the person's first, middle, and last name: ").strip().title()
    output = get_initials(full_name)
    print(f"Initials: {output}")


def get_initials(full_name):
    first_name, middle_name, last_name = full_name.split(" ")
    return f"{first_name[0]}. {middle_name[0]}. {last_name[0]}."


if __name__ == "__main__":
    main()
