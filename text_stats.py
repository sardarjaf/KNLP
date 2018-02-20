
# coding: utf-8

# In[7]:


import os
import nltk
import codecs
import matplotlib.pyplot as plt

from nltk import sent_tokenize, word_tokenize
nltk.download('punkt')


# In[15]:


PATH = os.getcwd()
output_dir_path = PATH + "/plain_text_corpus"
file_dir_list = os.listdir(output_dir_path)

input_dir_path = "/home/sardar/workspace/parse-html/normalised_files"
input_dir_list = os.listdir(input_dir_path)


# In[559]:


s = ['the cat sat', 'i like milk']
s.append('i like her')
if not(['the cat sat'] in s):
    print('yes')


# In[9]:


stats = {}
all_words={}


# In[ ]:


# read the normalised files and segment the sentences
# write the segmented sentences in a file
for dirs in input_dir_list:
        
    # store some stats in a dictionary
    stats[dirs] = {}
    stats[dirs]['total_documents']=0
    stats[dirs]['total_sentences']=0
    stats[dirs]['total_words']=0
    
    max_sent_len = 1
    min_sent_len = 10000
    
    all_words[dirs] = []

    for files in os.listdir(input_dir_path+"/"+dirs):
        
        file_input = codecs.open(input_dir_path+"/"+dirs+"/"+files, encoding='utf-8')
        text = file_input.read()
        file_input.close()
        
        # write the segmented sentences to new files in the directory specified by dir_path variable
        file_output = codecs.open(output_dir_path+"/"+dirs+"/"+files, 'w', encoding='utf-8')
        
        result = sent_tokenize(text)
        for r in result:
            if len(r) > 5:
                stats[dirs]['total_sentences'] += 1 # update the total_sentences value in the dictionary for a dir (topic)
                words_tokens = word_tokenize(r)                
                all_words[dirs] += words_tokens
                print(words_tokens, len(words_tokens),'\n')
                stats[dirs]['total_words'] += (len(words_tokens)) # update total_words value in the dictionary for a dir (topic)
                sent_length = len(words_tokens)
                
                if sent_length >= max_sent_len:
                   
                    stats[dirs]['max_sent_len'] = sent_length
                    stats[dirs]['max_sent_len_doc'] = dirs+"/"+files
                
                if sent_length <= min_sent_len:
                    min_sent_len = sent_length
                    stats[dirs]['min_sent_len'] = min_sent_len
                    stats[dirs]['min_sent_len_doc'] = dirs+"/"+files
               
                
                file_output.write(r+'\n')
        stats[dirs]['total_documents'] += 1
        file_output.close()
        


# In[55]:


total_docs = 0
total_words = 0
total_sents = 0
for key, values in stats.items():
    #if values['total_sentences']:
    print(key, values['total_documents'], values['total_sentences'], values['total_words'], 'Avg. word/sentence', values['total_words'] / values['total_sentences'])
    
    print('max_sent_len', values['max_sent_len'])
    print('max_sent_len_doc', values['max_sent_len_doc'])
    print('min_sent_len', values['min_sent_len'])
    print('min_sent_len_doc', values['min_sent_len_doc'])
   
        


print(total_sents, total_words, stats)



# In[509]:


ws = []
for key, value in all_words.items():
    print(key,'\n')
    for v in value[:100]:
        ws.append(v)
print(len(ws))
print(set(ws))

    


# In[294]:



topics = []
for dirs in input_dir_list:
    print(dirs, len(topics))
    topics.append(dirs[0:3])
    
x = topics
plt.ylabel("No. Documents")
x = topics
y = [1,2,3,4,5,6,7,8,9,22,11,22,33,22,44]
y = [1,2,3,4,5,6,7,8,9,22,11,22,33,22,44]
N = len(y)
x = range(N)
width = 1/1.5

width = 1/1.5
plt.bar(x,y, width, color="blue")
plt.show()


# In[143]:


words = word_list.words(with open(file, 'r') as f.read() for f in fileids)
words


# In[130]:


tokens = set(words)
#sorted(tokens)


# In[234]:


cfd = nltk.ConditionalFreqDist(
    (genre, words)
    for genre in ['IT', 'health'] #[genre for genre in file_dir_list]
    for words in genre
)


# In[137]:


genre_word = [(genre, word)
             for genre in [file_dir_list]
             for word in [ in genre]
len(genre_word)


# In[138]:


genre_word[:4]


# In[133]:


cfd = nltk.ConditionalFreqDist(genre_word)


