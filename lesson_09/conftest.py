import pytest
from student_table import StudentTable  # Импортируем ваш класс


@pytest.fixture(scope='function')
def db():
    connection_string = "postgresql://postgres:1@localhost:5432/учебный"
    db = StudentTable(connection_string)
    return db