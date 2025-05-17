import pytest
from registration.registration import add_user, initialize_users


def test_add_new_user():
    users = initialize_users()
    result = add_user(users, "new_user", "new_password")
    assert result == "Новый пользователь new_user успешно добавлен."
    assert "new_user" in users
    assert users["new_user"] == "new_password"


def test_add_existing_user():
    users = initialize_users()
    result = add_user(users, "user1", "password1")
    assert result == "Пользователь с таким логином уже существует."
    assert users["user1"] == "password1"

def add_user(users, username, password):
    """Добавляет нового пользователя, если его еще нет в словаре.
    Возвращает сообщение о результате операции."""
    if username in users:
        return "Пользователь с таким логином уже существует."
    users[username] = password
    return f"Новый пользователь {username} успешно добавлен."