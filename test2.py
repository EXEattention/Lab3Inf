from Informatics_Lab3_Task2 import findVowel

def test1():
    text = "Классное слово – обороноспособность, которое должно идти после слов: трава и молоко."
    expected = ['и', 'идти', 'слов', 'слово', 'трава', 'должно', 'молоко', 'обороноспособность']
    result = findVowel(text)
    assert result == expected, f"Ожидалось {expected}, получено {result}"
    print("Test 1 passed")

def test2():
    text = "дом лес сон вода гора"
    expected = ['дом', 'лес', 'сон']
    result = findVowel(text)
    assert result == expected, f"Ожидалось {expected}, получено {result}"
    print("Test 2 passed")

def test3():
    text = "ааа ббб ввв еёё иии ооо"
    expected = ['ааа', 'иии', 'ооо']
    result = findVowel(text)
    assert result == expected, f"Ожидалось {expected}, получено {result}"
    print("Test 3 passed")

def test4():
    text = "пятьдесят пятьдесят пять"
    expected = ['пять']
    result = findVowel(text)
    assert result == expected, f"Ожидалось {expected}, получено {result}"
    print("Test 4 passed")

def test5():
    text = "окно стол стул парта доска"
    expected = ['окно', 'стол', 'стул', 'парта']
    result = findVowel(text)
    assert result == expected, f"Ожидалось {expected}, получено {result}"
    print("Test 5 passed")

