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
        current_word = []
        result = []
        for k, v in start.items():
            if k != '#':
                pending_list.append((k, v))
        import pdb; pdb.set_trace()
        while len(pending_list) > 0:
            start = pending_list.pop()
            current_word.append(start[0])
            if len(start[1]) == 1 and start[1].get('#') == '#':
                result.append(''.join(current_word))
                current_word.pop()
            else:
                for k, v in start[1].items():
                    if k != '#':
                        pending_list.append((k, v))
                    else:
                        result.append(''.join(current_word))
        return result
