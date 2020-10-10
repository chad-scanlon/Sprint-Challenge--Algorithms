'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # base case
    count = 0
    
    if word.startswith("th"):
        count = 1  # start at 1
    # recursive case
    if len(word) > 2:
        return count_th(word[1: len(word)]) + count
    else:
        return count
