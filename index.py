def main():
    while True:
        print("\nTianyuan Academy of Magic - Student Management System")
        print("1. Add Student")
        print("2. List Students")
        print("3. Show Student's Courses")
        print("4. Show Magical Items Needed")
        print("5. Exit")
        choice = input("\nEnter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            print()
            list_students()
        elif choice == '3':
            show_student_courses()
        elif choice == '4':
            show_magical_items()
        elif choice == '5':
            print("\nExiting the program[!]")
            break
        else:
            print("\nInvalid Selection[!]\nPlease select from (1-5).")

class Student:
    def __init__(self, name, student_id, house, courses):
        self.name = name
        self.student_id = student_id
        self.house = house
        self.courses = courses

    def __str__(self):
        return f"Name: {self.name},    ID: {self.student_id},     House: {self.house},    Courses: {', '.join(self.courses)}"

# Courses and their required magical items
courses_magical_items = {
    "Magical History": ["MH Textbook", "Coffee"],
    "Potions": ["Cauldron", "Mortar and Pestle", "Vials", "Magical Ingredients"],
    "Defensive Magic": ["Wand", "Staff", "Wards", "Potion of Recovery"],
    "Magical Beasts": ["Heavy Leather Gloves", "Heavy Apron", "Staff"],
    "Human Studies": ["Laptop", "Smartphone"],
    "Astronomy": ["Telescope", "Orrery"],
    "Herbology": ["Shears", "Clay Pots"],
    "Divination": ["Tea", "Tarot Cards", "Magical Ingredients"],
    "Cosmology": ["C Textbook", "Talismans"],
    "Transfiguration": ["Wand", "Magical Ingredients"],
    "Evocation": ["Staff", "Healing Potion", "Conduit", "Wards"],
    "Illusion": ["Cloak", "Charms"],
    "Enchantments": ["Wand", "Staff", "Magical Ingredients"],
    "Conjuration": ["Wand", "Conduit"],
}

students = []

# Adds a new student asking for their name, ID, house and courses
def add_student():
    name = input("\nEnter student name: ").title().strip()

    # Checks if a student ID already exists
    while True:
        student_id = input("Enter student ID: ").strip()
        if any(student.student_id == student_id for student in students):
            print(f"\nA student with ID {student_id} already exists[!]\nPlease enter a unique student ID.\n")
        else:
            break

    houses = ["Dragon", "Phoenix", "Tiger", "Fox"]
    house = input("Enter student house (Dragon, Phoenix, Tiger, Fox): ").title().strip()
    # Ensures proper house is allocated
    while house not in houses:
        print("\nInvalid house[!]\nPlease select (Dragon, Phoenix, Tiger, Fox).")
        house = input("\nEnter student house (Dragon, Phoenix, Tiger, Fox): ").title().strip()

    print("\nAvailable courses:")
    for i, course in enumerate(courses_magical_items.keys(), 1):
        print(f"\t{i}. {course}")
    # Terminates the process of adding a new student if there is any error while selecting the courses
    while True:
        try:
            selected_courses = input("\nEnter the course numbers separated by commas (max 7): ").split(',')
            if len(selected_courses) > 7:
                print("\nStudents can only enroll in up to 7 courses[!]\nProcess of adding a new student terminated[!]")
                return
            courses = [list(courses_magical_items.keys())[int(c) - 1] for c in selected_courses]
            students.append(Student(name, student_id, house, courses))
            break
        except (ValueError, IndexError):
            print("\nInvalid selection[!]\nPlease choose from (1 - 14)")
    print(f"\nA new student {name} is successfully added.")

# Lists the students along with their information
def list_students():
    if not students:
        print("No students enrolled yet[!]")
        return
    for student in students:
        print(student)

# Displays the student's courses
def show_student_courses():
    student_id = input("\nEnter student ID: ")
    student = next((s for s in students if s.student_id == student_id), None)

    if student:
        print(f"\nCourses for {student.name}: {', '.join(student.courses)}")
    else:
        print(f"\nStudent with the id {student_id} was not found[!]")

# Shows the magical items needed for the student
def show_magical_items():
    student_id = input("\nEnter student ID: ")
    student = next((s for s in students if s.student_id == student_id), None)

    if student:
        print(f"\nMagical items needed for {student.name}:")
        for course in student.courses:
            items = courses_magical_items.get(course, [])
            print(f"\t{course}: {', '.join(items)}")
    else:
        print(f"\nStudent with the id {student_id} was not found[!]")

if __name__ == "__main__":
    main()