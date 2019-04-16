
# coding: utf-8

# In[17]:


def longestWord(wordlist):
    longWord = ""
    max_len = 0
    for word in wordlist:
        if len(word) > max_len:
            longWord = len(word)
            longWord = word
    return longWord
longestWord(["vcvv","fdfdfdfdf","ggitigfgfggg"])

