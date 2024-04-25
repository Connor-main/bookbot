def main():
    book_path = "books/Frakenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letter = get_num_letters(text)
    sorted_letter = get_sorted_list(num_letter)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for l in sorted_letter:
        print(f'The {l["name"]} charachter was found {l["num"]} times')
    print("--- End report ---")
   

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_letters(text):
    lower_text = text.lower()
    letter_dict = {}
    for i in range(0, len(text)):
        if lower_text[i] in letter_dict.keys():
            letter_dict[lower_text[i]] += 1
        else:
            letter_dict[lower_text[i]] = 1
    return letter_dict

def sort_on(dict):
    return dict["num"]

def get_sorted_list(dict):    
    lst = [] 
    for c in dict:
        if c.isalpha():
            lst.append({"name":c,"num":dict[c]})
    lst.sort(reverse=True, key=sort_on)        
    return lst
    


main()
          
