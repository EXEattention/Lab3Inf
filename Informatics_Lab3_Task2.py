 # Author = Kiyashko Alexander Maksimovich
 # Group = P3118
 # Date = 10.11.2025
import re

def findVowel(text):
    words = re.findall(r'\b[а-яё]+\b', text, re.IGNORECASE)
    
    result = []
    for word in words:
        word_lower = word.lower()
        vowels = re.findall(r'[аеёиоуыэюя]', word_lower)

        if vowels and len(set(vowels)) == 1:
            result.append(word_lower)
    
    result.sort(key=lambda x: (len(x), x))
    
    return result

text = "Классное слово – обороноспособность, которое должно идти после слов: трава и молоко."
result = findVowel(text)
for word in result:
    print(word)