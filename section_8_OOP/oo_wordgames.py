import random
import re
class WordGame:
    def __init__(self,*words):

        # List of possible words
        self._words = words
        
        # Set of correctly-guessed letters 
        self._guesses = set()

        # Set of all letters in the word
        self._letters = set()

        # Number of guesses made by the user
        self._number_guesses = 0 

        self._word = None
    def _show_word2(self):
        # Display the word, BUT:
        print('Show word: ',self._word)
        guessed_letter = self._guesses.pop()
        for i in range(len(self._word)):
            letter = self._word[i]
            if letter != guessed_letter:
                self._word = re.sub(letter,'-',self._word)
        




        # For any letters that aren't guessed yet, display '-'
        # For any letters that have been guessed by now, display the letter
        # Space out all the letters and hyphens; NOT --a--d-, but - - a - - d -
        
    # tutor solution    
    def _show_word(self):

        if not self._guesses:
            return
        escaped = re.escape("".join(self._guesses))
        regex = f'[^{escaped}]'
        text = re.sub(regex,'-',self._word)
        text = re.sub(r'(.)', r' \1 ', text)
        print('This is the word',regex)
        print('This is the text',text)




    def _choose_word(self):
        # Assign self._word. to a word randomly chosen from the list of words
        self._word = random.choice(self._words)
        # Add all the letter of the word (separately) to self._letters
        # for i in range(len(self._word)):
        #     self._letters.add(self._word[i])
        self._letters.update(self._word)
        print(self._word)
        print(self._letters)


    def _guess_letters(self):
        new_set = set()
        new_set.update(self._word)

        while True:
            user_input = input('Guest a letter in the word > ')
            if len(user_input) != 1:
                continue
            self._number_guesses +=  1
            
            if user_input in self._word:
                self._guesses.add(user_input)
            if new_set.difference(self._guesses) == set():
                break
            
                
        # print('Number of guesses ',  self._number_guesses)
        # print('Correct guesses ', self._guesses)






    def run(self):
        self._choose_word()
        self._guess_letters()
        self._show_word()


def main():
    game = WordGame('peach','alligator','sky','fascinator')
    game.run()

main()