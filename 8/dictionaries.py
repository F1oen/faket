from collections import Counter
def read_text_file(filename):
    try:
        with open(filename,"r") as file:
            text = file.read()
            words = text.lower().split()
            return words
    except FileNotFoundError:
        print(f"File{filename} not found")
        return []
def count_word_frequency(words):
    word_count = Counter(words)
    return word_count
def print_top_words(words_count,n=5):
    most_common = words_count.most_common(n)
    print(f"{'Words':<15}{'Frequency'}")
    print("-", * 25)
    for word, count in most_common:
        print(f"{word:<15}{count}")

def main():
    input_file="textfile.txt"
    words = read_text_file(input_file)
    if not words:
        return
    word_count = count_word_frequency(words)
    print_top_words(word_count)

    