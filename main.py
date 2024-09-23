def main():
    print_report("books/frankenstein.txt")

def get_book_path(path):
    with open(path) as f:
              return f.read()
    
def get_num_words(text):
       text_list = text.split()
       return len(text_list)

def get_num_chars(text):
      text = text.lower()
      char_dict = {}
      for char in text:
         if char in char_dict:
               char_dict[char] += 1
         else:
               char_dict[char] = 1
      return char_dict

def sort_on(dict):
            return dict["occurences"]

def print_report(file_path):
      text = get_book_path(file_path)
      num_words = get_num_words(text)
      char_dict = get_num_chars(text)
      print(f"--- Begin report of {file_path} ---")
      print(f"{num_words} words found in the document")
      print()

      # Create a list of dictonaries
      char_dict_list = []
      for char in char_dict:
            char_dict_list.append({"letter": char, "occurences":char_dict[char]})
      char_dict_list.sort(reverse=True, key=sort_on)

      # Print individual letter stats
      for dict in char_dict_list:
            if dict["letter"].isalpha():
                print(f"The '{dict['letter']}' was found {dict['occurences']} times")
      print("--- End report ---")

      

main()
