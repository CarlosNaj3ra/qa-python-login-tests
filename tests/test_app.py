import pytest
from src.app import validar_usuario, validar_password, login


def test_usuario_invalido():
    with pytest.raises(ValueError):
        validar_usuario("abc")


def test_password_sin_numero():
    with pytest.raises(ValueError):
        validar_password("abcdef")


def test_login_exitoso():
    resultado = login("carlos", "abc123")
    assert resultado == "Login exitoso"