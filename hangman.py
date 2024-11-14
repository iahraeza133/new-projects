def hangman():
    word_list = ["python", "hangman", "programming", "development", "challenge"]
    selected_word=random.choice(word_list)
    guess_count=len(selected_word)
    while count>0:
         guesssed_char=input("enter a char:")
         if guesssed_char.isalpha():
             if guesssed_char in selected_word:
             else:
                 guess_count_=1
                 print(f"wrong!")
                 
         else:
            print("plz enter valid char")
            
hangman()