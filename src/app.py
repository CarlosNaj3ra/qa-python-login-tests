def validar_usuario(usuario):
    if len(usuario) < 4:
        raise ValueError("El usuario debe tener al menos 4 caracteres")
    return True


def validar_password(password):
    if len(password) < 6:
        raise ValueError("La contraseña debe tener al menos 6 caracteres")

    if not any(char.isdigit() for char in password):
        raise ValueError("La contraseña debe contener al menos un número")

    return True


def login(usuario, password):
    validar_usuario(usuario)
    validar_password(password)

    return "Login exitoso"