class InvertedIndex:
    def __init__(self, word_to_docs_mapping):
        self.word_to_docs_mapping = word_to_docs_mapping
        return self.word_to_docs_mapping

    def query(self, words):
        common_art = self.word_to_docs_mapping[words[0]]
        word_temp_set = set()
        for word in words:
            if word in self.word_to_docs_mapping:
                word_temp_set = self.word_to_docs_mapping[word]
                common_art = word_temp_set.intersection(common_art)
                word_temp_set = set()
        return common_art


def load_document(filepath):
    dictionary = {}
    with open(filepath, encoding="utf-8", mode='r') as f:
        lines = f.readlines()
        for line in lines:
            key = int(line.split('\t', 1)[0])
            words = line.split('\t', 1)[1]
            dictionary.update({int(key): words.strip()})
    return dictionary


def build_inverted_index(articles):
    dictionary = {}
    for article in articles.keys():
        words = articles[article].split()
        for word in words:
            if word in dictionary:
                dictionary[word].add(int(article))
            else:
                dictionary[word] = set([int(article)])
    return dictionary
