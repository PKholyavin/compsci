HANGMANPICS = [r'''
       
      |
      |
      |
      |
      |
=========''',r'''
  +---+
      |
      |
      |
      |
      |
=========''',r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


word = "информатика"
open_letters = [word[0], word[-1]]

def print_word():
    blanked_word = ""
    for a in word:
        if a in open_letters:
            blanked_word += a
        else:
            blanked_word += "-"
    print(blanked_word)
    return blanked_word

print_word()

wrong_attempts = 0

while True:
    letter = input("Введите букву: ").lower()
    if letter in open_letters:
        print("Эта буква уже открыта!")
    elif letter in word:
        print("Угадал!")
        open_letters.append(letter)
        blanked_word = print_word()
        if blanked_word == word:
            print("Вы выиграли!")
            break
    else:
        print("Такой буквы нет!")
        print(HANGMANPICS[wrong_attempts])
        wrong_attempts += 1
        if wrong_attempts == len(HANGMANPICS):
            print("Вы проиграли!")
            break





            
        






        
        
