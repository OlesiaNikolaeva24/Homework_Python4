def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()  # Вызов внутренней функции


# Вызов функции test_function
test_function()

# Попытка вызвать inner_function вне test_function
try:
    inner_function()
except NameError as e:
    print(e)  # Вывод ошибки, так как inner_function не доступна здесь

# inner_function()  # NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
