# your code goes here!
class Anagram:
    def __init__(self , original_word):
        self.original_word= original_word

    def match(self, current_word):
        matches = []

        for word in current_word:
            if sorted(word)  == sorted(self.original_word):
                matches.append(word)
            
        return matches


