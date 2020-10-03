WORDS_PATH = "words.txt"
TEXT_PATH = "text.txt"
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ’"

def clean_word(word):
  """
    String -> String
    produce string with all character deleted despite letters(lower/upper case)
  """
  clear_word = ""
  for char in word:
    if char in letters:
      clear_word += char
  return clear_word

def get_text(text_path):
  """
    File -> List
    consume the text file, sparate it into words using spaces,
    return list with these words separated
  """
  open_file = open(text_path, "r", encoding='UTF-8')
  text_list = []
  for line in open_file:
    if len(line) == 1:
      text_list += line
    else:
      text_list += line.split()
  return text_list

def get_words(words_path):
  """
    File -> List
    consume the text file with words, return list with these words separated
  """
  open_file = open(words_path, "r")
  word_list = []
  for line in open_file:
    word_list += line.split()
  return word_list

def print_text(text):
  """
    File -> Console Input
    require user input for each step, if input insn't q, print a paragraph of
    text, in which all new words colored red, in console
  """
  text_line = ""
  for line in text:
    if line != "\n":
      clear_line = clean_word(line)
      if clear_line.lower() not in get_words(WORDS_PATH):
        for char in line.lower():
            if char in letters:
              text_line += "\33[101m" + char + "\x1b[0m"
            else:
              text_line += char
        text_line += " "
      else:
        text_line += line + " "
    else:
      try:
        print(text_line)
        text_line = ""
        user_input = input("")
        if user_input == "q":
          return 0
      except KeyboardInterrupt:
        return 0


print_text(get_text(TEXT_PATH))
