import os

# Путь к файлу с кодом
code_file_path = 'code.pialn'

# Проверка существования файла с кодом
if not os.path.exists(code_file_path):
    print("ERROR:1")
    exit()

# Чтение содержимого файла
with open(code_file_path, 'r', encoding='utf-8') as file:
    python_code = file.read()

# Проверка, что содержимое файла не пустое
if not python_code.strip():
    print("ERROR:2")
    exit()

# Выполнение кода Python из файла внутри лаунчера
try:
    exec(python_code)
except Exception as e:
    print(f"ERROR:{e}")
