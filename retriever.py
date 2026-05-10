from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def search_chunks(chunks, keyword):
    results = []

    for chunk in chunks:
        if keyword in chunk:
            results.append(chunk)

    return results


def semantic_search(chunks, question, top_k=3, min_score=0.05):
    #vectorizer = TfidfVectorizer() #suitable for English

    vectorizer = TfidfVectorizer(analyzer="char", ngram_range=(2,4))  #suitable for Chinese

    all_texts =  chunks + [question]

    tfidf_matrix = vectorizer.fit_transform(all_texts)

    chunk_vectors = tfidf_matrix[:-1]
    question_vector = tfidf_matrix[-1]

    similarities = cosine_similarity(question_vector,chunk_vectors)
    similarities = similarities[0]

    top_indices = similarities.argsort()[-top_k:][::-1]

    results = []

    for index in top_indices:
        if similarities[index] > min_score:
            results.append({
                "index": index,
                "score": similarities[index],
                "text": chunks[index]
            })

    return results