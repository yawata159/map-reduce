import string

with open('book.txt') as f:
    word_list = (f.read()
            .lower()
            .decode('utf-8-sig')
            .encode('utf-8')
            .strip()
            .translate(None, string.punctuation)
            .split())

def word_freq(word, l):
    return len(filter(lambda s: s == word, l))

def words_freq(words, l):
    return reduce(lambda a,b: a+b, map(lambda s: 1 if s in words else 0, l))

def most_freq(l):
    d = dict()
    for word in l:
        d[word] = (d[word] + 1) if word in d.keys() else 1
    return reduce(lambda a,b: a if d[a] > d[b] else b, d.keys())

if __name__ == '__main__':
    print "Frequency of 'france':", word_freq('france', word_list)
    print "Frequency of 'with':", word_freq('with', word_list)
    print "Frequency of 'conversation':", word_freq('conversation', word_list)
    print
    print "Frequency of ['france', 'with', 'conversation']:", words_freq(['france', 'with', 'conversation'], word_list)
    print
    print "Most frequent word (takes a while):"
    print most_freq(word_list)
