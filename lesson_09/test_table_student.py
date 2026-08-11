import pytest
import time
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


@pytest.fixture(scope='function')
def db():
    connection_string = "postgresql://postgres:1@localhost:5432/учебный"
    db = StudentTable(connection_string)
    return db


def test_add_student(db):
    unique_suffix = int(time.time() * 1000) % 100000
    user_id = 1000 + unique_suffix

    level = "elementary"
    initial_form = "personal"

    students_before = db.get_all_students()
    count_before = len(students_before)
    db.add_student(user_id, level, initial_form)
    students_after = db.get_all_students()
    count_after = len(students_after)

    assert count_after - count_before == 1

    found = False
    for student in students_after:
        if student["user_id"] == user_id:
            found = True
            assert student["level"] == level
            break

    assert found, "Студент не найден в базе данных"

    db.delete_student(user_id)

    assert not db.student_exists(user_id), "Студент должен быть удален"
    students_final = db.get_all_students()
    assert len(students_final) == count_before, \
        "Количество студентов не вернулось к исходному"


def test_update_student(db):
    unique_suffix = int(time.time() * 1000) % 100000
    user_id = 2000 + unique_suffix

    initial_level = "elementary"
    initial_form = "personal"

    students_before = db.get_all_students()
    count_before = len(students_before)

    db.add_student(user_id, initial_level, initial_form)

    assert db.student_exists(user_id), "Студент не был создан"

    new_level = "Master"
    new_form = "personal now"

    db.update_student(user_id, new_level, new_form)
    updated_student = db.get_student_by_id(user_id)

    assert updated_student is not None
    assert updated_student["level"] == new_level
    assert updated_student["education_form"] == new_form

    db.delete_student(user_id)

    assert not db.student_exists(user_id), "Студент должен быть удален"
    students_final = db.get_all_students()
    assert len(students_final) == count_before, \
        "Количество студентов не вернулось к исходному"


def test_delete_student(db):
    unique_suffix = int(time.time() * 1000) % 100000
    user_id = 3000 + unique_suffix

    level = "elementary"
    education_form = "personal"

    students_before = db.get_all_students()
    count_before = len(students_before)

    db.add_student(user_id, level, education_form)
    assert db.student_exists(user_id), "Студент не был создан"

    db.delete_student(user_id)
    assert not db.student_exists(user_id), "Студент должен быть удален"
    students_final = db.get_all_students()
    assert len(students_final) == count_before, \
        "Количество студентов не вернулось к исходному"

    found = False
    for student in students_final:
        if student["user_id"] == user_id:
            found = True
            break
    assert not found, "Студент найден в списке после удаления"
