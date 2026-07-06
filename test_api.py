import requests

def test_create_post_successfully():
    # 1. Arrange (Готовим URL и данные, которые хотим отправить)
    url = "https://jsonplaceholder.typicode.com/posts"
    
    payload = {
        "title": "Мой крутой автотест",
        "body": "Docker и CI/CD уже работают!",
        "userId": 1
    }
    
    # 2. Act (Отправляем POST-запрос на сервер)
    response = requests.post(url, json=payload)
    
    # 3. Assert (Проверяем результаты)
    
    # Сервер при успешном создании объекта должен вернуть статус-код 201 (Created)
    assert response.status_code == 201, f"Неверный статус код: {response.status_code}"
    
    # Парсим ответ от сервера в формат JSON (в Python это станет обычным словарем)
    response_data = response.json()
    
    # Проверяем, что сервер вернул нам те же данные, что мы отправляли
    assert response_data["title"] == payload["title"]
    assert response_data["body"] == payload["body"]
    
    # Проверяем, что сервер присвоил нашему посту уникальный ID
    assert "id" in response_data
    print(f"\n✅ Сервер успешно создал пост с ID: {response_data['id']}")