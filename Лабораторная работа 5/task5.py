import random
import string


def get_random_password(n: int = 8) -> str:
    return "".join(random.sample(string.ascii_uppercase+string.ascii_lowercase+string.digits, n))


print(get_random_password())
