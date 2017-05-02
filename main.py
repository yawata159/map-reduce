import string

with open('book.txt') as f:
    word_list = (f.read()
            .lower()
            .decode('utf-8-sig')
            .encode('utf-8')
            .strip()
            .translate(string.maketrans(string.punctuation, 32*' '))
            .split())

def word_freq(word):
    return len(filter(lambda s: s == word, word_list))

def words_freq(words):
    return reduce(lambda a,b: a+b, map(lambda s: 1 if s in words else 0, word_list))

def most_freq():
    pass

if __name__ == '__main__':

