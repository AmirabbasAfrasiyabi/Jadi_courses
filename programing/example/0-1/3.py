def function(text):
    characters = 0
    numbers = 0

    for char in text:
        if char.isalpha():
            characters += 1
        elif char.isdigit():
            numbers += 1

    return {
        "characters": characters,
        "numbers": numbers
    }

result = function(input("enter your text: "))
print(result)