from sqlalchemy import create_engine
from sqlalchemy.sql import text


class StudentTable:

    __scripts = {
        # Получить всех студентов
        "select all": text("SELECT * FROM student"),

        # Получить студента по user_id
        "select by user_id": text(
            "SELECT * FROM student WHERE user_id = :user_id"),

        # Добавить студента
        "insert": text("""
            INSERT INTO student (user_id, level)
            VALUES (:user_id, :level)
        """),

        # Обновить данные студента
        "update": text("""
            UPDATE student SET level = :level, education_form = :education_form
            WHERE user_id = :user_id"""),

        # Удалить студента
        "delete": text("DELETE FROM student WHERE user_id = :user_id"),

        # Проверить существование студента
        "exists": text("SELECT EXISTS ("
                       " SELECT 1 FROM student WHERE user_id = :user_id)")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_all_students(self):
        return self.__db.execute(self.__scripts["select all"]).fetchall()

    def get_student_by_id(self, user_id):
        return self.__db.execute(
            self.__scripts["select by user_id"],
            {"user_id": user_id}
        ).fetchone()

    def add_student(self, user_id, level, initial_form):
        self.__db.execute(
            self.__scripts["insert"],
            {
                "user_id": user_id,
                "level": level,
                "education_form": initial_form
            }
        )

    def update_student(self, user_id, new_level, new_education_form):
        self.__db.execute(
            self.__scripts["update"],
            {
                "user_id": user_id,
                "level": new_level,
                "education_form": new_education_form
            }
        )

    def delete_student(self, user_id):
        self.__db.execute(
            self.__scripts["delete"],
            {"user_id": user_id}
        )

    def student_exists(self, user_id):
        """Проверить, существует ли студент"""
        result = self.__db.execute(
            self.__scripts["exists"],
            {"user_id": user_id}
        ).scalar()
        return result
