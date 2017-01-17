## 4. Querying a normalized database ##

portman_query = '''select ceremonies.year, nominations.movie from nominations
inner join ceremonies 
on nominations.ceremony_id == ceremonies.id 
where nominations.nominee == "Natalie Portman";
'''
portman_movies = conn.execute(portman_query).fetchall()
for p in portman_movies:
    print(p)

## 6. Join table ##

five_join_table = conn.cursor().execute('select * from movies_actors limit 5;').fetchall()
five_movies = conn.cursor().execute('select * from movies limit 5;').fetchall()
five_actors = conn.cursor().execute('select * from actors limit 5;').fetchall()
print(five_join_table)
print(five_actors)
print(five_movies)

## 7. Querying a many-to-many relation ##

q = '''
SELECT actors.actor,movies.movie FROM movies
INNER JOIN movies_actors ON movies.id == movies_actors.movie_id
INNER JOIN actors ON movies_actors.actor_id == actors.id
WHERE movies.movie == "The King's Speech";
'''
kings_actors = conn.execute(q).fetchall()
print(kings_actors)

## 8. Practice: querying a many-to-many relation ##

q = '''
select movies.movie, actors.actor from movies
inner join movies_actors on movies.id == movies_actors.movie_id
inner join actors on actors.id == movies_actors.actor_id
where actors.actor == "Natalie Portman";
'''
portman_joins = conn.execute(q).fetchall()
print(portman_joins)