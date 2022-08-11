from university_system.database_service.generic_database import GenericDatabase


class StudentsDatabase(GenericDatabase):
    def __init__(self) -> None:
        super().__init__(database_name="students")
