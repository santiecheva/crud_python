def get_age_mean(database) -> float:
    data = database.get_all_data()

    mean = 0
    for student_data in data.values():
        mean += student_data["age"]

    return mean / database.count()


def get_semester_mean(database) -> float:
    data = database.get_all_data()

    mean = 0
    for student_data in data.values():
        mean += student_data["semester"]

    return mean / database.count()


def get_differents_letter_mean(database) -> float:
    data = database.get_all_data()

    mean = 0
    for student_data in data.values():
        lower_name = student_data["first_name"].lower()
        differents_letter = set(lower_name)
        mean += len(differents_letter)

    return mean / database.count()


def get_students_metrics(database) -> None:
    print("=" * 80)
    print(f"Age mean: {get_age_mean(database)}")
    print(f"Semester mean: {get_semester_mean(database)}")
    print(f"Differents letters mean: {get_differents_letter_mean(database)}")
    print(f"Students count: {database.count()}")