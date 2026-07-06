import requests
import pytest  # Импортируем сам pytest для доступа к декораторам

# Вешаем декоратор параметризации. 
# Первый аргумент — имя переменной, которая будет меняться.
# Второй аргумент — список значений, которые будут подставляться по очереди.
@pytest.mark.parametrize("user_id", [1, 2, 5, 10])
def test_get_different_users(user_id):
    # Переменная {user_id} подставится в строку динамически
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    
    response = requests.get(url)
    
    # Проверяем, что сервер на все эти ID отвечает успешным кодом 200
    assert response.status_code == 200
    
    response_data = response.json()
    # Проверяем, что сервер вернул данные именно того юзера, которого мы просили
    assert response_data["id"] == user_id
    print(f"\n👤 Успешно проверили пользователя с ID: {user_id}, его имя: {response_data['name']}")