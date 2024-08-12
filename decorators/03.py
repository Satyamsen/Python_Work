
def func_debug(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"{func.__name__}: {result}, kwargs: {kwargs}"
    return wrapper

@func_debug
def student(name, standard, school="BPS"):
    return f"student: {name}, standard: {standard}"


print(student("seenu", 12, school="BPS"))
