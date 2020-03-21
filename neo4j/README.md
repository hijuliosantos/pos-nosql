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

>match (a:Person)-[:ACTED_IN]->(m:Movie)<-[:DIRECTED]-(d:Person),(a2:Person)-[:ACTED_IN]->(m) where a.name = 'Gene Hackman' return m.title as movie, d.name AS director , a2.name AS `co-actors`

Exercise 5.2: Retrieve particular nodes that have a relationship.

>match (p1:Person)-[:FOLLOWS]-(p2:Person) where p1.name = 'James Thompson' return p1, p2

Exercise 5.3: Modify the query to retrieve nodes that are exactly three hops away.

>match (p1:Person)-[:FOLLOWS*3]-(p2:Person) where p1.name = 'James Thompson' return p1, p2

Exercise 5.4: Modify the query to retrieve nodes that are one and two hops away.

>match (p1:Person)-[:FOLLOWS*1..2]-(p2:Person) where p1.name = 'James Thompson' return p1, p2

Exercise 5.5: Modify the query to retrieve particular nodes that are connected no matter how many hops are required.

>match (p1:Person)-[:FOLLOWS*]-(p2:Person) where p1.name = 'James Thompson' return p1, p2

Exercise 5.6: Specify optional data to be retrieved during the query.

>match (p:Person) where p.name starts with 'Tom' optional match (p)-[:DIRECTED]->(m:Movie) return p.name, m.title

Exercise 5.7: Retrieve nodes by collecting a list.

>match (p:Person)-[:ACTED_IN]->(m:Movie) return p.name as actor, collect(m.title) as `movie list`

Exercise 5.9: Retrieve nodes as lists and return data associated with the corresponding lists.

>match (p:Person)-[:REVIEWED]->(m:Movie) return m.title as movie, count(p) as numReviews, collect(p.name) as reviewers

Exercise 5.10: Retrieve nodes and their relationships as lists.

>match (d:Person)-[:DIRECTED]->(m:Movie)<-[:ACTED_IN]-(a:Person) return d.name as director, count(a) as `number actors` , collect(a.name) as `actors worked with`

Exercise 5.11: Retrieve the actors who have acted in exactly five movies.

>match (a:Person)-[:ACTED_IN]->(m:Movie) with  a, count(a) as numMovies, collect(m.title) as movies where numMovies = 5 return a.name, movies
 
Exercise 5.12: Retrieve the movies that have at least 2 directors with other optional data.

> match (m:Movie) with m, size((:Person)-[:DIRECTED]->(m)) as directors where directors >= 2 optional match (p:Person)-[:REVIEWED]->(m) return  m.title, p.name

</br>

Exercise 6.1: Execute a query that returns duplicate records.

>match (m:Movie) with m, size((:Person)-[:DIRECTED]->(m)) as directors where directors >= 2 optional match (p:Person)-[:REVIEWED]->(m) return  m.title, p.name

Exercise 6.2: Modify the query to eliminate duplication

>match (a:Person)-[:ACTED_IN]->(m:Movie) where m.released >= 1990 and m.released < 2000 return  m.released, collect(m.title), collect(a.name)

Exercise 6.3: Modify the query to eliminate more duplication.

>match (a:Person)-[:ACTED_IN]->(m:Movie) where m.released >= 1990 and m.released < 2000 return  m.released, collect(distinct m.title), collect(a.name)

Exercise 6.4: Sort results returned.

>match (a:Person)-[:ACTED_IN]->(m:Movie) where m.released >= 1990 and m.released < 2000 return  m.released, collect(distinct m.title), collect(a.name) order by m.released desc

Exercise 6.5: Retrieve the top 5 ratings and their associated movies.

>match (:Person)-[r:REVIEWED]->(m:Movie) return  m.title as movie, r.rating as rating order by r.rating desc limit 5

Exercise 6.6: Retrieve all actors that have not appeared in more than 3 movies.

>match (a:Person)-[:ACTED_IN]->(m:Movie) with  a,  count(a) as numMovies, collect(m.title) as movies where numMovies <= 3 return a.name, movies

</br>

Exercise 7.1: Collect and use lists.

>match (a:Person)-[:ACTED_IN]->(m:Movie),(m)<-[:PRODUCED]-(p:Person) with  m, collect(distinct a.name) as cast, collect(distinct p.name) as producers return distinct m.title, cast, producers order by size(cast)

Exercise 7.2: Collect a list.

>match (p:Person)-[:ACTED_IN]->(m:Movie) with p, collect(m) as movies where size(movies)  > 5 return p.name, movies

Exercise 7.3: Unwind a list.

>match (p:Person)-[:ACTED_IN]->(m:Movie) with p, collect(m) AS movies where size(movies)  > 5 with p, movies unwind movies as movie return p.name, movie.title

Exercise 7.4: Perform a calculation with the date type.

>match (a:Person)-[:ACTED_IN]->(m:Movie) where a.name = 'Tom Hanks' return  m.title, m.released, date().year  - m.released as yearsAgoReleased, m.released  - a.born as `age of Tom` order by yearsAgoReleased

</br>

Exercise 8.1: Create a Movie node.

>create (:Movie {title: 'Forrest Gump'})

Exercise 8.2: Retrieve the newly-created node.

>match (m:Movie) where m.title = 'Forrest Gump' return m

Exercise 8.3: Create a Person node.

>create (:Person {name: 'Robin Wright'})

Exercise 8.4: Retrieve the newly-created node.

>match (p:Person) where p.name = 'Robin Wright' return p

Exercise 8.5: Add a label to a node.

>match (m:Movie) where m.released < 2010 set m:OlderMovie return distinct labels(m)

Exercise 8.6: Retrieve the node using the new label.

>match (m:OlderMovie) return m.title, m.released

Exercise 8.7: Add the Female label to selected nodes.

>match (p:Person) where p.name starts with 'Robin' set p:Female

Exercise 8.8: Retrieve all Female nodes.

>match (p:Female) return p.name

Exercise 8.9: Remove the Female label from the nodes that have this label.

>match (p:Female) remove p:Female

Exercise 8.10: View the current schema of the graph.

>call db.schema

Exercise 8.11: Add properties to a movie.

>match (m:Movie) where m.title = 'Forrest Gump'
set m:OlderMovie,
    m.released = 1994,
    m.tagline = "Life is like a box of chocolates...you never know what you're gonna get.",
    m.lengthInMinutes = 142

Exercise 8.12: Retrieve an OlderMovie node to confirm the label and properties.

>match (m:OlderMovie) where m.title = 'Forrest Gump' return m

Exercise 8.13: Add properties to the person, Robin Wright.

> match (p:Person) where p.name = 'Robin Wright' set p.born = 1966, p.birthPlace = 'Dallas'

Exercise 8.14: Retrieve an updated Person node.

>match (p:Person) where p.name = 'Robin Wright' return p

Exercise 8.15: Remove a property from a Movie node.

>match (m:Movie) where m.title = 'Forrest Gump' set m.lengthInMinutes = null

Exercise 8.16: Retrieve the node to confirm that the property has been removed.

>match (m:Movie) where m.title = 'Forrest Gump' return m

Exercise 8.17: Remove a property from a Person node.

>match (p:Person) where p.name = 'Robin Wright' remove p.birthPlace

Exercise 8.18: Retrieve the node to confirm that the property has been removed.

>match (p:Person) where p.name = 'Robin Wright' return p

</br>

Exercise 9.1: Create ACTED_IN relationships.

>match (m:Movie) where m.title = 'Forrest Gump' match (p:Person) where p.name = 'Tom Hanks' or p.name = 'Robin Wright' or p.name = 'Gary Sinise' create (p)-[:ACTED_IN]->(m)

Exercise 9.2: Create DIRECTED relationships.

>match (m:Movie) where m.title = 'Forrest Gump' match (p:Person) where p.name = 'Robert Zemeckis' create (p)-[:DIRECTED]->(m)

Exercise 9.3: Create a HELPED relationship.

>match (p1:Person) where p1.name = 'Tom Hanks' match (p2:Person) where p2.name = 'Gary Sinise' create (p1)-[:HELPED]->(p2)

Exercise 9.4: Query nodes and new relationships.

>match (p:Person)-[rel]-(m:Movie) where m.title = 'Forrest Gump' return p, rel, m

Exercise 9.5: Add properties to relationships.

>match (p:Person)-[rel:ACTED_IN]->(m:Movie) where m.title = 'Forrest Gump'
set rel.roles =
case p.name
  when 'Tom Hanks' then ['Forrest Gump']
  when 'Robin Wright' then ['Jenny Curran']
  when 'Gary Sinise' then ['Lieutenant Dan Taylor']
end

Exercise 9.6: Add a property to the HELPED relationship.

>match (p1:Person)-[rel:HELPED]->(p2:Person) where p1.name = 'Tom Hanks' and p2.name = 'Gary Sinise' set rel.research = 'war history'

Exercise 9.7: View the current list of property keys in the graph.

>call db.propertyKeys

Exercise 9.8: View the current schema of the graph.

>call db.schema

Exercise 9.9: Retrieve the names and roles for actors.

>match (p:Person)-[rel:ACTED_IN]->(m:Movie) where m.title = 'Forrest Gump' return p.name, rel.roles

Exercise 9.10: Retrieve information about any specific relationships.

>match (p1:Person)-[rel:HELPED]-(p2:Person) return p1.name, rel, p2.name

Exercise 9.11: Modify a property of a relationship.

>match (p:Person)-[rel:ACTED_IN]->(m:Movie) where m.title = 'Forrest Gump' and p.name = 'Gary Sinise' set rel.roles =['Lt. Dan Taylor']

Exercise 9.12: Remove a property from a relationship.

>match (p1:Person)-[rel:HELPED]->(p2:Person) where p1.name = 'Tom Hanks' AND p2.name = 'Gary Sinise' remove rel.research

Exercise 9.13: Confirm that your modifications were made to the graph.

>match (p:Person)-[rel:ACTED_IN]->(m:Movie) where m.title = 'Forrest Gump' return p, rel, m

</br>

Exercise 10.1: Delete a relationship.

>match (:Person)-[rel:HELPED]-(:Person) delete rel

Exercise 10.2: Confirm that the relationship has been deleted.

>match (:Person)-[rel:HELPED]-(:Person) return rel

Exercise 10.3: Retrieve a movie and all of its relationships.

>match (p:Person)-[rel]-(m:Movie) where m.title = 'Forrest Gump' return p, rel, m

Exercise 10.4: Try deleting a node without detaching its relationships.

>match (m:Movie) where m.title = 'Forrest Gump' delete m

Exercise 10.5: Delete a Movie node, along with its relationships.

>match (m:Movie) where m.title = 'Forrest Gump' detach delete m

Exercise 10.6: Confirm that the Movie node has been deleted.

>match (p:Person)-[rel]-(m:Movie) where m.title = 'Forrest Gump' return p, rel, m
















