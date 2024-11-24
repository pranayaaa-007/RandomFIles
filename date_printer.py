def main():
    date = input("Enter date in the format mm/dd/yyyy: ")
    output = convert_date(date)
    print(f"Output: {output}")


def convert_date(date):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']

    month, day, year = date.split("/")
    day = int(day)
    year = int(year)

    month_name = months[int(month) - 1]

    return f"{month_name} {day}, {year}"


if __name__ == "__main__":
    main()
