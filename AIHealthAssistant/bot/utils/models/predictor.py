import pickle
import spacy
import pandas as pd
import numpy as np

nlp = spacy.load('ru_core_news_lg')
df_concat = pd.read_csv('./utils/models/df_concat.csv', index_col=0)


def load_model(fname):
    model_data = open(fname, "rb").read()
    model = pickle.loads(model_data)

    return model


def get_prediction(model, query: str):
    query = query.lower()
    query = nlp(query)

    query_vec = []
    for symp in df_concat.columns[1:]:
        query_vec.append(int(query.similarity(nlp(symp)) > 0.4))

    print(query_vec.count(1))

    res = model.predict([
        np.array(query_vec)
    ])

    return res
