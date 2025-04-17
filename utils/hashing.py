import bcrypt


# hash the password
def hash_password(password: str) -> str:
    """Hashing the password and returning it"""
    hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hash.decode()  # decode to string


# verify if the hash matches
def verify_password(password: str, hashed_password: str) -> bool:
    """match the password with hashed password by unhashing it"""
    return bcrypt.checkpw(password.encode(), hashed_password.encode())  # match password
