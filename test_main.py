from main import calculate_bonus

def test_correct_bonus_calculation():
    # Проверяем: от 100 000 премия должна быть ровно 10 000
    assert calculate_bonus(100000) == 100000

def test_zero_salary_bonus():
    # Проверяем: если зарплата 0, то и премия 0
    assert calculate_bonus(0) == 0