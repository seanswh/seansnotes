#Word Clouds
    #Word clouds (also known as text clouds or tag clouds) work in a simple way: the more a specific word appears in a source of textual data (such as a speech, blog post, or database), the bigger and bolder it appears in the word cloud.
    #Luckily, a Python package already exists in Python for generating word clouds. The package, called word_cloud was developed by Andreas Mueller. You can learn more about the package by following this link.
# open the file and read it into a variable alice_novel

# import package and its set of stopwords
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image # converting images into arrays
print ('Wordcloud is installed and imported!')
alice_novel = open('alice_novel.txt', 'r').read()
    
print ('File downloaded and saved!')
#Next, let's use the stopwords that we imported from word_cloud. We use the function set to remove any redundant stopwords.

stopwords = set(STOPWORDS)

#Excellent! This looks really interesting! Another cool thing you can implement with the word_cloud package is superimposing the words onto a mask of any shape. Let's use a mask of Alice and her rabbit. We already created the mask for you, so let's go ahead and download it and call it alice_mask.png.

# instantiate a word cloud object
alice_wc = WordCloud(
    background_color='white',
    max_words=2000,
    stopwords=stopwords
)

#said isn't really an informative word. So let's add it to our stopwords and re-generate the cloud.
# add the words said to stopwords
stopwords.add('said')
alice_wc.generate(alice_novel)
#display the cloud
fig = plt.figure()
fig.set_figwidth(14) # set width
fig.set_figheight(18) # set height
plt.imshow(alice_wc, interpolation='bilinear')
plt.axis('off')
plt.show()