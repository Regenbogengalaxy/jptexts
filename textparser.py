from sudachipy import Dictionary, SplitMode

def roughTokenize(text):

    tok = Dictionary(dict="full").create(SplitMode.C)
    morphemes = tok.tokenize(text)
    tok.tokenize(text, out=morphemes)

    return morphemes

def fineTokenize(text):

    tok = Dictionary(dict="full").create(SplitMode.A)
    morphemes = tok.tokenize(text)
    tok.tokenize(text, out=morphemes)

    return morphemes
