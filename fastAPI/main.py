import json
import logging
import time
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pydantic
import uvicorn

# Виправлено: параметр timefmt замінено на правильний datefmt
logging.basicConfig(
    level=logging.INFO,
    datefmt="%d/%m/%Y %H:%M:%S",
    format="%(asctime)s - %(levelname)s - %(message)s",
)

app = FastAPI()

text_hello_world = "Hello world!"


# FastAPI автоматично конвертує словники (dict) у JSON, 
# тому краще повертати dict або Response об'єкт, а не сирий str.
@app.get(
    path="/",
    tags=["Тестовая страница"],
    summary="Тестовая страница",
    description="Тестовая страница",
)
def root():
    logging.info("запуск главного root")
    return create_data_for_send()


@app.get(
    path="/hello",
    tags=["Тестовая страница"],
    summary="Тестовая страница",
    description="Тестовая страница",
)
def hello():
    logging.info("запуск главного hello")
    return create_data_for_send()


def create_data_for_send() -> dict:
    # Повертаємо звичайний словник. FastAPI сам серіалізує його в JSON 
    # та виставить правильний заголовок Content-Type: application/json
    return {"message": text_hello_world}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",  # Переконайтеся, що цей файл називається саме main.py
        host="127.0.0.1",
        port=8000,
        reload=True,
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