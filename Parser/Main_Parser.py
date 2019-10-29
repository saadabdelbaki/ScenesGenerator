>>> import nltk
>>> sentence = """ At eight o'clock I will kiss my gf. """
>>> tokens = nltk.word_tokenize(sentence)
>>> tokens
['At', 'eight', "o'clock", 'I', 'will', 'kiss', 'my', 'gf', '.']
>>> tagged = nltk.pos_tag(tokens)
>>> tagged[0:6]
[('At', 'IN'), ('eight', 'CD'), ("o'clock", 'NN'), ('I', 'PRP'), ('will', 'MD'), ('kiss', 'VB')]
>>> entities = nltk.chunk.ne_chunk(tagged)
>>> entities
Tree('S', [('At', 'IN'), ('eight', 'CD'), ("o'clock", 'NN'), ('I', 'PRP'), ('will', 'MD'), ('kiss', 'VB'), ('my', 'PRP$'), ('gf', 'NN'), ('.', '.')])
>>> from nltk.corpus import treebank
>>> t = treebank.parsed_sents('wsj_0001.mrg')[0]
>>> t.draw()
