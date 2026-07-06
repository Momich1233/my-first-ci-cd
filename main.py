def calculate_bonus(salary):
    """Функция считает премию: 10% от зарплаты"""
    return salary * 0.1

if __name__ == "__main__":
    print("🚀 Приложение успешно запустилось внутри Docker-контейнера!")
    my_salary = 150000
    bonus = calculate_bonus(my_salary)
    print(f"💰 При зарплате {my_salary} руб. твоя премия составит: {bonus} руб.")