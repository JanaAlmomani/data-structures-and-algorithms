def sort_by_year(movies):
    return sorted(movies, key=lambda movie: movie['year'], reverse=True)

def sort_by_title(movies):
    articles = ['A', 'An', 'The']
    return sorted(movies, key=lambda movie: movie['title'].lstrip(' '.join(articles)))

movies = [

    {'title': 'Movie 1', 'year': 2022, 'genres': ['Genre 1', 'Genre 2']},
    {'title': 'Movie 2', 'year': 2021, 'genres': ['Genre 2', 'Genre 3']},
    {'title': 'Movie 3', 'year': 2023, 'genres': ['Genre 1', 'Genre 3']}

]

print(sort_by_year(movies) )
print("\n")
print(sort_by_title(movies))
