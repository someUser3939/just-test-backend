from fastapi import FastAPI


app = FastAPI()

@app.get(path="/", tags=["Тестовая страница"], summary="Тестовая страница", description="Тестовая страница")
def root():
    return {"Hello, World!"}


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