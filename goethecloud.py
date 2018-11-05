"""A short script to create wordclouds from a given text and with a     """

from PIL import Image
from wordcloud import WordCloud
#  import wordcloud
#  from nltk.corpus import stopwords
from stop_words import get_stop_words
import random

import numpy as np
import matplotlib.pyplot as plt

with open("Goethe_Sammler.txt", "r") as f:
    text = f.read()

goethe_mask = np.array(Image.open('Goethe_Schattenriss.jpg'))

blacklist = get_stop_words('german')
blacklist = set(blacklist)
blacklist = blacklist.union({'wäre', 'konnte', 'lassen', 'sagte', 'muß', 'Oheim', 'Julie', 'sei'})

def grey_color(word, font_size, position, orientation, random_state=None, **kwargs):
    return("hsl(0, 0%%, %d%%)" % np.random.randint(10, 20))

wc = WordCloud(background_color='white', mask=goethe_mask, stopwords=blacklist, width=800, height=800)

wc.generate(text)

wc.recolor(color_func = grey_color)
fig = plt.figure(dpi=600)

plt.imshow(wc, interpolation="bilinear")
plt.axis('off')

fig.savefig('WC_Goethe.jpg')
