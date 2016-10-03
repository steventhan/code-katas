from trie import Trie


class AutoCompleter(object):
    def __init__(self, vocabulary=None, max_completions=5):
        self.vocabulary = Trie(vocabulary)
        self.max_completions = max_completions

    def __call__(self, token):
        start = self.vocabulary.root
        counter = 0
        while counter < len(token):
            try:
                start = start[token[counter]]
            except KeyError:
                return []
            counter += 1
        completion_words = self.get_completion_words(start)
        return [token + item for item in completion_words]

    def get_completion_words(self, start):
        pending_list = []
        current_tring = ''
        while True:
            if len(start) > 1:
                for k, v in start.items():
                    if k != '#':
                        pending_list.append((k, v))
                start = pending_list.pop()
                current_tring += start[0]
            else:
                yield current_tring
            if len(pending_list) == 0:
                break
