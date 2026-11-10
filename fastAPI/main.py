from fastapi import FastAPI
import pydantic
import uvicorn
import logging
import json
import time
logging.basicConfig(level=logging.INFO, timefmt="[%d/%m/%Y %H:%M:%S]", format="%(asctime)s - %(levelname)s - %(message)s") # type: ignore
app = FastAPI()
text_hello_world = str("Hello world!")
@app.get(path="/", tags=["Тестовая страница"], summary="Тестовая страница", description="Тестовая страница")
def root() -> str:
    logging.info('запуск главного root')
    return create_data_for_send()
@app.get(path="/hello", tags=["Тестовая страница"], summary="Тестовая страница", description="Тестовая страница")
def hello() -> str:
    logging.info('запуск главного hello')
    return create_data_for_send()
def create_data_for_send():
    data = {
        "message": text_hello_world
    }
    return json.dumps(data)
if __name__ == "__main__":
    
    uvicorn.run(
        "main:app",  # Ім'я файлу (без .py) та ім'я змінної додатка
        host="127.0.0.1",  # IP-адреса для запуску
        port=8000,  # Порт
        reload=True,  # Автоматичне перезавантаження при зміні коду
    )


# number1 = int(10)
# number2 = str('20')

# number1_value_type = isinstance(number1, int)
# number2_value_type = isinstance(number2, str)

# if number1_value_type:
#     print(f"number1 is of type: {type(number1)}")
# if number2_value_type:
#     print(f"number2 is of type: {type(number2)}")

# print(f"Type of number1_value_type: {type(number1_value_type)}")

# print(type(number1_value_type))
# print(type(number2_value_type))