Exercise 1.1: Retrieve all nodes from the database</br>
>match (n) return n

Exercise 1.2: Examine the schema of your database

>╒══════════════════════════════════════════════════════════════════════╤═══════════════════╕
│"nodes"                                                               │"relationships"    │
╞══════════════════════════════════════════════════════════════════════╪═══════════════════╡
│[{"indexes":[],"name":"Movie","constraints":[]},{"indexes":[],"name":"│[{},{},{},{},{},{}]│
│Person","constraints":[]}]                                            │                   │
└──────────────────────────────────────────────────────────────────────┴───────────────────┘

Exercise 1.3: Retrieve all Person nodes.
>match (p:Person) return p

Exercise 1.4: Retrieve all Movie nodes.
>match (m:Movie) RETURN m

</br>

Exercise 2.1: Retrieve all movies that were released in a specific year
>match (m:Movie {released:1999}) return m

Exercise 2.2: View the retrieved results as a table.

>╒══════════════════════════════════════════════════════════════════════╕
│"m"                                                                   │
╞══════════════════════════════════════════════════════════════════════╡
│{"title":"The Matrix","tagline":"Welcome to the Real World","released"│
│:1999}                                                                │
├──────────────────────────────────────────────────────────────────────┤
│{"title":"Snow Falling on Cedars","tagline":"First loves last. Forever│
│.","released":1999}                                                   │
├──────────────────────────────────────────────────────────────────────┤
│{"title":"The Green Mile","tagline":"Walk a mile you'll never forget."│
│,"released":1999}                                                     │
├──────────────────────────────────────────────────────────────────────┤
│{"title":"Bicentennial Man","tagline":"One robot's 200 year journey to│
│ become an ordinary man.","released":1999}                            │
└──────────────────────────────────────────────────────────────────────┘

Exercise 2.3: Query the database for all property keys.

>CALL db.propertyKeys

Exercise 2.4: Retrieve all Movies released in a specific year, returning their titles.

>match (m:Movie {released:1999}) return m.title

Exercise 2.5: Display title, released, and tagline values for every Movie node in the graph.

>match (m:Movie ) return m.title, m.released, m.tagline

Exercise 2.6: Display more user-friendly headers in the table

>match (m:Movie) return m.title as Title, m.released as Released, m.tagline as TagLine

</br>

Exercise 3.1: Display the schema of the database.

>CALL db.schema()

Exercise 3.2: Retrieve all people who wrote the movie Speed Racer.

>match (p:Person)-[:WROTE]->(:Movie {title: 'Speed Racer'}) return p.name

Exercise 3.3: Retrieve all movies that are connected to the person, Tom Hanks.

>match (m:Movie)<--(:Person{name: 'Tom Hanks'}) return m.title

Exercise 3.4: Retrieve information about the relationships Tom Hanks had with the set of movies retrieved earlier.

>match (m:Movie)-[rel]-(:Person {name: 'Tom Hanks'}) return m.title, type(rel)

Exercise 3.5: Retrieve information about the roles that Tom Hanks acted in.
>match (m:Movie)-[rel:ACTED_IN]-(:Person {name: 'Tom Hanks'}) return m.title, rel.roles

</br>

Exercise 4.1: Retrieve all movies that Tom Cruise acted in.

>match (p:Person)-[:ACTED_IN]->(m:Movie) where p.name = 'Tom Cruise' return m.title

Exercise 4.2: Retrieve all people that were born in the 70’s.

>match (p:Person) where p.born >= 1970 and p.born < 1980 return p

Exercise 4.3: Retrieve the actors who acted in the movie The Matrix who were born after 1960.

>match (p:Person)-[:ACTED_IN]->(m:Movie) where p.born >= 1960 and m.title = 'The Matrix' return p

Exercise 4.4: Retrieve all movies by testing the node label and a property.

>match (m) where m:Movie and m.released = 1999  return m

Exercise 4.5: Retrieve all people that wrote movies by testing the relationship between two nodes.

>match (p)-[rel]->(m) where p:Person and type(rel) = 'WROTE' and m:Movie return a,m

Exercise 4.6: Retrieve all people in the graph that do not have a property.

>match (p:Person) where not exists(p.born) return p

Exercise 4.7: Retrieve all people related to movies where the relationship has a property.

>match(p:Person)-[rel]->(m:Movie) where exists(rel.rating) return p.name,m.title,rel.rating

Exercise 4.8: Retrieve all actors whose name begins with James.

>match(p:Person)-[:ACTED_IN]->(m:Movie) where p.name starts with 'James' return p.name

Exercise 4.9: Retrieve all REVIEW relationships from the graph with filtered results.

>match (p:Person)-[r:REVIEWED]->(m:Movie) where r.summary contains 'but' return  m.title, r.summary

Exercise 4.10: Retrieve all people who have produced a movie, but have not directed a movie.

>match (p:Person)-[:PRODUCED]->(m:Movie) where not ((p)-[:DIRECTED]->(:Movie)) return p.name,m.title

Exercise 4.11: Retrieve the movies and their actors where one of the actors also directed the movie.

>match (p1:Person)-[:ACTED_IN]->(m:Movie)<-[:ACTED_IN]-(p2:Person) where exists((p2)-[:DIRECTED]->(m)) return p1.name as Actor, p2.name as AD, m.title as Movie

Exercise 4.12: Retrieve all movies that were released in a set of years.

>match(m:Movie) where m.released in [1990, 1992, 2000] return m

Exercise 4.13: Retrieve the movies that have an actor’s role that is the name of the movie.

>match(p:Person)-[r:ACTED_IN]->(m:Movie) where m.title in r.roles return m.title,r.roles

</br>

Exercise 5.1: Retrieve data using multiple MATCH patterns

Exercise 5.2: Retrieve particular nodes that have a relationship.

Exercise 5.3: Modify the query to retrieve nodes that are exactly three hops away.

Exercise 5.4: Modify the query to retrieve nodes that are one and two hops away.

Exercise 5.5: Modify the query to retrieve particular nodes that are connected no matter how many hops are required.


Exercise 5.6: Specify optional data to be retrieved during the query.


Exercise 5.7: Retrieve nodes by collecting a list.


Exercise 5.9: Retrieve nodes as lists and return data associated with the corresponding lists.


Exercise 5.10: Retrieve nodes and their relationships as lists.


Exercise 5.11: Retrieve the actors who have acted in exactly five movies.

 
Exercise 5.12: Retrieve the movies that have at least 2 directors with other optional data.
























