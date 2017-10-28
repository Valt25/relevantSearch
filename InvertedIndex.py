

class InvertedIndex():
    _tokens = {}

    def add(self, new_token, doc_number):
        new_token = new_token.lower()
        if new_token not in self._tokens:
            self._tokens[new_token] = []
        if (len(self._tokens[new_token]) == 0) or (self._tokens[new_token][-1] != doc_number):
            self._tokens[new_token].append(doc_number)

    def add_list(self, new_tokens, doc_number):
        for token in new_tokens:
            self.add(token, doc_number)

    def sort(self):
        for token, doc_list in self._tokens.items():
            doc_list.sort()

