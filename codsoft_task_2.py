import pandas as pd
data = {
    'Title': ['Titanic', 'Martian', 'Life', 'Avengers', 'BatMan'],
    'Genre': ['Action', 'Adventure', 'Action', 'Comedy', 'Adventure'],
    'Description': [
        'Action-packed movie with thrilling scenes.',
        'An adventure movie set in a fantasy world.',
        'Fast-paced action movie with intense battles.',
        'A hilarious comedy that will make you laugh.',
        'Epic adventure film with breathtaking landscapes.'
    ]
}
df = pd.DataFrame(data)
def cosine_similarity(vec1, vec2):
    genre1 = set(vec1.lower().split())
    genre2 = set(vec2.lower().split())
    intersection = genre1.intersection(genre2)
    union = genre1.union(genre2)
    return len(intersection) / len(union)
def get_recommendations(movie_title, num_recommendations=5):
    movie = df[df['Title'] == movie_title]
    if movie.empty:
        return []  # Movie not found

    movie_genre = movie['Genre'].values[0]

    similarities = []
    for index, row in df.iterrows():
        if row['Title'] != movie_title:
            similarity = cosine_similarity(movie_genre, row['Genre'])
            similarities.append((row['Title'], similarity))

    similarities.sort(key=lambda x: x[1], reverse=True)

    recommended_movies = [movie[0] for movie in similarities[:num_recommendations]]
    return recommended_movies

movie_title = 'Titanic'
recommendations = get_recommendations(movie_title, num_recommendations=3)
if recommendations:
    print(f"Recommendations for '{movie_title}':")
    for movie in recommendations:
        print(movie)
else:
    print(f"'{movie_title}' not found in the dataset.")
