def count_words(text):
    return len(text.split())

def count_char(text):
    freq = dict()
    for ch in text:
        ch = ch.lower()
        freq[ch] = freq.get(ch, 0) + 1
    return freq

def sort_on(dic):
    charlist = [{'char': char, 'count': dic[char]} for char in dic]
    charlist.sort(reverse=True, key=lambda x: x['count'])
    return charlist

