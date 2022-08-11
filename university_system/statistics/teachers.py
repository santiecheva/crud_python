def get_mean_salary(database) -> float:
    data = database.get_all_data()

    mean = 0
    for teacher_data in data.values():
        mean += teacher_data["salary"]

    return mean / database.count()


def get_teachers_metrics(database):
    print("=" * 80)
    print(f"Mean Salary: {get_mean_salary(database)}")
