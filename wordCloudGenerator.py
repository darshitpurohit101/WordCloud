import wikipedia
from wordcloud import WordCloud,STOPWORDS
import os
from PIL import Image
import numpy as np

#dirp=os.path.dirname(_file_)
f = open('textfile','r')
z = f.read()
#print(z)


#def get_wiki(query):
 #    title=wikipedia.search(query[0])
   #  return page.content
  #   page=wikipedia.page(title)

def create_worldcloud(text):
     stopwords = set(STOPWORDS)#creating set of stopwords
     print(stopwords)
     mask=np.array(Image.open(os.path.join('/root/Desktop/pythonproject','mask.png')))
     wc = WordCloud (background_color='black',
                  mask=mask,
                  max_words=300,
                  #min_font_size=1,
                  #max_font_size=14,
                  #mode='RGBA',  #to make background transparent
                  normalize_plurals=True,
                  stopwords=stopwords)
     
     wc.generate(text)
     wc.to_file(os.path.join('/root/Desktop/pythonproject','wc7.png'))

        
#create_worldcloud(get_wiki("Football"))#give any query title(name of a   topic  to search) 
create_worldcloud(z)
f.close()
