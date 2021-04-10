# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 23:11:56 2021

@author: kartik.sharma10
"""

# import libraties
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer


class Recommend:
    
    def __init__(self):
        self.data = pickle.load(open('pickle/processed_data.pkl','rb'))
        self.user_final_rating = pickle.load(open('pickle/user_final_rating.pkl','rb'))
        self.model = pickle.load(open('pickle/lr.pkl','rb'))
        
        
    def getTopProducts(self, user):
        items=None
        try:
            items = self.user_final_rating.loc[user].sort_values(ascending=False)[0:20].index
        except:
            return [-1]
        features = pickle.load(open('pickle/feature.pkl','rb'))
        vectorizer = TfidfVectorizer(vocabulary = features)
        temp=self.data[self.data.id.isin(items)]
        X = vectorizer.fit_transform(temp['processed'])
        temp=temp[['id']]
        temp['prediction'] = self.model.predict(X)
        temp=temp.groupby('id').sum()
        temp['pos_percent']=temp.apply(lambda x: x['prediction']/sum(x), axis=1)
        final_list=temp.sort_values('pos_percent', ascending=False).iloc[:5,:].index
        return self.data[self.data.id.isin(final_list)][['id', 'brand',
                              'categories', 'manufacturer', 'name']].drop_duplicates()
    
        
        
#r =Recommend()
#li = r.getTopProducts('jygibri')


    
    