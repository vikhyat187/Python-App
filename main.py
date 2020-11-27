import random
from string import ascii_lowercase

def no_of_attempt():
  '''This is the function used to get the  no of attempts based on the choice of the user but it should lie b/w 1 and 10'''
  while True:
    num=input("Enter the no of attempts do you want to choose it can range from 1 to 10 as low as the number of chances the more difficult the game would be: ")
    try:
      num=int(num)
      if 1<=num<=10:
        return num
      else:
        print('{0} is not in between 1 and 10 '.format(num))
    except ValueError:
      print('{0} is not a number and it should be in between 1 and 10'.format(num))

#-----------------
def get_display_word(word,idxs):
  """ This function displays the word after our attempts"""
  if(len(word) != len(idxs)):
    raise ValueError("The lenght of word is not the same as indices lenght")
  displayed_word = ''.join([letter if idxs[i] else '*' for i, letter in enumerate(word)])
  return displayed_word.strip()
  '''Suppose the word that the player must guess is “hangman”. If the player has already guessed ‘a’, ‘m’, and ’n’, the boolean list would be [False, True, True, False, True, True, True] and the displayed word would look like *an*man.'''



#--------------------------------------
def get_next_letter(remaining_letters):
  '''This fn is used to get the user input characters'''
  if len(remaining_letters)==0:
    raise ValueError('There are no remaining letters')
  while True:
    next_letter= input('Choose the next letter ').lower()
    if len(next_letter)!=1:
      print('{0} is not a single character '.format(next_letter))
    elif next_letter not in ascii_lowercase:
      print('{0} is not a letter '.format(next_letter))
    elif next_letter not in remaining_letters:
      print('You have already entered {0}! Try another letter.'.format(next_letter))
    else:
      remaining_letters.remove(next_letter)
      return next_letter
  


#------------
def play_hangman():
  """ This is the main function for this game."""
  print("............Let's play Hangman!.................")
  attempts_remaining = no_of_attempt()
  #Randomly select a word
  print('Selecting a word .....')
  word_list = ['apple','banana','mango','orange','grapes','pineapple','kiwi','strawberry','blueberries','papaya','peach','lychee']
  word=random.choice(word_list)
  # print(word)

  
  #Initialize game state variables
  idxs = [letter not in ascii_lowercase for letter in word]
  remaining_letters = set(ascii_lowercase)
  wrong_letters = []
  word_solved = False

 
# Main game loop
  while(attempts_remaining > 0 and not word_solved):
  #Print current game state
    print('Word: {0}'.format(get_display_word(word,idxs)))
    print('Attempts Remaining: {0}'.format(attempts_remaining))
    print('Previous Wrong Guesses: {0}'.format(' '.join(wrong_letters)))

  #Get player's next letter guess
    next_letter = get_next_letter(remaining_letters)

  #Check if letter guess is in word
    if next_letter in word:
    #guessed correctly
      print('{0} is in the word! '.format(next_letter))
    
    #reveal matching letters 
      for i in range (len(word)):
        if word[i] ==next_letter:
          idxs[i]=True
    else:
      #guessed incorrectly  
       print('{0} is NOT in the word! '.format(next_letter))
     
      #decrement the no of attempts left out and append guess to wrong Guesses
      
       attempts_remaining -= 1
       wrong_letters.append(next_letter)
 
  #Check if word is completely solved
    if False not in idxs:
      word_solved =True
    print()

  # Revealing the word once the game is done
  print('The word is {0}'.format(word))

# Notifying the player of Victory or Defeat
  if word_solved:
    print('Congratulations! You won!')
  else:
    print('Try again next time!')

# Asking the player if he/she wants to try again
  try_again = input("Would you like to try again? [y/Y]")
  return try_again =='y'


  #main fn
if __name__=='__main__':
  while play_hangman():
    print()