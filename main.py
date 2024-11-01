def main():
    file_contents = get_text("books/frankenstein.txt")
    #print(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words_count(file_contents)} words found in the document")
    #print(count_characters(file_contents))
    print_list_of_characters(count_characters(file_contents))
    print("--- End report ---")
def get_text(path):
    with open(path) as f:
        return f.read()
def words_count(text):
    words = text.split()
    return len(words)
def count_characters(text):
    text = text.lower()
    count = {}
    for char in text:
        if char.isalpha():
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
    return count
def print_list_of_characters(count):
    for key in count:
        print(f"The '{key}' character was found {count[key]} times")
main()
