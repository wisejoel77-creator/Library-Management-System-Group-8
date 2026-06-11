def require_login(func):
    def wrapper(*args, **kwargs):
        print("Checking authentication...")
        return func(*args, **kwargs)
    return wrapper