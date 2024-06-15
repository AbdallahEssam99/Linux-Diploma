# #Task #2
def isVowel():
    Char = input("\nEnter a character to check if its a vowel or not : " ).strip().lower()
    if Char in {'a', 'e', 'i', 'o', 'u'}:
        print("\nVOWEL\n")
    else:
        print("\nCONSONANT\n")


isVowel()





