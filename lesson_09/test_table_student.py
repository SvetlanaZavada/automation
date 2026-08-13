import time


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
