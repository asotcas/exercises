def word_count (my_text):
    '''Count every single word within a text string (case ir )
   
    my text (str): any text
     output (dict): key --> word , value -> number of mathecs'''
    times_by_word = {}
    word_list = my_text.split()
    for my_word in word_list:
        key = my_word.lower()
        if my_word not in times_by_word:
            times_by_word [key] = 1
            
        
    return times_by_word