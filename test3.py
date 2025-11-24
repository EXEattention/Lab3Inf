import pytest
from Informatics_Lab3_Task3 import check_password

def test_valid_password():
    """Тест 1: Валидный пароль, удовлетворяющий всем правилам"""
    password = "March988!ABC"
    errors = check_password(password)
    assert len(errors) == 0, f"Unexpected errors: {errors}"

def test_short_password():
    """Тест 2: Слишком короткий пароль"""
    password = "A1!"
    errors = check_password(password)
    assert any("Rule 1" in err for err in errors)

def test_no_uppercase():
    """Тест 3: Пароль без заглавных букв"""
    password = "december988!abc"
    errors = check_password(password)
    assert any("Rule 3" in err for err in errors)

def test_wrong_digit_sum():
    """Тест 4: Сумма цифр не равна 25"""
    password = "January123!ABC"
    errors = check_password(password)
    assert any("Rule 5" in err for err in errors)

def test_no_month():
    """Тест 5: Пароль без названия месяца"""
    password = "Password988!ABC"
    errors = check_password(password)
    assert any("Rule 6" in err for err in errors)

