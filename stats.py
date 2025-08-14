def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    number_of_characters = {}
    for letter in text:
        if letter.isalpha():
            letter = letter.lower()
            if letter in number_of_characters:
                number_of_characters[letter] += 1
            else:
                number_of_characters[letter] = 1
    return number_of_characters

def list_of_counts(diction):
    list_dictionary = []
    current_dict = {}
    for key, value in diction.items():
        current_dict['char'] = key
        current_dict['count'] = value
        list_dictionary.append(current_dict)
        current_dict = {}
    def sort_by_count(item):
        return item['count']
    list_dictionary.sort(key=sort_by_count, reverse=True)
    return list_dictionary

def stats_printer(listed_dictionary):
    for dict in listed_dictionary:
        print(f'{dict['char']}: {dict['count']}')
    


         
    
