#!/usr/bin/env python
# coding: utf-8

# In[14]:


import nltk


# In[15]:


text="""Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome.
The sky is pinkish-blue. You shouldn't eat cardboard. Exemple : nouvelles images à venir demain nouvelles images à venir demain."""


# In[16]:


text.split(' ')


# In[17]:


get_ipython().system('pip install nltk')


# In[55]:


text="""Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome.
The sky is pinkish-blue. You shouldn't eat cardboard.Merhaba Bay Smith, bugün nasılsınız? Hava harika ve şehir harika.
Gökyüzü pembemsi-mavidir. karton yememelisin.Bonjour M. Smith, comment allez-vous aujourd'hui ? Il fait beau et la ville est géniale.
Le ciel est bleu rosé. Tu ne devrais pas manger de carton."""


# # Sentence Tokenization

# In[56]:


nltk.download('punkt')


# In[89]:


from nltk.tokenize import sent_tokenize


# In[90]:


tokenized_text=sent_tokenize(text)
print(tokenized_text)


# In[ ]:





# # Word Tokenization
# 

# In[91]:


from nltk.tokenize import word_tokenize


# In[92]:


tokenized_word=word_tokenize(text)


# In[93]:


print(tokenized_word)


# # Frequency Distribution
# 

# In[94]:


from nltk.probability import FreqDist


# In[95]:


fdist = FreqDist(tokenized_word)


# In[96]:


print(fdist)


# In[97]:


fdist.most_common(2)


# In[98]:


# Frequency Distribution Plot
import matplotlib.pyplot as plt


# In[99]:


fdist.plot(30,cumulative=False)
plt.show()


# # Stopwords

# In[100]:


from nltk.corpus import stopwords


# In[101]:


nltk.download('stopwords')


# In[102]:


stop_words=set(stopwords.words("Turkish"))


# In[71]:


print(stop_words)


# In[72]:


stop_words=set(stopwords.words("French"))


# In[73]:


print(stop_words)


# In[74]:


stop_words=set(stopwords.words("english"))


# In[75]:


print(stop_words)


# # Removing Stopwords
# 

# In[76]:


if 'our' in stop_words:print("fount it")


# In[77]:


filtered_sent = []
for word in tokenized_sent:
    if word not in stop_words:
        filtered_sent.append(word)
print("Tokenized Sentence:",tokenized_sent)
print("Filterd Sentence:",filtered_sent)


# In[79]:


# download stpwords
import nltk
nltk.download('stopwords')

# import nltk for stopwords
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
print(stop_words)

# assign string
no_wspace_string='python released in was a major revision of the language that is not completely backward compatible and much python code does not run unmodified on python with python s endoflife only python x and later are supported with older versions still supporting eg windows and old installers not restricted to bit windows'

# convert string to list of words
lst_string = [no_wspace_string][0].split()
print(lst_string)

# remove stopwords
no_stpwords_string=""
for i in lst_string:
    if not i in stop_words:
        no_stpwords_string += i+' '

        # removing last space
no_stpwords_string = no_stpwords_string[:-1]
print(no_stpwords_string)


# # Lexicon Normalization

# # Stemming
# 

# In[80]:


# Stemming
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize


# In[81]:


ps = PorterStemmer()

stemmed_words=[]
for w in filtered_sent:
    stemmed_words.append(ps.stem(w))

print("Filtered Sentence:",filtered_sent)
print("Stemmed Sentence:",stemmed_words)


# # Lemmatization
# 

# In[82]:


nltk.download('wordnet')


# In[83]:


nltk.download('omw-1.4')


# In[84]:


#Lexicon Normalization
#performing stemming and Lemmatization

from nltk.stem.wordnet import WordNetLemmatizer
lem = WordNetLemmatizer()

from nltk.stem.porter import PorterStemmer
stem = PorterStemmer()

word = "flying"
print("Lemmatized Word:",lem.lemmatize(word,"v"))
print("Stemmed Word:",stem.stem(word))


# # POS Tagging
# 

# In[85]:


sent = "Albert Einstein was born in Ulm, Germany in 1879."


# In[86]:


tokens=nltk.word_tokenize(sent)
print(tokens)


# In[87]:


nltk.download('averaged_perceptron_tagger')


# In[88]:


nltk.pos_tag(tokens)


# In[ ]:





# In[ ]:




