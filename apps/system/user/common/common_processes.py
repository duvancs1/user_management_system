import hashlib


def sanitize_and_hash_email(email: str) -> str:
    # Trim leading and trailing whitespace, and convert to lowercase
    sanitized_email = email.strip().lower()

    # Hash the final string using SHA256
    hashed_email = hashlib.sha256(sanitized_email.encode()).hexdigest()

    return hashed_email
