def main():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()
    
    word_count = count_words(file_contents)

    character_count = count_characters(file_contents)
    sorted_character_count = sort_dict(character_count)

    print("---- Report for {path_to_file} ----")
    print_report(word_count, sorted_character_count)
    print("---- End of Report ----")

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

#sorts a dictionary in descending order by their values
def sort_dict(unsorted_dict):
    return {k: v for k, v in sorted(unsorted_dict.items(), key=lambda item: item[1], reverse=True)}

def print_report(word_count, character_count):
    print(f"{word_count} words in the file\n")
    for k in character_count:
        print(f"The \'{k}\' character was found {character_count[k]} times")

main()