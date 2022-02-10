words = {
    "mouse": 2,
    "difficult": 7,
    "surprise": 7,
}
results = {}
question_index = 1
is_username_correct = False
while not is_username_correct:
    print("Привет введите пожалуйста ваше имя")
    print("Оно должно быть без пробелов и цифр")
    user_input = input()

    user_input_has_digits = False

    user_input_has_spaces = " " in user_input
    for symbol in user_input:
        if symbol.isdigit():
            user_input_has_digits = True

    if (not user_input_has_spaces) and (not user_input_has_digits):
        is_username_correct = True
        user_name = user_input

for word, index in words.items():

    secret = list(word)
    secret_letter = secret[index - 1]
    secret[index - 1] = "*"
    secret_word = "".join(secret)
    print(f"Вставте букву в слове {secret_word}")

    user_input = input()
    if user_input == secret_letter:
        print('Ответ верный')
        results[question_index] = True
    else:
        print(f"Ответ неверный, верный ответ {word}")
        results[question_index] = False
    question_index += 1

print(results)
print(f"Вот и все {user_name}")
index = 1
for word in words.keys():
    print(f"{index} {word} {results[index]}")
    index += 1