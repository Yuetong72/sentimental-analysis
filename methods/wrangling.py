import re

class wrangling():
    def __init__(self, scrapedData):
        self.scrapedData = scrapedData

    def clean(self): 
        cleanedData = {'title':[]}
        for sent in self.scrapedData['title']:
            cleanedSent = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", str(sent)).split()) 
            cleanedData['title'].append(cleanedSent)
        return cleanedData

        



