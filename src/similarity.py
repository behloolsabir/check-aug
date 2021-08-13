from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


def getCosineSimilarity(model, sentences):
    sentence_embeddings = model.encode(sentences)
    return cosine_similarity([sentence_embeddings[0]], sentence_embeddings[1:])

def getSimilarityScores(model, data):
    df = pd.DataFrame()
    count = 1
    for base_sent in data:
        sentences = [base_sent] + data[base_sent]
        print(f"{count}: {base_sent}")
        scores = getCosineSimilarity(model, sentences)
        temp_df = pd.DataFrame()
        temp_df['aug'] = data[base_sent]
        temp_df['score'] = scores.tolist()[0]
        temp_df['base'] = base_sent
        df = df.append(temp_df, ignore_index=True)
        count += 1
    return df
