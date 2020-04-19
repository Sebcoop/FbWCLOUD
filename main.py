from wordcloud import WordCloud
from nltk.corpus import stopwords
import matplotlib.pyplot as plt 
import json

# list of files you wish to take data from
files_list = ["message_1.json", "message_2.json"]

# to store processed words
comment_words = ''

# predefined list of stop words
stop_words = set(stopwords.words('english'))

# dictionary to store frequency of each unique word
word_freq = {}



for file in files_list:
	with open(file, 'r') as json_file:
		data = json.load(json_file)
		for i in data['messages']:
			if i.get('content'):
				sentence = i['content']
				for word in sentence.split():
					if word not in word_freq:
						word_freq[word] = 1
					else:
						word_freq[word] += 1
					if word not in stop_words:
						word = word.lower()
						#content_list.append(word)
						comment_words += " "+word+","+" "
						print(type(word), word)


sorted_word_freq = {k: v for k, v in sorted(word_freq.items(), key=lambda item: item[1])}
for i in sorted_word_freq:
	print(i, sorted_word_freq[i])



# generate the word cloud using wordcloud library
wordcloud = WordCloud(width = 800, height = 800, background_color ='white', stopwords = stop_words, min_font_size = 10).generate(comment_words) 

# plot the WordCloud image                        
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
plt.show() 
