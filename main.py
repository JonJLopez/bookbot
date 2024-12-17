def main():
    path_to_file = "./books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()
    
    word_count = count_words(file_contents)

    character_count = count_characters(file_contents)
    print(f"Word count is: {word_count}")
    print(character_count)

#counts word in a file
def count_words(file):
    return len(file.split()) # return the length of the list of words

#takes a file and returns a dictionary with count of all 
def count_characters(file):
    character_count = {}
    for s in file.lower():
        #if character is whitespace do nothing
        if s in " \n":
            continue
        #if character is not in dictionary add it
        if s not in character_count:
            character_count[s] = 0
        #increase count of character by one
        character_count[s] += 1
    
    return character_count

main()