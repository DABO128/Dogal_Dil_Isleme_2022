#!/usr/bin/env python
# coding: utf-8

# In[17]:


import nltk


# # Removing Stopwords
# 

# In[18]:


from nltk.tokenize import word_tokenize
text="""Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome.
The sky is pinkish-blue. You shouldn't eat cardboard"""
tokenized_sent=word_tokenize(text)

filtered_sent=[]
for w in tokenized_sent:
    if w not in stop_words:
        filtered_sent.append(w)
print("Tokenized Sentence:",tokenized_sent)
print("Filterd Sentence:",filtered_sent)


# # Lexicon Normalization

# # Stemming

# In[19]:


# Stemming
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()

stemmed_words=[]
for w in filtered_sent:
    stemmed_words.append(ps.stem(w))

print("Filtered Sentence:",filtered_sent)
print("Stemmed Sentence:",stemmed_words)


# # Lemmatization

# In[20]:


#Lexicon Normalization
#performing stemming and Lemmatization

from nltk.stem.wordnet import WordNetLemmatizer
lem = WordNetLemmatizer()

from nltk.stem.porter import PorterStemmer
stem = PorterStemmer()

word = "Lemmatization"
print("Lemmatized Word:",lem.lemmatize(word,"v"))
print("Stemmed Word:",stem.stem(word))


# # POS Tagging

# In[21]:


sent = "Albert Einstein was born in Ulm, Germany in 1879."


# In[22]:


tokens=nltk.word_tokenize(sent)
print(tokens)


# In[25]:


nltk.pos_tag(tokens)


# # NNP:Proper noun singular
# 

# # VBD : Verb past tense
# 

# # CD:Cardinal number
# 

# # VBN:Verb past participle

# # Sentiment Analysis

# # Text Classification

# In[ ]:




