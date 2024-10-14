import os
import re
import sys


def make_vocab(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        raw_text = f.read()

    preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
    preprocessed = [item.strip() for item in preprocessed if item.strip()]
    words = sorted(set(preprocessed))
    vocab = {word: idx for idx, word in enumerate(words)}
    return vocab


class SimpleTokenizerV1:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {v: k for k, v in vocab.items()}

    def encode(self, text):
        preprocessed = re.split(r'([,.?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        ids = [self.str_to_int[x] for x in preprocessed]
        return ids
    
    def decode(self, ids):
        text = " ".join([self.int_to_str[x] for x in ids])
        text = re.sub(r'\s+([,.?!()\'])', r'\1', text) # 去掉符号前面的空格
        return text
    


def test_simple_tokenizer_v1():
    
    filepath = "../data/the-verdict.txt"
    vocab = make_vocab(filepath)

    text = """"It's the last he painted, you know," 
           Mrs. Gisburn said with pardonable pride."""

    tokenizer = SimpleTokenizerV1(vocab)

    ids = tokenizer.encode(text)

    decode_text = tokenizer.decode(ids)

    print(text)
    print(decode_text)

    print(decode_text == text)


if __name__ == "__main__":
    os.chdir(sys.path[0])
    test_simple_tokenizer_v1()