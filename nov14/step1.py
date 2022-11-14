import contractions
import string
import re
# import os

def clean_text(text):
    text = contractions.fix(text)
    print(text)
    text = text.lower()
    print(text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    print(text)
    text = re.sub(r'\w*\d\w*', '', text)
    print(text)

    # print('*'*40, os.getcwd())
    stopwords = [word.strip() for word in open('./nov14/stopwords_en.txt', 'r')]
    text = ' '.join([word for word in text.split() if word not in stopwords])
    print(text)
    

    return text


def main():
    text = "I read this book for the first time in 1987, and it's still one of my favorites!"
    # print(contractions.fix("that's it's i'll"))
    print(clean_text(text))

if __name__ == '__main__':
    main()
