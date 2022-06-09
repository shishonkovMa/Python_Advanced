class CountVectorizer:
    def __init__(self, ngram_size):
        self.ngram_size = ngram_size
        self.dictionary = dict()

    def fit(self, corpus):
        lst = []
        lst_1 = []
        for i in corpus:
            start = 0
            end = self.ngram_size
            while end <= len(i):
                lst.append(i[start:end])
                start += 1
                end += 1
            lst_1.append(lst)
        unique_tokens = sorted(list(set(lst)))
        ind = 0
        for i in unique_tokens:
            self.dictionary[i] = ind
            ind += 1
        return self.dictionary

    def transform(self, corpus):
        spis = []
        for i in corpus:
            lst = []
            start = 0
            end = self.ngram_size
            while end <= len(i):
                lst.append(i[start:end])
                start += 1
                end += 1
            sub_spis = []
            for k in self.dictionary:
                count = 0
                for j in lst:
                    if k == j:
                        count += 1
                sub_spis.append(count)
            spis.append(sub_spis)
        self.dictionary = dict()
        return spis

    def fit_transform(self, corpus):
        self.dictionary = self.fit(corpus)
        ft = self.transform(corpus)
        self.dictionary = dict()
        return ft
