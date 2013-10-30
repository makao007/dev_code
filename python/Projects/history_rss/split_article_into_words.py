#encoding=utf-8

def stop_words ():
    sign = '、 。 ， ： “ ” ？ 》 《 ！ , " ! . 【 】 （ ） ～ ( ) & # ￥ $ ; / [ ] ? - _ * : % ；'.decode('utf8').split(' ')
    sign.extend ([u' ',u'\n',u'\r',u'\t',u'\\',u'的'])
    sign.extend (map(str,range(10)))
    sign.extend (list(string.ascii_letters))
    return sign


def split_text (s):
    sign = stop_words()
    words = {}
    length = 1.0

    english_words = re.findall(r'''[1-9a-zA-Z\-\_]{2,}''',s)
    for word in english_words:
        if len(word)==2:
            if '-' in word or '_' in word or word.isdigit() or word=='u2' or word=='1D' or word =='1C':
                continue
        word = word.lower()
        if not words.has_key(word):
            words[word] = 0
        words[word] += 1
        length += 1
    
    for i in range(len(s)-1):
        if s[i] in sign or s[i+1] in sign:
            continue
        word = s[i:i+2]
        if not words.has_key (word):
            words[word] = 0
        words[word] += 1
        length += 1.0
   
    return words,length
