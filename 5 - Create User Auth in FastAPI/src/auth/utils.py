from passlib.context import CryptContext

# Use Argon2 for password hashing. Argon2 is a modern, secure algorithm
# and it avoids bcrypt's 72-byte limit and backend compatibility issues.
passwd_context = CryptContext(
    schemes=['argon2'],
    deprecated='auto'
)

def generate_passwd_hash(password: str) -> str:
    return passwd_context.hash(password)

def verify_password(password: str, hash: str) -> bool:
    return passwd_context.verify(password, hash)