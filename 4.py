from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
ps = PorterStemmer()
new_text = "Is is very important to be pythonly while yoou are pythoning with python .all pythoners have poorly pythoned atleast once"
words = word_tokenize(new_text)
for w in words:
    print(ps.stem(w))
