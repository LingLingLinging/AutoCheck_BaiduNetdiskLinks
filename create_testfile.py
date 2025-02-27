import os
import random
import string

size = int(input("Create a file of size (MB): "))
filename = f'random_{size}MB.txt'

def generate_random_file(file_path, size_in_mb):
    size_in_bytes = size_in_mb * 1024 * 1024
    with open(file_path, 'w', encoding='utf-8') as file:
        while os.path.getsize(file_path) < size_in_bytes:
            random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=1024))
            file.write(random_string)

generate_random_file(filename, size)