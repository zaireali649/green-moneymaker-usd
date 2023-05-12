import random
import uuid
import os

def generate_file(name: str = None, size: int = random.randint(1, 10)) -> None:
    """
    Generate a file with the given name and size.

    Args:
        name (str, optional): The name of the file. If not provided, a random name will be generated.
        size (int, optional): The size of the file in bytes. If not provided, a random size between 1 and 10 will be used.
    """
    if name is None:
        name = str(uuid.uuid4())[:8] + ".dummy"
    with open(name, 'wb') as fout:
        fout.write(os.urandom(size))
    fout.close()
