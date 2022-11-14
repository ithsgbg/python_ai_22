from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC

def main():
    corpus = [
        'i love the Book',
        'this book was not so great',
        'the fit was great',
        'i love the shoes'
    ]

    books = 'Books'
    clothing = 'Clothing'

    categories = [books, books, clothing, clothing]

    vectorizer = CountVectorizer(ngram_range=(1, 4))

    vectors = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names_out())
    print(vectors.toarray())

    test_x = [
        'i love this read',
        'such a nice hat',
        'what a great book'
    ]

    test_y = [books, clothing, books]

    clf_svm = SVC(kernel='linear')
    clf_svm.fit(vectors, categories)

    test_vectors = vectorizer.transform(test_x)
    print('The result is:', clf_svm.score(test_vectors, test_y))


if __name__ == '__main__':
    main()
