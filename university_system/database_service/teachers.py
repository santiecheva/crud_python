from university_system.database_service.generic_database import GenericDatabase


class TeachersDatabase(GenericDatabase):
    def __init__(self) -> None:
        super().__init__(database_name="teachers")
