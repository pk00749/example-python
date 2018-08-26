from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
import random

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 255)

d = path.dirname(__file__)

# read the mask image
# taken from
# http://www.stencilry.org/stencils/movies/star%20wars/storm-trooper.gif
mask = imread(path.join(d, "5.png"))

# movie script of "a new hope"
# http://www.imsdb.com/scripts/Star-Wars-A-New-Hope.html
# May the lawyers deem this fair use.
# text = open("a_new_hope.txt").read()
text = open('G:\Program\Projects\wordCloud.txt').read()

# preprocessing the text a little bit
# text = text.replace("HAN", "Han")
# text = text.replace("LUKE'S", "Luke")

# adding movie script specific stopwords
stopwords = STOPWORDS.copy()
stopwords.add("int")
stopwords.add("ext")

wc = WordCloud(font_path='.\\Dinky_Rink_NF.ttf',
               max_words=1000,
               background_color="white",
               mask=mask,
               stopwords=stopwords,
               margin=10, random_state=42
               ).generate(text)

# store default colored image
default_colors = wc.to_array()
plt.figure()
plt.title("Custom colors")
image_colors = ImageColorGenerator(mask)
plt.imshow(wc.recolor(color_func=image_colors))
wc.to_file("a_new_hope.png")
plt.axis("off")
# plt.title("Default colors")
# plt.imshow(default_colors)
# plt.axis("off")
plt.show()
