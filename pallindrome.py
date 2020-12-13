def first(word):
    return word[0]
def middle(word):
    return word[1:-1]
def last(word):
    return word[-1]
word=(input("enter a word:")).lower()
print("firsr:",first(word))

"""1*if we call middle function with two letters ,the middle function return that two letters,
    2*if we call middle function with one letter, the middle function return that one letter,
    3*if nothing is given as input that is empty string, the python throw back error as "IndexError: string index out of range"
       since no input is given"""
    
print("middle:",middle(word))
print("last:",last(word))


def is_palindrome(word):
    wordlen=len(word)
    word_list=list(word)
    reverse=[]
    for i in range(1,wordlen+1):
        reverse.append(word_list[-i])
           
    if  str(word_list)==str(reverse):
        return True
    else:
        return False
print(is_palindrome(word))
