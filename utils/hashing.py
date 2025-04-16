import bcrypt


def hash_password(password: str) -> str:
    """Hashing the password and returning it"""
    hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hash.decode()  # salt round 12 by default


def verify_password(password: str, hashed_password: str) -> bool:
    """match the password with hashed password by unhashing it"""
    return bcrypt.checkpw(password.encode(), hashed_password.encode()) # match password









