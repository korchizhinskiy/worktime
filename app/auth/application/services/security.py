import bcrypt


def hash_password(password: bytes) -> bytes:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password, salt)
