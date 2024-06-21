import string
def menu_input():
    print('----- MENU ------')
    print('(E)nter a word')
    print('(Q)uit program')
    
    choice = input('Select option (E or Q):')
    return choice

def validate_word(word):
    word = word.strip()
    valid = string.ascii_letters

    if len(word.split()) > 1:
        print(f'{len(word.split())} words were typed')
        return False
    
    for char in word:
        if char not in valid:
            return False
        
    return True

    