
# Strings

name = 'Terminator2'

genre = 'Action film with Arnold Sharcenegger'

rank = 400

s = 'Name: {movie}\nGenre: {gen}.\nRank - {rnk}'

result2 = 'Name: ' + name + ' ' + genre

result = s.format(movie=name,gen=genre,rnk=rank)

result = f'Movie: {name}. Genre: {genre}. Rank: {rank}'


print(result)

print(result2)

