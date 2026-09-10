from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
sample_text ="Hello Mr.smith how are you doing today? the weather is great and python is awesome"
words = word_tokenize(sample_text)
stop_words = set(stopwords.words('english'))
print(stop_words)
filtered_sentence=[]
for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)
print(filtered_sentence)
