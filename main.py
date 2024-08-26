
def main():
    with open("books/frankenstein.txt") as f:
        text = f.read()

    word_count = count_words(text)

    letter_index = count_chars(text)
    sorted_frequency = sort_frequency(letter_index)
    print("Letters by frequency:")

    for position in sorted_frequency:
        print(f" {position['letter']} - {position['count']}")


def count_words(text):
    words = text.split()
    return len(words)


def count_chars(text):
    lower_text = text.lower()
    letter_index = {}

    for letter in lower_text:
        if not letter.isalpha():
            continue
        elif letter in letter_index:
            letter_index[letter] += 1
        else:
            letter_index[letter] = 1
    return letter_index


def sort_frequency(letter_index):
    listed = []

    for letter, count in letter_index.items():
        listed.append({"count": count, "letter": letter})

    listed.sort(key=lambda x: x["count"], reverse=True)

    return listed


main()
