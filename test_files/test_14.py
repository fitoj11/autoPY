# print("Let's count together: {}, then goes {}, and then {}".format("one", "two", "three")) # подставляет вместо [] значения из .format("первое","второе","третье")

# str1 = "1"
# str2 = "2"
# str3 = "3"
# print(f"Let's count together: {str1}, then goes {str2}, and then {str3}") # аналогично .format, только через переменные. !ВАЖНО, перед текстом "f"

expected_result = "1", "2"
actual_result = "3", "4"
def test_input_text(expected_result, actual_result): # моя функция ничего не делает, в задании скрыто описание функционала этой функции
    assert expected_result == actual_result, "test"
print(test_input_text)

def test_input_text(expected_result, actual_result):
        assert expected_result == actual_result, \
            f"expected {expected_result}, got {actual_result}"

s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')

def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number" 

if __name__ == "__main__":
    test_abs1()
    print("All tests passed!")

def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"

if __name__ == "__main__":
    test_abs1()
    test_abs2()
    print("Everything passed")

# catalog_text = self.catalog_link.text # считываем текст и записываем его в переменную
# assert catalog_text == "Каталог", \
#     f"Wrong language, got {catalog_text} instead of 'Каталог'"  

# assert abs(-42) == -42, "test error msg" # через запятую - описание ошибки
