from textblob import TextBlob
import pandas as pd
import numpy as np

class sentimental:
    def __init__(self):
        self.keyword = [['Bitcoin', 'BTC'], ['Ethereum', 'ETH'],['Ripple','XRP'], ['Litecoin', 'LTC'], ['Stellar', 'XLM'], 
          ['Neo', 'NEO'], ['Monero', 'XMR'], ['Ethereum Classic', 'ETC'], ['QTUM', 'QTUM'],['ZCash', 'ZEC'], 
          ['Nano', 'NANO'], ['Basic Attention Token', 'BAT'], ['Augur', 'REP'], ['Ark', 'ARK'], ['Iota', 'MIOTA'], 
          ['Tezos', 'XTZ'], ['VeChain', 'VET'], ['EOS', 'EOS'], ['Bcash', 'BCH'], ['Decred', 'DCR']]


    # get sentimental scores
    def get_sentiment(self, post): 
        analysis = TextBlob(post) 
        sentiment_result = analysis.sentiment.polarity
        return sentiment_result


    # get magnitude from the sentimental scores
    def get_sentiment_mag(self, post): 
        analysis = TextBlob(post) 
        if analysis.sentiment.polarity > 0: 
            return 'positive'
        elif analysis.sentiment.polarity == 0: 
            return 'neutral'
        else: 
            return 'negative'



    # get average result of two key words
    def caculate_average(self, data_frame1, data_frame2):
        list1_met1 = data_frame1['matrix1']
        list2_met1 = data_frame2['matrix1']
        avg_met1 = (list1_met1 + list2_met1) / 2
        
        list1_met2 = data_frame1['matrix2']
        list2_met2 = data_frame2['matrix2']
        avg_met2 = (list1_met2 + list2_met2) / 2
        
        list1_ttl = data_frame1['total']
        list2_ttl = data_frame2['total']
        sum_ttl = list1_ttl + list2_ttl
        
        list1_num_pos = data_frame1['num_pos']
        list2_num_pos = data_frame2['num_pos']
        sum_num_pos = list1_num_pos + list2_num_pos
        
        list1_num_neu = data_frame1['num_neu']
        list2_num_neu = data_frame2['num_neu']
        sum_num_neu = list1_num_neu + list2_num_neu
        
        list1_num_neg = data_frame1['num_neg']
        list2_num_neg = data_frame2['num_neg']
        sum_num_neg = list1_num_neg + list2_num_neg

        pol1 = self.final_mag(avg_met1)
        pol2 = self.final_mag(avg_met2) 
        
        result = {"result_pos":[sum_num_pos],
                "result_neg":[sum_num_neg],
                "result_neu":[sum_num_neu],
                "amount":[sum_ttl],
                "matrix1":[avg_met1],
                "polarity1":[pol1],
                "matrix2":[avg_met2],
                "polarity2":[pol2]
                    }
        return result

    def final_mag(self, score): 
        if score <= 1 and score > 0.01: 
            return 'positive'
        elif score <= 0.01 and score >= -0.01: 
            return 'neutral'
        else: 
            return 'negative'




    # get metrices using two different ways
    def get_sentiment_result(self, data):
        if len(data['title']) != 0:
            dataframe = {'title':[],
                    'sentiment':[],
                    'sentiment mag':[],
                    'num_pos':[],           
                    'num_neg':[],
                    'num_neu':[],
                    'total':[],
                    'matrix1':[],        
                    'matrix2':[],   
                    }
            for sentence in data['title']:
                dataframe['title'].append(sentence)
                dataframe['sentiment'].append(self.get_sentiment(sentence))
                dataframe['sentiment mag'].append(self.get_sentiment_mag(sentence))
    
            dataframe['num_pos'] = dataframe['sentiment mag'].count('positive')
            dataframe['num_neg'] = dataframe['sentiment mag'].count('negative')
            dataframe['num_neu'] = dataframe['sentiment mag'].count('neutral')
            dataframe['total'] = dataframe['num_pos'] + dataframe['num_neg'] + dataframe['num_neu']
            total_count = dataframe['total']
            POS_count = dataframe['num_pos']
            NEG_count = dataframe['num_neg']
            # NEUT_count = dataframe['num_neu']
            sent = dataframe['sentiment']
            NEG_magnitude = sum([sent for sent in sent if sent < 0])
            POS_magnitude = sum([sent for sent in sent if sent > 0])
            matrix1 = (1/total_count) * ((POS_count/total_count) * POS_magnitude + (NEG_count/total_count) * NEG_magnitude)# + (NEU_count/total_count)*NEU_magnitude)
            # matrix2 = equal weight summation
            matrix2 = (1/total_count) * sum(sent)# + NEU_magnitude)
            dataframe['matrix1'] = matrix1
            dataframe['matrix2'] = matrix2

        else:
            dataframe = {'title':0,
                    'sentiment':0,
                    'sentiment mag':0,
                    'num_pos':0,
                    'num_neg':0,
                    'num_neu':0,
                    'total':0,
                    'matrix1':0,      
                    'matrix2':0
                    }
        return dataframe

