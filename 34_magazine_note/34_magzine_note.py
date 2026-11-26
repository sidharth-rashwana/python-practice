
from collections import Counter


def checkMagazine(magazine, note):
                                                
    magazine_words = Counter(magazine)
                                                   
    note_words = Counter(note)
                                                         
    for word, count in note_words.items():
        if magazine_words[word] <= count:
            print("No")
            return

    print("Yes")


                
example1 = checkMagazine(['give', 'me', 'one', 'grand', 'today', 'night'], [
                         'give', 'one', 'grand', 'today'])
example2 = checkMagazine(['two', 'times', 'three', 'is', 'not', 'four'], [
                         'two', 'times', 'two', 'is', 'four'])
example3 = checkMagazine(['ive', 'got', 'a', 'lovely', 'bunch', 'of', 'coconuts'], [
                         'ive', 'got', 'some', 'coconuts'])
