user_text = input("Text: ")

def readability(user_text):
    letter_count = 0
    sentence_count = 0
    word_count = 1

    for char in user_text:
        if char.isalpha():
            letter_count += 1
        if char in ".!?":
            sentence_count += 1
        if char == " ":
            word_count += 1

    avg_l = (letter_count / word_count) * 100
    avg_s = (sentence_count / word_count) * 100

    index = 0.0588 * avg_l - 0.296 * avg_s - 15.8
    rounded_index = round(index)


    if rounded_index < 1:
        return "Before Grade 1"
    elif rounded_index >= 16:
        return "Grade 16+"
    else:
        return f"Grade {rounded_index}"

print(readability(user_text))
