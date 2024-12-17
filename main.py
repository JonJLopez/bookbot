def main():
    path_to_file = "./books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()
    
    word_count = count_words(file_contents)
    print(f"Word count is: {word_count}")

#counts word in a file
def count_words(file):
    return len(file.split()) # return the length of the list of words


main()