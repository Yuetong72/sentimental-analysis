# Import classes from packages
from methods import scraping
from methods import wrangling
from methods import sentimental
import pandas as pd
from pymongo import MongoClient
import datetime

# def main():
#     # Create an object of methods class & call a method of it
#     keywords = [['Bitcoin', 'BTC'], ['Ethereum', 'ETH'],['Ripple','XRP'], ['Litecoin', 'LTC'], ['Stellar', 'XLM'], 
#             ['Neo', 'NEO'], ['Monero', 'XMR'], ['Ethereum Classic', 'ETC'], ['QTUM', 'QTUM'],['ZCash', 'ZEC'], 
#             ['Nano', 'NANO'], ['Basic Attention Token', 'BAT'], ['Augur', 'REP'], ['Ark', 'ARK'], ['Iota', 'MIOTA'], 
#             ['Tezos', 'XTZ'], ['VeChain', 'VET'], ['EOS', 'EOS'], ['Bcash', 'BCH'], ['Decred', 'DCR']]

#     result_dict = {"asset":[],
#                 "result_pos":[],
#                 "result_neg":[],
#                 "result_neu":[],
#                 "amount":[],
#                 'matrix1':[],
#                 'polarity1':[],         
#                 'matrix2':[],
#                 'polarity2':[]
#                 }
#     myScraping = scraping()
#     for word in keywords:
#         print('start scraping')
#         date_time_start = datetime.datetime.now()
#         times_start = date_time_start.time() 
#         if times_start.hour == 14 and times_start.minute == 30:
#             dfNews1 = myScraping.get_news(word[0])
#         dfReddit1 = myScraping.get_reddit(word[0])
#         dfTwitter1 = myScraping.get_twitter(word[0])

#         sources1 = [dfReddit1, dfTwitter1]
#         data1 = pd.concat(sources1, sort=False)
 
#         if times_start.hour == 14 and times_start.minute == 30:
#             dfNews2 = myScraping.get_news(word[1])
#         dfReddit2 = myScraping.get_reddit(word[1])
#         dfTwitter2 = myScraping.get_twitter(word[1])

#         sources2 = [dfReddit2, dfTwitter2]
#         data2 = pd.concat(sources2, sort=False)


#         # print('start scraping')
#         myWrangling1 = wrangling(data1)
#         cleanedData1 = myWrangling1.clean()
#         myWrangling2 = wrangling(data2)
#         cleanedData2 = myWrangling2.clean()

#         mySentimental1 = sentimental()
#         data_frame1 = mySentimental1.get_sentiment_result(cleanedData1)
#         mySentimental2 = sentimental()
#         data_frame2 = mySentimental2.get_sentiment_result(cleanedData2)
#         result = mySentimental1.caculate_average(data_frame1, data_frame2)

#         result_dict["asset"].append(word[1])
#         result_dict["result_pos"].append(result['result_pos'])
#         result_dict["result_neg"].append(result['result_neg'])
#         result_dict["result_neu"].append(result['result_neu'])
#         result_dict["amount"].append(result['amount'])
#         result_dict["matrix1"].append(result['matrix1'])
#         result_dict["polarity1"].append(result['polarity1'])
#         result_dict["matrix2"].append(result['matrix2'])
#         result_dict["polarity2"].append(result['polarity2'])
        
#     return pd.DataFrame(result_dict)




# iteration = 0
# while True:
#     if iteration > 100000000:
#         iteration = 0
#     date_time_start = datetime.datetime.now()
#     times_start = date_time_start.time()  # Gives the time
    
#     if times_start.minute == 30 and times_start.second == 0:
#         # calling main function
#         results = main() 

#         date_time_end = datetime.datetime.now()
#         times_end = date_time_end.time()
#         print('iteration: ', iteration)
#         print('end time:', times_end.hour, times_end.minute, times_end.second, times_end.microsecond)
#         iteration += 1

#         # write into database and update IDs for assets
#         # uri = "mongodb://sentiment:BlackHole1@ds153394.mlab.com:53394/cryptoeq"
    
#         uri = "mongodb://localhost:27017/local"
        
#         client = MongoClient(uri)
#         db = client.cryptoeq
#         # db = client.test
#         print("Mar31")
#         # for each keyword
#         for j in range(20):
#             db.Mar31.insert_one({"result_pos":results['result_pos'][j][0],
#                                   "result_neg":results['result_neg'][j][0],
#                                   "result_neu":results['result_neu'][j][0],
#                                   "amount":results['amount'][j][0],
#                                   "matrix1":results['matrix1'][j][0],
#                                   "polarity1":results["polarity1"][j][0],
#                                   "matrix2":results['matrix2'][j][0],
#                                   "polarity2":results["polarity2"][j][0],
#                                   "asset":results['asset'][j],
#                                   "createdAt": str(date_time_start),
#                                   "updatedAt": str(date_time_end)
#                                   })



keywords = [['Bitcoin', 'BTC'], ['Ethereum', 'ETH'],['Ripple','XRP'], ['Litecoin', 'LTC'], ['Stellar', 'XLM'], 
            ['Neo', 'NEO'], ['Monero', 'XMR'], ['Ethereum Classic', 'ETC'], ['QTUM', 'QTUM'],['ZCash', 'ZEC'], 
            ['Nano', 'NANO'], ['Basic Attention Token', 'BAT'], ['Augur', 'REP'], ['Ark', 'ARK'], ['Iota', 'MIOTA'], 
            ['Tezos', 'XTZ'], ['VeChain', 'VET'], ['EOS', 'EOS'], ['Bcash', 'BCH'], ['Decred', 'DCR']]

dfNews = pd.DataFrame()
for word in keywords:
    dfNews1 = myScraping1.get_news(word[0])
    dfNews2 = myScraping1.get_news(word[1])
    news = dfNews1.append(dfNews2)
    dfNews = pd.merge(dfNews, news, left_index=True, right_index=True, how='outer')
# for word in keywords:
#     dfNews1 = pd.DataFrame({'A': [1, 2]})
#     dfNews2 = pd.DataFrame({'A': [1, 2,3]})
#     news = dfNews1.append(dfNews2)
#     dfNews = pd.merge(dfNews, news, left_index=True, right_index=True, how='outer')
    
dfNews.columns = ['Bitcoin', 'Ethereum', 'Ripple', 'Litecoin', 'Stellar', 'Neo', 'Monero', 'Ethereum Classic',
            'QTUM', 'ZCash', 'Nano', 'Basic Attention Token', 'Augur', 'Ark', 'Iota', 'Tezos', 'VeChain', 
            'EOS', 'Bcash', 'Decred']

def main():
    # Create an object of methods class & call a method of it
    result_dict = {"asset":[],
                "result_pos":[],
                "result_neg":[],
                "result_neu":[],
                "amount":[],
                'matrix1':[],
                'polarity1':[],         
                'matrix2':[],
                'polarity2':[]
                }
    myScraping = scraping()
    for word in keywords:
        key = 1
        print('start scraping', key)
        key += 1
        date_time_start = datetime.datetime.now()
        times_start = date_time_start.time() 
        dfReddit1 = myScraping.get_reddit(word[0])
        dfTwitter1 = myScraping.get_twitter(word[0])
        dfNews1 = pd.DataFrame(dfNews[word[0]])

        sources1 = [dfReddit1, dfTwitter1, dfNews1]
        # sources1 = [dfReddit1, dfTwitter1]
        data1 = pd.concat(sources1, sort=False)
 
        dfReddit2 = myScraping.get_reddit(word[1])
        dfTwitter2 = myScraping.get_twitter(word[1])

        sources2 = [dfReddit2, dfTwitter2]
        data2 = pd.concat(sources2, sort=False)


        myWrangling1 = wrangling(data1)
        cleanedData1 = myWrangling1.clean()
        myWrangling2 = wrangling(data2)
        cleanedData2 = myWrangling2.clean()

        mySentimental1 = sentimental()
        data_frame1 = mySentimental1.get_sentiment_result(cleanedData1)
        mySentimental2 = sentimental()
        data_frame2 = mySentimental2.get_sentiment_result(cleanedData2)
        result = mySentimental1.caculate_average(data_frame1, data_frame2)

        result_dict["asset"].append(word[1])
        result_dict["result_pos"].append(result['result_pos'])
        result_dict["result_neg"].append(result['result_neg'])
        result_dict["result_neu"].append(result['result_neu'])
        result_dict["amount"].append(result['amount'])
        result_dict["matrix1"].append(result['matrix1'])
        result_dict["polarity1"].append(result['polarity1'])
        result_dict["matrix2"].append(result['matrix2'])
        result_dict["polarity2"].append(result['polarity2'])
        
    return pd.DataFrame(result_dict)




iteration = 0
while True:
    if iteration > 100000000:
        iteration = 0
    date_time_start = datetime.datetime.now()
    times_start = date_time_start.time()  # Gives the time
    
    myScraping1 = scraping()    
    if times_start.minute == 15 or 30 and times_start.second == 0:
        # calling main function
        results = main() 

        date_time_end = datetime.datetime.now()
        times_end = date_time_end.time()
        print('iteration: ', iteration)
        print('end time:', times_end.hour, times_end.minute, times_end.second, times_end.microsecond)
        iteration += 1

        # write into database and update IDs for assets
        # uri = "mongodb://sentiment:BlackHole1@ds153394.mlab.com:53394/cryptoeq"
    
        uri = "mongodb://localhost:27017/local"
        
        client = MongoClient(uri)
        db = client.cryptoeq
        # db = client.test
        print("Mar31")
        # for each keyword
        for j in range(20):
            db.Mar31.insert_one({"result_pos":results['result_pos'][j][0],
                                  "result_neg":results['result_neg'][j][0],
                                  "result_neu":results['result_neu'][j][0],
                                  "amount":results['amount'][j][0],
                                  "matrix1":results['matrix1'][j][0],
                                  "polarity1":results["polarity1"][j][0],
                                  "matrix2":results['matrix2'][j][0],
                                  "polarity2":results["polarity2"][j][0],
                                  "asset":results['asset'][j],
                                  "createdAt": str(date_time_start),
                                  "updatedAt": str(date_time_end)
                                  })


        





