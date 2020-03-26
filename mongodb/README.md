# Exercício 1 - Aquecendo com os pets

1.Adicione outro Peixe e um Hamster com nome Frodo

>db.pets.insert({name: "Frodo", species: "Peixe"})</br>
WriteResult({ "nInserted" : 1 })</br></br>
>db.pets.insert({name: "Frodo", species: "Hamster"})</br>
WriteResult({ "nInserted" : 1 })


2. Faça uma contagem dos pets na coleção
>db.pets.count()</br>
8

3. Retorne apenas um elemento o método prático possível
>db.pets.findOne()</br>
{
        "_id" : ObjectId("5e61b49fc42d8266db1e17b0"),
        "name" : "Mike",
        "species" : "Hamster"
}

4. Identifique o ID para o Gato Kilha
> db.pets.find({$and: [{species: "Gato"}, {name: "Kilha"}]},{_id:1})</br>
{ "_id" : ObjectId("5e61b49fc42d8266db1e17b2") }

5. Faça uma busca pelo ID e traga o Hamster Mike

> db.pets.find({_id: ObjectId("5e61b49fc42d8266db1e17b0")})</br>
{ "_id" : ObjectId("5e61b49fc42d8266db1e17b0"), "name" : "Mike", "species" : "Hamster" }

6. Use o find para trazer todos os Hamsters
> db.pets.find({species:"Hamster"})</br>
{ "_id" : ObjectId("5e61b49fc42d8266db1e17b0"), "name" : "Mike", "species" : "Hamster" }</br>
{ "_id" : ObjectId("5e61b54ec42d8266db1e17b7"), "name" : "Frodo", "species" : "Hamster" }

7. Use o find para listar todos os pets com nome Mike
> db.pets.find({name:"Mike"})</br>
{ "_id" : ObjectId("5e61b49fc42d8266db1e17b0"), "name" : "Mike", "species" : "Hamster" }</br>
{ "_id" : ObjectId("5e61b49fc42d8266db1e17b3"), "name" : "Mike", "species" : "Cachorro" }

8. Liste apenas o documento que é um Cachorro chamado Mike
> db.pets.find({$and: [{species:"Cachorro"},{"name": "Mike"}]})</br>
{ "_id" : ObjectId("5e61b49fc42d8266db1e17b3"), "name" : "Mike", "species" : "Cachorro" }


# Exercício 2 - Mama mia!

1. Liste/Conte todas as pessoas que tem exatamente 99 anos. Você pode usar um count para indicar a quantidade.
> db.italians.find({age: 99}).count()</br>
0

2. Identifique quantas pessoas são elegíveis atendimento prioritário (pessoas com mais de 65 anos)
> db.italians.find({age: {$gt: 65}}).count()</br>
1825

3. Identifique todos os jovens (pessoas entre 12 a 18 anos).
> db.italians.find({$and: [{age: {$gte: 13}}, {age: {$lte: 18}}]}).count()</br>
743

4. Identifique quantas pessoas tem gatos, quantas tem cachorro e quantas não tem nenhum dos dois

> db.italians.find({cat: {$exists: true}}).count()</br>
4045</br>
> db.italians.find({dog: {$exists: true}}).count()</br>
5893</br>
> db.italians.find({$and: [{dog: null}, {cat: null}]}).count()</br>
2426

5. Liste/Conte todas as pessoas acima de 60 anos que tenham gato
> db.italians.find({$and: [{age: {$gt: 60}}, {cat: {$exists: true}}]}).count()</br>
1425

6. Liste/Conte todos os jovens com cachorro
> db.italians.find({$and: [{age: {$gte: 13}}, {age: {$lte: 18}}, {dog: {$exists: true}}]}).count()</br>
302

7. Utilizando o $where, liste todas as pessoas que tem gato e cachorro
> db.italians.find({$where: function() { return this.cat && this.dog}},{"firstname":1,"cat":1,"dog":1,"_id":0})</br>
{ "firstname" : "Tiziana", "cat" : { "name" : "Vincenzo", "age" : 13 }, "dog" : { "name" : "Giulia", "age" : 14 } }
{ "firstname" : "Alberto", "cat" : { "name" : "Rosa", "age" : 0 }, "dog" : { "name" : "Gabiele", "age" : 7 } }
{ "firstname" : "Cristian", "cat" : { "name" : "Chiara", "age" : 10 }, "dog" : { "name" : "Carlo", "age" : 4 } }
{ "firstname" : "Cristian", "cat" : { "name" : "Martina", "age" : 0 }, "dog" : { "name" : "Maurizio", "age" : 10 } }
{ "firstname" : "Serena", "cat" : { "name" : "Marco", "age" : 5 }, "dog" : { "name" : "Giorgio", "age" : 6 } }
{ "firstname" : "Giusy", "cat" : { "name" : "Maria", "age" : 12 }, "dog" : { "name" : "Stefano", "age" : 16 } }
{ "firstname" : "Massimiliano", "cat" : { "name" : "Angelo", "age" : 10 }, "dog" : { "name" : "Eleonora", "age" : 1 } }
{ "firstname" : "Michela", "cat" : { "name" : "Michele", "age" : 6 }, "dog" : { "name" : "Paola", "age" : 8 } }
{ "firstname" : "Simone", "cat" : { "name" : "Stefania", "age" : 8 }, "dog" : { "name" : "Antonella", "age" : 12 } }
{ "firstname" : "Alessandra", "cat" : { "name" : "Rita", "age" : 3 }, "dog" : { "name" : "Cristina", "age" : 8 } }
{ "firstname" : "Raffaele", "cat" : { "name" : "Cristian", "age" : 3 }, "dog" : { "name" : "Elisabetta", "age" : 3 } }
{ "firstname" : "Rita", "cat" : { "name" : "Anna", "age" : 9 }, "dog" : { "name" : "Angelo", "age" : 11 } }
{ "firstname" : "Sara", "cat" : { "name" : "Stefano", "age" : 7 }, "dog" : { "name" : "Mauro", "age" : 2 } }
{ "firstname" : "Alessio", "cat" : { "name" : "Sergio", "age" : 14 }, "dog" : { "name" : "Giovanni", "age" : 9 } }
{ "firstname" : "Salvatore", "cat" : { "name" : "Elisabetta", "age" : 4 }, "dog" : { "name" : "Giuseppe", "age" : 12 } }
{ "firstname" : "Alessio", "cat" : { "name" : "Claudia", "age" : 12 }, "dog" : { "name" : "Elisabetta", "age" : 14 } }
{ "firstname" : "Alex", "cat" : { "name" : "Salvatore", "age" : 8 }, "dog" : { "name" : "Alessandro", "age" : 12 } }
{ "firstname" : "Serena", "cat" : { "name" : "Cristina", "age" : 6 }, "dog" : { "name" : "Lorenzo", "age" : 2 } }
{ "firstname" : "Stefania", "cat" : { "name" : "Domenico", "age" : 4 }, "dog" : { "name" : "Mirko", "age" : 0 } }
{ "firstname" : "Fabio", "cat" : { "name" : "Paolo", "age" : 7 }, "dog" : { "name" : "Giovanni", "age" : 4 } }
Type "it" for more

8. Liste todas as pessoas mais novas que seus respectivos gatos.
> db.italians.find({ "$expr": { "$lt": [ "$age" , "$cat.age" ] } }, {"firstname":1,"age":1,"cat.age":1})</br>
{ "_id" : ObjectId("5e65aeb430173f6dff00087c"), "firstname" : "Marco", "age" : 8, "cat" : { "age" : 13 } }
{ "_id" : ObjectId("5e65aeb430173f6dff000884"), "firstname" : "Barbara", "age" : 1, "cat" : { "age" : 9 } }
{ "_id" : ObjectId("5e65aeb430173f6dff000885"), "firstname" : "Gabiele", "age" : 9, "cat" : { "age" : 16 } }
{ "_id" : ObjectId("5e65aeb430173f6dff000896"), "firstname" : "Giusy", "age" : 3, "cat" : { "age" : 12 } }
{ "_id" : ObjectId("5e65aeb430173f6dff0008a3"), "firstname" : "Simone", "age" : 0, "cat" : { "age" : 8 } }
{ "_id" : ObjectId("5e65aeb430173f6dff0008b0"), "firstname" : "Rita", "age" : 5, "cat" : { "age" : 9 } }
{ "_id" : ObjectId("5e65aeb430173f6dff0008b5"), "firstname" : "Sara", "age" : 0, "cat" : { "age" : 7 } }
{ "_id" : ObjectId("5e65aeb430173f6dff0008bd"), "firstname" : "Alessio", "age" : 1, "cat" : { "age" : 12 } }
{ "_id" : ObjectId("5e65aeb430173f6dff0008c1"), "firstname" : "Monica", "age" : 3, "cat" : { "age" : 9 } }
{ "_id" : ObjectId("5e65aeb430173f6dff0008cf"), "firstname" : "Giusy", "age" : 0, "cat" : { "age" : 14 } }
{ "_id" : ObjectId("5e65aeb430173f6dff0008f9"), "firstname" : "Gianni", "age" : 0, "cat" : { "age" : 9 } }
{ "_id" : ObjectId("5e65aeb430173f6dff00090a"), "firstname" : "Emanuele", "age" : 0, "cat" : { "age" : 8 } }
{ "_id" : ObjectId("5e65aeb430173f6dff00092e"), "firstname" : "Gianluca", "age" : 1, "cat" : { "age" : 9 } }
{ "_id" : ObjectId("5e65aeb430173f6dff000936"), "firstname" : "Veronica", "age" : 15, "cat" : { "age" : 16 } }
{ "_id" : ObjectId("5e65aeb430173f6dff00094a"), "firstname" : "Enrico", "age" : 7, "cat" : { "age" : 10 } }
{ "_id" : ObjectId("5e65aeb430173f6dff000973"), "firstname" : "Sonia", "age" : 2, "cat" : { "age" : 6 } }
{ "_id" : ObjectId("5e65aeb430173f6dff0009a2"), "firstname" : "Michele", "age" : 3, "cat" : { "age" : 5 } }
{ "_id" : ObjectId("5e65aeb430173f6dff0009bc"), "firstname" : "Cristina", "age" : 8, "cat" : { "age" : 13 } }
{ "_id" : ObjectId("5e65aeb430173f6dff0009c6"), "firstname" : "Fabio", "age" : 14, "cat" : { "age" : 17 } }
{ "_id" : ObjectId("5e65aeb530173f6dff0009ea"), "firstname" : "Alessio", "age" : 11, "cat" : { "age" : 16 } }
Type "it" for more

9 Liste as pessoas que tem o mesmo nome que seu bichano (gatou ou cachorro)
> db.italians.find({$or: [{"$expr": { "$eq": [ "$firstname" , "$cat.name" ]}}, {"$expr": { "$eq": [ "$firstname" , "$dog.name" ]}}]},{"firstname":1,"dog.name":1,"cat.name":1,"_id":0})</br>

{ "firstname" : "Sonia", "cat" : { "name" : "Sonia" } }
{ "firstname" : "Emanuela", "cat" : { "name" : "Giorgio" }, "dog" : { "name" : "Emanuela" } }
{ "firstname" : "Antonio", "cat" : { "name" : "Daniela" }, "dog" : { "name" : "Antonio" } }
{ "firstname" : "Manuela", "cat" : { "name" : "Alessandro" }, "dog" : { "name" : "Manuela" } }
{ "firstname" : "Simone", "dog" : { "name" : "Simone" } }
{ "firstname" : "Carlo", "cat" : { "name" : "Carlo" } }
{ "firstname" : "Mattia", "cat" : { "name" : "Mattia" } }
{ "firstname" : "Alessio", "cat" : { "name" : "Sergio" }, "dog" : { "name" : "Alessio" } }
{ "firstname" : "Davide", "cat" : { "name" : "Davide" }, "dog" : { "name" : "Maurizio" } }
{ "firstname" : "Andrea", "cat" : { "name" : "Andrea" } }
{ "firstname" : "Emanuela", "cat" : { "name" : "Emanuela" }, "dog" : { "name" : "Claudio" } }
{ "firstname" : "Rosa", "cat" : { "name" : "Paolo" }, "dog" : { "name" : "Rosa" } }
{ "firstname" : "Alessandra", "dog" : { "name" : "Alessandra" } }
{ "firstname" : "Mirko", "cat" : { "name" : "Mirko" } }
{ "firstname" : "Andrea", "dog" : { "name" : "Andrea" } }
{ "firstname" : "Michele", "cat" : { "name" : "Monica" }, "dog" : { "name" : "Michele" } }
{ "firstname" : "Barbara", "cat" : { "name" : "Barbara" } }
{ "firstname" : "Rosa", "cat" : { "name" : "Rosa" }, "dog" : { "name" : "Sonia" } }
{ "firstname" : "Paola", "cat" : { "name" : "Paola" } }
{ "firstname" : "Laura", "cat" : { "name" : "Laura" }, "dog" : { "name" : "Carlo" } }
Type "it" for more

10. Projete apenas o nome e sobrenome das pessoas com tipo de sangue de fator RH negativo
> db.italians.find({bloodType: {$in: ["A-", "B-", "AB-", "O-"]}}, {firstname:1, surname:1, _id:0})</br>

{ "firstname" : "Eleonora", "surname" : "Giuliani" }
{ "firstname" : "Filipo", "surname" : "Villa" }
{ "firstname" : "Tiziana", "surname" : "Colombo" }
{ "firstname" : "Federico", "surname" : "Vitale" }
{ "firstname" : "Fabrizio", "surname" : "Valentini" }
{ "firstname" : "Teresa", "surname" : "Serra" }
{ "firstname" : "Cinzia", "surname" : "Palmieri" }
{ "firstname" : "Roberta", "surname" : "Sanna" }
{ "firstname" : "Domenico", "surname" : "Benedetti" }
{ "firstname" : "Antonella", "surname" : "Morelli" }
{ "firstname" : "Monica", "surname" : "Marino" }
{ "firstname" : "Marco", "surname" : "De Santis" }
{ "firstname" : "Simona", "surname" : "Rossetti" }
{ "firstname" : "Giorgia", "surname" : "Cattaneo" }
{ "firstname" : "Federico", "surname" : "Caruso" }
{ "firstname" : "Fabio", "surname" : "Marino" }
{ "firstname" : "Veronica", "surname" : "Colombo" }
{ "firstname" : "Elisabetta", "surname" : "Marino" }
{ "firstname" : "Eleonora", "surname" : "Pagano" }
{ "firstname" : "Giovanna", "surname" : "Palumbo" }
Type "it" for more

11. Projete apenas os animais dos italianos. Devem ser listados os animais com nome e idade. Não mostre o identificado do mongo (ObjectId)
  
> db.italians.find({$where: "this.cat || this.dog"}, {"cat.name":1,"cat.age": 1, "dog.name":1, "dog.age":1,_id:0})</br>

{ "cat" : { "name" : "Valeira", "age" : 17 } }
{ "cat" : { "name" : "Monica", "age" : 13 } }
{ "cat" : { "name" : "Vincenzo", "age" : 14 }, "dog" : { "name" : "Elena", "age" : 4 } }
{ "cat" : { "name" : "Mattia", "age" : 2 } }
{ "dog" : { "name" : "Alessandra", "age" : 14 } }
{ "dog" : { "name" : "Domenico", "age" : 16 } }
{ "cat" : { "name" : "Pietro", "age" : 3 } }
{ "cat" : { "name" : "Tiziana", "age" : 0 }, "dog" : { "name" : "Gianluca", "age" : 1 } }
{ "cat" : { "name" : "Mauro", "age" : 1 }, "dog" : { "name" : "Michele", "age" : 8 } }
{ "cat" : { "name" : "Matteo", "age" : 5 }, "dog" : { "name" : "Anna", "age" : 16 } }
{ "dog" : { "name" : "Fabio", "age" : 5 } }
{ "cat" : { "name" : "Paola", "age" : 17 }, "dog" : { "name" : "Mauro", "age" : 4 } }
{ "dog" : { "name" : "Mauro", "age" : 4 } }
{ "cat" : { "name" : "Cinzia", "age" : 3 }, "dog" : { "name" : "Sabrina", "age" : 9 } }
{ "dog" : { "name" : "Alex", "age" : 15 } }
{ "dog" : { "name" : "Angela", "age" : 6 } }
{ "cat" : { "name" : "Roberta", "age" : 9 } }
{ "cat" : { "name" : "Mario", "age" : 15 }, "dog" : { "name" : "Vincenzo", "age" : 15 } }
{ "cat" : { "name" : "Giulia", "age" : 6 }, "dog" : { "name" : "Emanuele", "age" : 16 } }
{ "dog" : { "name" : "Federico", "age" : 11 } }
Type "it" for more

12. Quais são as 5 pessoas mais velhas com sobrenome Rossi?
> db.italians.find({surname:"Rossi"}).limit(5).sort({"age":-1})</br>

{ "_id" : ObjectId("5e644390ee36625be4c9a55e"), "firstname" : "Fabio", "surname" : "Rossi", "username" : "user2344", "age" : 79, "email" : "Fabio.Rossi@uol.com.br", "bloodType" : "B-", "id_num" : "747666227124", "registerDate" : ISODate("2018-02-21T09:30:07.405Z"), "ticketNumber" : 3002, "jobs" : [ "Gerontologia", "Estudos de Mídia" ], "favFruits" : [ "Tangerina" ], "movies" : [ { "title" : "Guerra nas Estrelas (1977)", "rating" : 1.3 }, { "title" : "A Lista de Schindler (1993)", "rating" : 0.41 }, { "title" : "Clube da Luta (1999)", "rating" : 4.83 }, { "title" : "À Espera de um Milagre (1999)", "rating" : 4.09 }, { "title" : "Parasita (2019)", "rating" : 4.4 } ], "dog" : { "name" : "Rosa", "age" : 11 } }
{ "_id" : ObjectId("5e644398ee36625be4c9b149"), "firstname" : "Mirko", "surname" : "Rossi", "username" : "user5395", "age" : 79, "email" : "Mirko.Rossi@gmail.com", "bloodType" : "A-", "id_num" : "281561882822", "registerDate" : ISODate("2020-02-22T15:40:27.230Z"), "ticketNumber" : 6364, "jobs" : [ "Construção Naval", "Aquicultura" ], "favFruits" : [ "Mamão", "Maçã", "Kiwi" ], "movies" : [ { "title" : "A Viagem de Chihiro (2001)", "rating" : 4.29 }, { "title" : "Forrest Gump: O Contador de Histórias (1994)", "rating" : 2.06 }, { "title" : "A Viagem de Chihiro (2001)", "rating" : 2.66 }, { "title" : "À Espera de um Milagre (1999)", "rating" : 4.87 }, { "title" : "O Silêncio dos Inocentes (1991)", "rating" : 3.53 } ], "father" : { "firstname" : "Alessio", "surname" : "Rossi", "age" : 107 }, "dog" : { "name" : "Cristian", "age" : 7 } }
{ "_id" : ObjectId("5e644392ee36625be4c9a7e3"), "firstname" : "Davide", "surname" : "Rossi", "username" : "user2989", "age" : 77, "email" : "Davide.Rossi@outlook.com", "bloodType" : "O+", "id_num" : "873135140220", "registerDate" : ISODate("2009-02-20T10:28:31.399Z"), "ticketNumber" : 8195, "jobs" : [ "Alimentos" ], "favFruits" : [ "Maçã", "Banana" ], "movies" : [ { "title" : "Guerra nas Estrelas (1977)", "rating" : 2.64 }, { "title" : "12 Homens e uma Sentença (1957)", "rating" : 1.89 } ], "cat" : { "name" : "Simona", "age" : 6 } }
{ "_id" : ObjectId("5e6443a3ee36625be4c9c1e9"), "firstname" : "Eleonora", "surname" : "Rossi", "username" : "user9651", "age" : 77, "email" : "Eleonora.Rossi@gmail.com", "bloodType" : "O+", "id_num" : "332526488223", "registerDate" : ISODate("2014-08-25T00:05:08.553Z"), "ticketNumber" : 2993, "jobs" : [ "Produção Têxtil", "Gestão de Seguros" ], "favFruits" : [ "Kiwi" ], "movies" : [ { "title" : "Pulp Fiction: Tempo de Violência (1994)", "rating" : 1.79 }, { "title" : "A Felicidade Não se Compra (1946)", "rating" : 3.06 }, { "title" : "Os Bons Companheiros (1990)", "rating" : 3.05 }, { "title" : "Pulp Fiction: Tempo de Violência (1994)", "rating" : 1.42 } ], "father" : { "firstname" : "Alessandro", "surname" : "Rossi", "age" : 106 }, "cat" : { "name" : "Marta", "age" : 10 } }
{ "_id" : ObjectId("5e64439fee36625be4c9bb82"), "firstname" : "Massimiliano", "surname" : "Rossi", "username" : "user8012", "age" : 76, "email" : "Massimiliano.Rossi@uol.com.br", "bloodType" : "A-", "id_num" : "158061238352", "registerDate" : ISODate("2014-05-29T15:12:22.424Z"), "ticketNumber" : 9256, "jobs" : [ "Gestão em Saúde" ], "favFruits" : [ "Pêssego" ], "movies" : [ { "title" : "A Lista de Schindler (1993)", "rating" : 4.05 }, { "title" : "Guerra nas Estrelas (1977)", "rating" : 2.25 } ] }

13. Crie um italiano que tenha um leão como animal de estimação. Associe um nome e idade ao bichano
> db.italians.insert({ "firstname": "Michelangelo", "surname": "Romeo", "age": 50, "id_num": "0123456789", "lion": {"name": "Emiliano", "age": 65}})</br>
WriteResult({ "nInserted" : 1 })

14. Infelizmente o Leão comeu o italiano. Remova essa pessoa usando o Id.
> db.italians.remove({"_id": ObjectId("5e651df4ee36625be4c9c3aa")})</br>
WriteResult({ "nRemoved" : 1 })

15. Passou um ano. Atualize a idade de todos os italianos e dos bichanos em 1
> db.italians.update({}, {"$inc": {"age": 1}}, {multi: true})</br>
WriteResult({ "nMatched" : 10000, "nUpserted" : 0, "nModified" : 10000 })</br>
> db.italians.update({cat: {$exists: true}}, {"$inc": {"cat.age": 1}}, {multi: true})</br>
WriteResult({ "nMatched" : 6032, "nUpserted" : 0, "nModified" : 6032 })</br>
> db.italians.update({dog: {$exists: true}}, {"$inc": {"dog.age": 1}}, {multi: true})</br>
WriteResult({ "nMatched" : 3962, "nUpserted" : 0, "nModified" : 3962 })

16. O Corona Vírus chegou na Itália e misteriosamente atingiu pessoas somente com gatos e de 66 anos. Remova esses italianos.
> db.italians.remove({"age": 66, cat: {$exists: true}})</br>
WriteResult({ "nRemoved" : 72 })

17. Utilizando o framework agregate, liste apenas as pessoas com nomes iguais a sua respectiva mãe e que tenha gato ou cachorro.
> db.italians.aggregate([
{"$match": {
mother: {$exists: true},
$or: [{cat: {$exists: true}}, {dog: {$exists: true}}]
}}, 
{"$project": {
"firstname": 1,
"mother": 1,
"cat":1,
"dog":1,
"isEqual": {"$cmp": ["$firstname", "$mother.firstname"]}
 }},
{"$match": {"isEqual": 0}}])</br>

{ "_id" : ObjectId("5e652e2cee36625be4c9ebda"), "firstname" : "Michela", "mother" : { "firstname" : "Michela", "surname" : "Fiore", "age" : 83 }, "cat" : { "name" : "Cristian", "age" : 4 }, "dog" : { "name" : "Federico", "age" : 16 }, "isEqual" : 0 }
{ "_id" : ObjectId("5e652e2dee36625be4c9ee1d"), "firstname" : "Giacomo", "mother" : { "firstname" : "Giacomo", "surname" : "Lombardi", "age" : 84 }, "cat" : { "name" : "Maurizio", "age" : 12 }, "isEqual" : 0 }
{ "_id" : ObjectId("5e652e30ee36625be4c9f227"), "firstname" : "Marta", "mother" : { "firstname" : "Marta", "surname" : "Battaglia", "age" : 89 }, "dog" : { "name" : "Giusy", "age" : 17 }, "isEqual" : 0 }
{ "_id" : ObjectId("5e652e30ee36625be4c9f3b5"), "firstname" : "Martina", "mother" : { "firstname" : "Martina", "surname" : "Ferrari", "age" : 60 }, "cat" : { "name" : "Luigi", "age" : 11 }, "isEqual" : 0 }
{ "_id" : ObjectId("5e652e37ee36625be4c9fe7d"), "firstname" : "Cinzia", "mother" : { "firstname" : "Cinzia", "surname" : "Basile", "age" : 81 }, "cat" : { "name" : "Fabio", "age" : 3 }, "isEqual" : 0 }


18. Utilizando aggregate framework, faça uma lista de nomes única de nomes. Faça isso usando apenas o primeiro nome
> db.italians.aggregate( [ { $group : { _id : "$firstname" } } ] )</br>
{ "_id" : "Salvatore" }
{ "_id" : "Serena" }
{ "_id" : "Valeira" }
{ "_id" : "Andrea" }
{ "_id" : "Stefania" }
{ "_id" : "Mattia" }
{ "_id" : "Domenico" }
{ "_id" : "Mario" }
{ "_id" : "Simone" }
{ "_id" : "Nicola" }
{ "_id" : "Rita" }
{ "_id" : "Paola" }
{ "_id" : "Filipo" }
{ "_id" : "Enzo " }
{ "_id" : "Emanuela" }
{ "_id" : "Matteo" }
{ "_id" : "Sara" }
{ "_id" : "Mirko" }
{ "_id" : "Giulia" }
{ "_id" : "Barbara" }
Type "it" for more

19. Agora faça a mesma lista do item acima, considerando nome completo.
> db.italians.aggregate( [ { $group : { _id : {"a":"$firstname","b":"$surname"} } } ] )</br>
{ "_id" : { "a" : "Martina", "b" : "Battaglia" } }
{ "_id" : { "a" : "Gabiele", "b" : "Conti" } }
{ "_id" : { "a" : "Alessia", "b" : "Milani" } }
{ "_id" : { "a" : "Gianni", "b" : "De Rosa" } }
{ "_id" : { "a" : "Matteo", "b" : "De Rosa" } }
{ "_id" : { "a" : "Maria", "b" : "Testa" } }
{ "_id" : { "a" : "Ilaria", "b" : "Bellini" } }
{ "_id" : { "a" : "Eleonora", "b" : "Ferri" } }
{ "_id" : { "a" : "Massimo", "b" : "Grassi" } }
{ "_id" : { "a" : "Mauro", "b" : "Monti" } }
{ "_id" : { "a" : "Cristina", "b" : "Mariani" } }
{ "_id" : { "a" : "Paola", "b" : "Fiore" } }
{ "_id" : { "a" : "Mirko", "b" : "Milani" } }
{ "_id" : { "a" : "Domenico", "b" : "Marini" } }
{ "_id" : { "a" : "Massimo", "b" : "Marini" } }
{ "_id" : { "a" : "Giulia", "b" : "Amato" } }
{ "_id" : { "a" : "Enzo ", "b" : "D’Amico" } }
{ "_id" : { "a" : "Claudia", "b" : "Grasso" } }
{ "_id" : { "a" : "Filipo", "b" : "Ferri" } }
{ "_id" : { "a" : "Marco", "b" : "Rizzo" } }
Type "it" for more

20. Procure pessoas que gosta de Banana ou Maçã, tenham cachorro ou gato, mais de 20 e menos de 60 anos.
> db.italians.find({$where: '(this.favFruits == "Banana" || this.favFruits == "Maça") && (this.cat || this.dog) && (this.age > 20 && this.age < 60)'},{"favFruits":1, "age":1, "dog":1, "cat":1,_id:0})</br>
{ "age" : 25, "favFruits" : [ "Banana" ], "cat" : { "name" : "Tiziana", "age" : 11 } }
{ "age" : 26, "favFruits" : [ "Banana" ], "cat" : { "name" : "Salvatore", "age" : 3 } }
{ "age" : 57, "favFruits" : [ "Banana" ], "cat" : { "name" : "Angela", "age" : 1 } }
{ "age" : 54, "favFruits" : [ "Banana" ], "cat" : { "name" : "Luigi", "age" : 18 } }
{ "age" : 23, "favFruits" : [ "Banana" ], "cat" : { "name" : "Giulia", "age" : 12 } }
{ "age" : 57, "favFruits" : [ "Banana" ], "cat" : { "name" : "Laura", "age" : 7 }, "dog" : { "name" : "Rita", "age" : 4 } }
{ "age" : 32, "favFruits" : [ "Banana" ], "cat" : { "name" : "Lucia", "age" : 3 } }
{ "age" : 40, "favFruits" : [ "Banana" ], "cat" : { "name" : "Alessandro", "age" : 10 } }
{ "age" : 45, "favFruits" : [ "Banana" ], "dog" : { "name" : "Federica", "age" : 8 } }
{ "age" : 40, "favFruits" : [ "Banana" ], "dog" : { "name" : "Ilaria", "age" : 14 } }
{ "age" : 25, "favFruits" : [ "Banana" ], "cat" : { "name" : "Marco", "age" : 8 } }
{ "age" : 55, "favFruits" : [ "Banana" ], "cat" : { "name" : "Luigi", "age" : 2 }, "dog" : { "name" : "Mario", "age" : 3 } }
{ "age" : 26, "favFruits" : [ "Banana" ], "cat" : { "name" : "Silvia", "age" : 12 } }
{ "age" : 25, "favFruits" : [ "Banana" ], "cat" : { "name" : "Luca", "age" : 9 } }
{ "age" : 55, "favFruits" : [ "Banana" ], "cat" : { "name" : "Alessio", "age" : 11 } }
{ "age" : 22, "favFruits" : [ "Banana" ], "cat" : { "name" : "Teresa", "age" : 7 } }
{ "age" : 55, "favFruits" : [ "Banana" ], "dog" : { "name" : "Gabiele", "age" : 7 } }
{ "age" : 24, "favFruits" : [ "Banana" ], "cat" : { "name" : "Carlo", "age" : 9 } }
{ "age" : 48, "favFruits" : [ "Banana" ], "cat" : { "name" : "Federica", "age" : 1 } }
{ "age" : 50, "favFruits" : [ "Banana" ], "cat" : { "name" : "Massimo", "age" : 2 } }
Type "it" for more

# Exercício 3 - Stockbrokers

1. Liste as ações com profit acima de 0.5 (limite a 10 o resultado)

> db.stocks.find({"Profit Margin": {"$gt": 0.5}},{"Profit Margin":1,_id:0}).sort({"Profit Margin": 1}).limit(10)</br>
{ "Profit Margin" : 0.503 }
{ "Profit Margin" : 0.506 }
{ "Profit Margin" : 0.506 }
{ "Profit Margin" : 0.507 }
{ "Profit Margin" : 0.507 }
{ "Profit Margin" : 0.513 }
{ "Profit Margin" : 0.518 }
{ "Profit Margin" : 0.519 }
{ "Profit Margin" : 0.522 }
{ "Profit Margin" : 0.525 }

2. Liste as ações com perdas (limite a 10 novamente)

> db.stocks.find({"Profit Margin": {"$lt": 0}},{"Profit Margin":1,_id:0}).sort({"Profit Margin": 1}).limit(10)</br>
{ "Profit Margin" : -266.0417 }
{ "Profit Margin" : -27.9802 }
{ "Profit Margin" : -21.5587 }
{ "Profit Margin" : -11.7596 }
{ "Profit Margin" : -11.079 }
{ "Profit Margin" : -6.176 }
{ "Profit Margin" : -4.7349 }
{ "Profit Margin" : -3.3162 }
{ "Profit Margin" : -3.0824 }
{ "Profit Margin" : -3.0335 }

3. Liste as 10 ações mais rentáveis

> db.stocks.find({},{"Profit Margin":1,"Company":1,_id:0}).sort({"Profit Margin": -1}).limit(10)</br>
{ "Profit Margin" : 0.994, "Company" : "BP Prudhoe Bay Royalty Trust" }
{ "Profit Margin" : 0.994, "Company" : "Cascade Bancorp" }
{ "Profit Margin" : 0.99, "Company" : "Pacific Coast Oil Trust" }
{ "Profit Margin" : 0.986, "Company" : "Enduro Royalty Trust" }
{ "Profit Margin" : 0.982, "Company" : "Whiting USA Trust II" }
{ "Profit Margin" : 0.976, "Company" : "MV Oil Trust" }
{ "Profit Margin" : 0.972, "Company" : "American Capital Agency Corp." }
{ "Profit Margin" : 0.971, "Company" : "VOC Energy Trust" }
{ "Profit Margin" : 0.97, "Company" : "Mesa Royalty Trust" }
{ "Profit Margin" : 0.97, "Company" : "One Liberty Properties Inc." }

4. Qual foi o setor mais rentável?
> db.stocks.aggregate([{$group:{_id:"$Sector", Profits:{$sum:"$Profit Margin"}}},{$sort:{"Profits": -1}}])</br>
{ "_id" : "Financial", "Profits" : 162.5356 }
{ "_id" : "Services", "Profits" : 20.5515 }
{ "_id" : "Consumer Goods", "Profits" : 13.23 }
{ "_id" : "Industrial Goods", "Profits" : 11.0327 }
{ "_id" : "Utilities", "Profits" : 7.423 }
{ "_id" : "Conglomerates", "Profits" : 0.3835 }
{ "_id" : "Basic Materials", "Profits" : -9.190900000000001 }
{ "_id" : "Technology", "Profits" : -18.8968 }
{ "_id" : "Healthcare", "Profits" : -316.68649999999997 }

5. Ordene as ações pelo profit e usando um cursor, liste as ações.

> var cursor = db.stocks.find({"Profit Margin":{$exists: true}}, {"Company":1,"Profit Margin":1,"_id": 0})</br>
> cursor.sort({"Profit Margin":-1})
{ "Profit Margin" : 0.994, "Company" : "BP Prudhoe Bay Royalty Trust" }
{ "Profit Margin" : 0.994, "Company" : "Cascade Bancorp" }
{ "Profit Margin" : 0.99, "Company" : "Pacific Coast Oil Trust" }
{ "Profit Margin" : 0.986, "Company" : "Enduro Royalty Trust" }
{ "Profit Margin" : 0.982, "Company" : "Whiting USA Trust II" }
{ "Profit Margin" : 0.976, "Company" : "MV Oil Trust" }
{ "Profit Margin" : 0.972, "Company" : "American Capital Agency Corp." }
{ "Profit Margin" : 0.971, "Company" : "VOC Energy Trust" }
{ "Profit Margin" : 0.97, "Company" : "Mesa Royalty Trust" }
{ "Profit Margin" : 0.97, "Company" : "One Liberty Properties Inc." }
{ "Profit Margin" : 0.97, "Company" : "Permian Basin Royalty Trust" }
{ "Profit Margin" : 0.969, "Company" : "Cross Timbers Royalty Trust" }
{ "Profit Margin" : 0.967, "Company" : "Harvest Capital Credit Corporation" }
{ "Profit Margin" : 0.966, "Company" : "Whiting USA Trust I" }
{ "Profit Margin" : 0.963, "Company" : "Mesabi Trust" }
{ "Profit Margin" : 0.959, "Company" : "Sabine Royalty Trust" }
{ "Profit Margin" : 0.958, "Company" : "North European Oil Royalty Trust" }
{ "Profit Margin" : 0.933, "Company" : "Sandridge Mississippian Trust II" }
{ "Profit Margin" : 0.93, "Company" : "Hugoton Royalty Trust" }
{ "Profit Margin" : 0.928, "Company" : "SandRidge Mississippian Trust I" }
Type "it" for more

6. Renomeie o campo “Profit Margin” para apenas “profit”.
> db.stocks.update({"Profit Margin":{$exists:true}},{$rename:{"Profit Margin":"Profit"}},{multi: true})</br>
WriteResult({ "nMatched" : 4302, "nUpserted" : 0, "nModified" : 4302 })

7. Agora liste apenas a empresa e seu respectivo resultado
> db.stocks.find({"Profit":{$exists: true}},{"Company":1,"Profit":1,"_id": 0}).sort({"Profit": -1})</br>
{ "Company" : "BP Prudhoe Bay Royalty Trust", "Profit" : 0.994 }
{ "Company" : "Cascade Bancorp", "Profit" : 0.994 }
{ "Company" : "Pacific Coast Oil Trust", "Profit" : 0.99 }
{ "Company" : "Enduro Royalty Trust", "Profit" : 0.986 }
{ "Company" : "Whiting USA Trust II", "Profit" : 0.982 }
{ "Company" : "MV Oil Trust", "Profit" : 0.976 }
{ "Company" : "American Capital Agency Corp.", "Profit" : 0.972 }
{ "Company" : "VOC Energy Trust", "Profit" : 0.971 }
{ "Company" : "Mesa Royalty Trust", "Profit" : 0.97 }
{ "Company" : "One Liberty Properties Inc.", "Profit" : 0.97 }
{ "Company" : "Permian Basin Royalty Trust", "Profit" : 0.97 }
{ "Company" : "Cross Timbers Royalty Trust", "Profit" : 0.969 }
{ "Company" : "Harvest Capital Credit Corporation", "Profit" : 0.967 }
{ "Company" : "Whiting USA Trust I", "Profit" : 0.966 }
{ "Company" : "Mesabi Trust", "Profit" : 0.963 }
{ "Company" : "Sabine Royalty Trust", "Profit" : 0.959 }
{ "Company" : "North European Oil Royalty Trust", "Profit" : 0.958 }
{ "Company" : "Sandridge Mississippian Trust II", "Profit" : 0.933 }
{ "Company" : "Hugoton Royalty Trust", "Profit" : 0.93 }
{ "Company" : "SandRidge Mississippian Trust I", "Profit" : 0.928 }
Type "it" for more

8. Analise as ações. É uma bola de cristal na sua mão... Quais as três ações você investiria?
> var lucrativas = db.stocks.find({"Profit":{$exists: true}}, {"Company":1,"Sector":1,"Profit":1,"_id":0 })</br>
> lucrativas.sort({"Profit":-1}).limit(3)</br>
{ "Sector" : "Basic Materials", "Company" : "BP Prudhoe Bay Royalty Trust", "Profit" : 0.994 }
{ "Sector" : "Financial", "Company" : "Cascade Bancorp", "Profit" : 0.994 }
{ "Sector" : "Basic Materials", "Company" : "Pacific Coast Oil Trust", "Profit" : 0.99 }

9. Liste as ações agrupadas por setor
> db.stocks.aggregate([{"$group": {_id:"$Sector"}}])</br>
{ "_id" : "Healthcare" }
{ "_id" : "Services" }
{ "_id" : "Basic Materials" }
{ "_id" : "Utilities" }
{ "_id" : "Technology" }
{ "_id" : "Consumer Goods" }
{ "_id" : "Financial" }
{ "_id" : "Industrial Goods" }
{ "_id" : "Conglomerates" }

> db.stocks.aggregate([{"$group": {_id:"$Sector", companies: {"$addToSet": {Company:"$Company"}}}},{"$project": {"_id":1,"companies":1}}])</br>
Irá apresentar o nome das companias agrupados pelo setor.

Exercício 3 – Fraude na Enron!

1. Liste as pessoas que enviaram e-mails (de forma distinta, ou seja, sem repetir). Quantas pessoas são?

> db.enron.distinct('sender').length</br>
2200

2. Contabilize quantos e-mails tem a palavra “fraud”

> db.enron.find({"text": /fraud/}).count()</br>
23

     



