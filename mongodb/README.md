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

> db.italians.find({"cat": null}).count()</br>
4045</br>
> db.italians.find({"dog": null}).count()</br>
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
> db.italians.find({$where: function() { return this.cat && this.dog}})</br>

{ "_id" : ObjectId("5e64438aee36625be4c99c9c"), "firstname" : "Filipo", "surname" : "Villa", "username" : "user102", "age" : 68, "email" : "Filipo.Villa@live.com", "bloodType" : "B-", "id_num" : "375860277854", "registerDate" : ISODate("2013-01-21T00:00:03.485Z"), "ticketNumber" : 1531, "jobs" : [ "Estatística" ], "favFruits" : [ "Banana" ], "movies" : [ { "title" : "Batman: O Cavaleiro das Trevas (2008)", "rating" : 0.12 }, { "title" : "A Origem (2010)", "rating" : 2.76 }, { "title" : "O Senhor dos Anéis: O Retorno do Rei (2003)", "rating" : 0.27 } ], "cat" : { "name" : "Vincenzo", "age" : 14 }, "dog" : { "name" : "Elena", "age" : 4 } }
{ "_id" : ObjectId("5e64438aee36625be4c99ca1"), "firstname" : "Roberta", "surname" : "Martino", "username" : "user107", "age" : 17, "email" : "Roberta.Martino@uol.com.br", "bloodType" : "AB+", "id_num" : "053066064525", "registerDate" : ISODate("2007-05-30T05:49:38.301Z"), "ticketNumber" : 6574, "jobs" : [ "Musicoterapia", "Engenharia Eletrônica" ], "favFruits" : [ "Banana", "Pêssego" ], "movies" : [ { "title" : "A Origem (2010)", "rating" : 0.58 }, { "title" : "Um Estranho no Ninho (1975)", "rating" : 3.62 }, { "title" : "O Silêncio dos Inocentes (1991)", "rating" : 0.13 }, { "title" : "A Vida é Bela (1997)", "rating" : 1.97 } ], "cat" : { "name" : "Tiziana", "age" : 0 }, "dog" : { "name" : "Gianluca", "age" : 1 } }
{ "_id" : ObjectId("5e64438aee36625be4c99ca2"), "firstname" : "Simone", "surname" : "Milani", "username" : "user108", "age" : 5, "email" : "Simone.Milani@live.com", "bloodType" : "AB+", "id_num" : "321473786521", "registerDate" : ISODate("2009-01-26T09:20:33.109Z"), "ticketNumber" : 1194, "jobs" : [ "Pilotagem profissional de aeronaves" ], "favFruits" : [ "Laranja", "Goiaba", "Laranja" ], "movies" : [ { "title" : "A Origem (2010)", "rating" : 1.3 }, { "title" : "Star Wars, Episódio V: O Império Contra-Ataca (1980)", "rating" : 0.62 }, { "title" : "O Senhor dos Anéis: O Retorno do Rei (2003)", "rating" : 2.81 } ], "cat" : { "name" : "Mauro", "age" : 1 }, "dog" : { "name" : "Michele", "age" : 8 } }
{ "_id" : ObjectId("5e64438aee36625be4c99ca5"), "firstname" : "Sergio", "surname" : "Lombardi", "username" : "user111", "age" : 42, "email" : "Sergio.Lombardi@live.com", "bloodType" : "O+", "id_num" : "018122438182", "registerDate" : ISODate("2013-12-15T17:08:40.642Z"), "ticketNumber" : 5343, "jobs" : [ "Terapia Ocupacional" ], "favFruits" : [ "Tangerina" ], "movies" : [ { "title" : "Batman: O Cavaleiro das Trevas (2008)", "rating" : 4.42 }, { "title" : "1917 (2019)", "rating" : 0.01 }, { "title" : "Três Homens em Conflito (1966)", "rating" : 1.29 }, { "title" : "Forrest Gump: O Contador de Histórias (1994)", "rating" : 3.05 }, { "title" : "Parasita (2019)", "rating" : 1.12 } ], "cat" : { "name" : "Matteo", "age" : 5 }, "dog" : { "name" : "Anna", "age" : 16 } }
{ "_id" : ObjectId("5e64438aee36625be4c99ca8"), "firstname" : "Roberta", "surname" : "Sanna", "username" : "user114", "age" : 60, "email" : "Roberta.Sanna@uol.com.br", "bloodType" : "AB-", "id_num" : "811452225213", "registerDate" : ISODate("2017-08-11T20:34:10.770Z"), "ticketNumber" : 6272, "jobs" : [ "Jogos Digitais" ], "favFruits" : [ "Tangerina", "Kiwi", "Tangerina" ], "movies" : [ { "title" : "A Origem (2010)", "rating" : 2.47 }, { "title" : "Guerra nas Estrelas (1977)", "rating" : 1.71 }, { "title" : "O Poderoso Chefão (1972)", "rating" : 1.01 }, { "title" : "1917 (2019)", "rating" : 4.57 }, { "title" : "Guerra nas Estrelas (1977)", "rating" : 1.08 } ], "cat" : { "name" : "Paola", "age" : 17 }, "dog" : { "name" : "Mauro", "age" : 4 } }
{ "_id" : ObjectId("5e64438aee36625be4c99caa"), "firstname" : "Paolo", "surname" : "Ferretti", "username" : "user116", "age" : 2, "email" : "Paolo.Ferretti@live.com", "bloodType" : "B+", "id_num" : "317287044634", "registerDate" : ISODate("2014-03-18T07:04:50.086Z"), "ticketNumber" : 9763, "jobs" : [ "Manutenção de aeronaves", "Esporte" ], "favFruits" : [ "Mamão" ], "movies" : [ { "title" : "Intocáveis (2011)", "rating" : 0.78 }, { "title" : "Interestelar (2014)", "rating" : 1.49 }, { "title" : "Star Wars, Episódio V: O Império Contra-Ataca (1980)", "rating" : 3.22 }, { "title" : "Três Homens em Conflito (1966)", "rating" : 2.81 } ], "cat" : { "name" : "Cinzia", "age" : 3 }, "dog" : { "name" : "Sabrina", "age" : 9 } }
{ "_id" : ObjectId("5e64438aee36625be4c99cae"), "firstname" : "Massimiliano", "surname" : "Fabbri", "username" : "user120", "age" : 45, "email" : "Massimiliano.Fabbri@hotmail.com", "bloodType" : "A+", "id_num" : "638770286480", "registerDate" : ISODate("2019-03-11T14:52:47.509Z"), "ticketNumber" : 8171, "jobs" : [ "Secretariado" ], "favFruits" : [ "Melancia", "Pêssego" ], "movies" : [ { "title" : "12 Homens e uma Sentença (1957)", "rating" : 3.29 }, { "title" : "O Senhor dos Anéis: As Duas Torres (2002)", "rating" : 3.52 }, { "title" : "O Senhor dos Anéis: O Retorno do Rei (2003)", "rating" : 3.15 } ], "cat" : { "name" : "Mario", "age" : 15 }, "dog" : { "name" : "Vincenzo", "age" : 15 } }
{ "_id" : ObjectId("5e64438aee36625be4c99caf"), "firstname" : "Antonella", "surname" : "Morelli", "username" : "user121", "age" : 35, "email" : "Antonella.Morelli@live.com", "bloodType" : "A-", "id_num" : "222568343160", "registerDate" : ISODate("2019-04-11T14:58:06.275Z"), "ticketNumber" : 8012, "jobs" : [ "Engenharia de Controle e Automação" ], "favFruits" : [ "Pêssego", "Maçã", "Goiaba" ], "movies" : [ { "title" : "Matrix (1999)", "rating" : 3.39 }, { "title" : "Batman: O Cavaleiro das Trevas (2008)", "rating" : 0.66 } ], "cat" : { "name" : "Giulia", "age" : 6 }, "dog" : { "name" : "Emanuele", "age" : 16 } }
{ "_id" : ObjectId("5e64438aee36625be4c99cb2"), "firstname" : "Enzo ", "surname" : "Rossetti", "username" : "user124", "age" : 3, "email" : "Enzo .Rossetti@yahoo.com", "bloodType" : "A+", "id_num" : "868011018458", "registerDate" : ISODate("2009-11-03T05:01:39.833Z"), "ticketNumber" : 249, "jobs" : [ "Petróleo e Gás" ], "favFruits" : [ "Pêssego", "Maçã", "Uva" ], "movies" : [ { "title" : "1917 (2019)", "rating" : 1.42 }, { "title" : "Cidade de Deus (2002)", "rating" : 2.38 }, { "title" : "O Senhor dos Anéis: O Retorno do Rei (2003)", "rating" : 2.68 }, { "title" : "1917 (2019)", "rating" : 3.02 } ], "mother" : { "firstname" : "Teresa", "surname" : "Rossetti", "age" : 30 }, "father" : { "firstname" : "Roberto", "surname" : "Rossetti", "age" : 34 }, "cat" : { "name" : "Giovanna", "age" : 7 }, "dog" : { "name" : "Giacomo", "age" : 12 } }
{ "_id" : ObjectId("5e64438aee36625be4c99cb5"), "firstname" : "Michele", "surname" : "Gatti", "username" : "user127", "age" : 19, "email" : "Michele.Gatti@gmail.com", "bloodType" : "A+", "id_num" : "370847035548", "registerDate" : ISODate("2010-06-24T13:27:58.658Z"), "ticketNumber" : 1194, "jobs" : [ "Esporte" ], "favFruits" : [ "Uva", "Maçã" ], "movies" : [ { "title" : "Interestelar (2014)", "rating" : 4.81 }, { "title" : "1917 (2019)", "rating" : 2.22 } ], "cat" : { "name" : "Rita", "age" : 1 }, "dog" : { "name" : "Marta", "age" : 12 } }
{ "_id" : ObjectId("5e64438aee36625be4c99cb8"), "firstname" : "Fabio", "surname" : "Marino", "username" : "user130", "age" : 43, "email" : "Fabio.Marino@gmail.com", "bloodType" : "A-", "id_num" : "845775846118", "registerDate" : ISODate("2007-03-13T01:44:17.481Z"), "ticketNumber" : 9108, "jobs" : [ "Produção Cultural" ], "favFruits" : [ "Tangerina", "Pêssego" ], "movies" : [ { "title" : "O Senhor dos Anéis: O Retorno do Rei (2003)", "rating" : 0 }, { "title" : "Interestelar (2014)", "rating" : 3.12 }, { "title" : "Um Sonho de Liberdade (1994)", "rating" : 1.71 } ], "cat" : { "name" : "Silvia", "age" : 15 }, "dog" : { "name" : "Raffaele", "age" : 15 } }
{ "_id" : ObjectId("5e64438aee36625be4c99cc5"), "firstname" : "Giuseppe", "surname" : "Rossi", "username" : "user143", "age" : 62, "email" : "Giuseppe.Rossi@hotmail.com", "bloodType" : "O-", "id_num" : "543254636678", "registerDate" : ISODate("2017-01-12T17:30:58.057Z"), "ticketNumber" : 9597, "jobs" : [ "Estética e Cosmética", "Eletrônica Industrial" ], "favFruits" : [ "Tangerina", "Kiwi" ], "movies" : [ { "title" : "Pulp Fiction: Tempo de Violência (1994)", "rating" : 1.03 }, { "title" : "Pulp Fiction: Tempo de Violência (1994)", "rating" : 4.74 } ], "cat" : { "name" : "Giovanni", "age" : 4 }, "dog" : { "name" : "Marta", "age" : 3 } }
{ "_id" : ObjectId("5e64438aee36625be4c99cc7"), "firstname" : "Giuseppe", "surname" : "De Rosa", "username" : "user145", "age" : 16, "email" : "Giuseppe.De Rosa@uol.com.br", "bloodType" : "O-", "id_num" : "243034008505", "registerDate" : ISODate("2013-09-26T19:08:06.144Z"), "ticketNumber" : 8344, "jobs" : [ "Produção Sucroalcooleira" ], "favFruits" : [ "Melancia" ], "movies" : [ { "title" : "1917 (2019)", "rating" : 0.26 } ], "mother" : { "firstname" : "Daniele", "surname" : "De Rosa", "age" : 33 }, "cat" : { "name" : "Federico", "age" : 4 }, "dog" : { "name" : "Stefano", "age" : 3 } }
{ "_id" : ObjectId("5e64438aee36625be4c99cca"), "firstname" : "Nicola", "surname" : "Caputo", "username" : "user148", "age" : 58, "email" : "Nicola.Caputo@outlook.com", "bloodType" : "B-", "id_num" : "825074656728", "registerDate" : ISODate("2008-07-20T02:24:18.663Z"), "ticketNumber" : 451, "jobs" : [ "Comunicação Organizacional", "Astronomia" ], "favFruits" : [ "Laranja" ], "movies" : [ { "title" : "Cidade de Deus (2002)", "rating" : 2.1 }, { "title" : "Vingadores: Ultimato (2019)", "rating" : 4.02 }, { "title" : "Um Estranho no Ninho (1975)", "rating" : 3.66 }, { "title" : "1917 (2019)", "rating" : 1.33 }, { "title" : "A Vida é Bela (1997)", "rating" : 1.34 } ], "cat" : { "name" : "Laura", "age" : 5 }, "dog" : { "name" : "Daniela", "age" : 12 } }
{ "_id" : ObjectId("5e64438aee36625be4c99cce"), "firstname" : "Alex", "surname" : "Sanna", "username" : "user152", "age" : 30, "email" : "Alex.Sanna@outlook.com", "bloodType" : "AB+", "id_num" : "501367683578", "registerDate" : ISODate("2008-03-05T23:47:20.370Z"), "ticketNumber" : 2194, "jobs" : [ "Secretariado" ], "favFruits" : [ "Laranja" ], "movies" : [ { "title" : "Um Sonho de Liberdade (1994)", "rating" : 3.37 }, { "title" : "O Poderoso Chefão II (1974)", "rating" : 0.17 }, { "title" : "Gladiador (2000)", "rating" : 2.59 } ], "father" : { "firstname" : "Marco", "surname" : "Sanna", "age" : 52 }, "cat" : { "name" : "Antonella", "age" : 11 }, "dog" : { "name" : "Giorgia", "age" : 3 } }
{ "_id" : ObjectId("5e64438aee36625be4c99cd4"), "firstname" : "Pietro", "surname" : "Montanari", "username" : "user158", "age" : 63, "email" : "Pietro.Montanari@gmail.com", "bloodType" : "AB-", "id_num" : "681153520701", "registerDate" : ISODate("2011-08-25T05:45:32.149Z"), "ticketNumber" : 777, "jobs" : [ "Saúde e Bem-estar" ], "favFruits" : [ "Laranja" ], "movies" : [ { "title" : "O Poderoso Chefão (1972)", "rating" : 2.91 } ], "cat" : { "name" : "Simone", "age" : 13 }, "dog" : { "name" : "Veronica", "age" : 10 } }
{ "_id" : ObjectId("5e64438aee36625be4c99cdb"), "firstname" : "Laura", "surname" : "Conte", "username" : "user165", "age" : 57, "email" : "Laura.Conte@gmail.com", "bloodType" : "O+", "id_num" : "188178221521", "registerDate" : ISODate("2019-02-09T05:04:12.292Z"), "ticketNumber" : 7821, "jobs" : [ "Engenharia de Sistemas", "Construção Naval" ], "favFruits" : [ "Uva", "Kiwi", "Uva" ], "movies" : [ { "title" : "Seven: Os Sete Crimes Capitais (1995)", "rating" : 2.93 }, { "title" : "À Espera de um Milagre (1999)", "rating" : 4.71 } ], "mother" : { "firstname" : "Antonella", "surname" : "Conte", "age" : 73 }, "cat" : { "name" : "Marco", "age" : 7 }, "dog" : { "name" : "Matteo", "age" : 17 } }
{ "_id" : ObjectId("5e64438aee36625be4c99ce3"), "firstname" : "Anna", "surname" : "Gallo", "username" : "user173", "age" : 70, "email" : "Anna.Gallo@outlook.com", "bloodType" : "A-", "id_num" : "276715322271", "registerDate" : ISODate("2016-01-14T17:02:37.920Z"), "ticketNumber" : 6501, "jobs" : [ "Ciência e Tecnologia de Alimentos", "Engenharia de Petróleo" ], "favFruits" : [ "Pêssego" ], "movies" : [ { "title" : "Batman: O Cavaleiro das Trevas (2008)", "rating" : 2.9 }, { "title" : "12 Homens e uma Sentença (1957)", "rating" : 0.89 } ], "cat" : { "name" : "Roberta", "age" : 10 }, "dog" : { "name" : "Carlo", "age" : 16 } }
{ "_id" : ObjectId("5e64438aee36625be4c99ce6"), "firstname" : "Emanuela", "surname" : "Romano", "username" : "user176", "age" : 49, "email" : "Emanuela.Romano@hotmail.com", "bloodType" : "AB-", "id_num" : "268266363256", "registerDate" : ISODate("2014-06-16T19:38:15.799Z"), "ticketNumber" : 3291, "jobs" : [ "Sistemas de Telecomunicações" ], "favFruits" : [ "Uva" ], "movies" : [ { "title" : "12 Homens e uma Sentença (1957)", "rating" : 2.07 }, { "title" : "O Senhor dos Anéis: A Sociedade do Anel (2001)", "rating" : 0.93 } ], "father" : { "firstname" : "Sara", "surname" : "Romano", "age" : 70 }, "cat" : { "name" : "Raffaele", "age" : 4 }, "dog" : { "name" : "Enzo ", "age" : 12 } }
{ "_id" : ObjectId("5e64438aee36625be4c99cec"), "firstname" : "Marta", "surname" : "Caruso", "username" : "user182", "age" : 59, "email" : "Marta.Caruso@outlook.com", "bloodType" : "B+", "id_num" : "188886717612", "registerDate" : ISODate("2010-05-15T03:36:57.669Z"), "ticketNumber" : 6990, "jobs" : [ "Gestão de Seguros", "Eletrotécnica Industrial" ], "favFruits" : [ "Tangerina", "Mamão", "Mamão" ], "movies" : [ { "title" : "12 Homens e uma Sentença (1957)", "rating" : 4.85 }, { "title" : "Clube da Luta (1999)", "rating" : 2.6 }, { "title" : "Interestelar (2014)", "rating" : 0.46 }, { "title" : "Cidade de Deus (2002)", "rating" : 2.07 }, { "title" : "Star Wars, Episódio V: O Império Contra-Ataca (1980)", "rating" : 2.31 } ], "cat" : { "name" : "Alex", "age" : 0 }, "dog" : { "name" : "Sabrina", "age" : 11 } }
Type "it" for more

8. Liste todas as pessoas mais novas que seus respectivos gatos.
> db.italians.find({ "$expr": { "$lt": [ "$age" , "$cat.age" ] } })</br>

{ "_id" : ObjectId("5e64438aee36625be4c99c9a"), "firstname" : "Eleonora", "surname" : "Giuliani", "username" : "user100", "age" : 6, "email" : "Eleonora.Giuliani@yahoo.com", "bloodType" : "AB-", "id_num" : "478422641332", "registerDate" : ISODate("2020-02-03T23:28:43.330Z"), "ticketNumber" : 2108, "jobs" : [ "Engenharia Industrial Madeireira", "Artes e Design" ], "favFruits" : [ "Melancia" ], "movies" : [ { "title" : "Três Homens em Conflito (1966)", "rating" : 2.36 }, { "title" : "À Espera de um Milagre (1999)", "rating" : 0.99 }, { "title" : "12 Homens e uma Sentença (1957)", "rating" : 4.02 } ], "father" : { "firstname" : "Elisa", "surname" : "Giuliani", "age" : 36 }, "cat" : { "name" : "Valeira", "age" : 17 } }
{ "_id" : ObjectId("5e64438aee36625be4c99caa"), "firstname" : "Paolo", "surname" : "Ferretti", "username" : "user116", "age" : 2, "email" : "Paolo.Ferretti@live.com", "bloodType" : "B+", "id_num" : "317287044634", "registerDate" : ISODate("2014-03-18T07:04:50.086Z"), "ticketNumber" : 9763, "jobs" : [ "Manutenção de aeronaves", "Esporte" ], "favFruits" : [ "Mamão" ], "movies" : [ { "title" : "Intocáveis (2011)", "rating" : 0.78 }, { "title" : "Interestelar (2014)", "rating" : 1.49 }, { "title" : "Star Wars, Episódio V: O Império Contra-Ataca (1980)", "rating" : 3.22 }, { "title" : "Três Homens em Conflito (1966)", "rating" : 2.81 } ], "cat" : { "name" : "Cinzia", "age" : 3 }, "dog" : { "name" : "Sabrina", "age" : 9 } }
{ "_id" : ObjectId("5e64438aee36625be4c99cb2"), "firstname" : "Enzo ", "surname" : "Rossetti", "username" : "user124", "age" : 3, "email" : "Enzo .Rossetti@yahoo.com", "bloodType" : "A+", "id_num" : "868011018458", "registerDate" : ISODate("2009-11-03T05:01:39.833Z"), "ticketNumber" : 249, "jobs" : [ "Petróleo e Gás" ], "favFruits" : [ "Pêssego", "Maçã", "Uva" ], "movies" : [ { "title" : "1917 (2019)", "rating" : 1.42 }, { "title" : "Cidade de Deus (2002)", "rating" : 2.38 }, { "title" : "O Senhor dos Anéis: O Retorno do Rei (2003)", "rating" : 2.68 }, { "title" : "1917 (2019)", "rating" : 3.02 } ], "mother" : { "firstname" : "Teresa", "surname" : "Rossetti", "age" : 30 }, "father" : { "firstname" : "Roberto", "surname" : "Rossetti", "age" : 34 }, "cat" : { "name" : "Giovanna", "age" : 7 }, "dog" : { "name" : "Giacomo", "age" : 12 } }
{ "_id" : ObjectId("5e64438aee36625be4c99cc4"), "firstname" : "Mirko", "surname" : "De Luca", "username" : "user142", "age" : 3, "email" : "Mirko.De Luca@hotmail.com", "bloodType" : "B+", "id_num" : "503668015368", "registerDate" : ISODate("2018-05-04T07:43:31.241Z"), "ticketNumber" : 6366, "jobs" : [ "Agroecologia", "Engenharia Florestal" ], "favFruits" : [ "Uva", "Tangerina" ], "movies" : [ { "title" : "Star Wars, Episódio V: O Império Contra-Ataca (1980)", "rating" : 1.84 }, { "title" : "A Vida é Bela (1997)", "rating" : 0.81 }, { "title" : "Os Sete Samurais (1954)", "rating" : 0.78 } ], "cat" : { "name" : "Filipo", "age" : 14 } }
{ "_id" : ObjectId("5e64438aee36625be4c99ccc"), "firstname" : "Rosa", "surname" : "D’Angelo", "username" : "user150", "age" : 7, "email" : "Rosa.D’Angelo@gmail.com", "bloodType" : "A-", "id_num" : "708642835842", "registerDate" : ISODate("2012-07-05T05:06:41.750Z"), "ticketNumber" : 6884, "jobs" : [ "Ciências Naturais e Exatas" ], "favFruits" : [ "Banana", "Melancia", "Maçã" ], "movies" : [ { "title" : "Clube da Luta (1999)", "rating" : 2.67 }, { "title" : "Star Wars, Episódio V: O Império Contra-Ataca (1980)", "rating" : 3.51 }, { "title" : "A Origem (2010)", "rating" : 1.95 } ], "mother" : { "firstname" : "Patrizia", "surname" : "D’Angelo", "age" : 26 }, "father" : { "firstname" : "Silvia", "surname" : "D’Angelo", "age" : 35 }, "cat" : { "name" : "Luca", "age" : 10 } }
{ "_id" : ObjectId("5e64438aee36625be4c99cd6"), "firstname" : "Pietro", "surname" : "Messina", "username" : "user160", "age" : 7, "email" : "Pietro.Messina@live.com", "bloodType" : "A+", "id_num" : "222873638456", "registerDate" : ISODate("2011-12-17T15:59:37.378Z"), "ticketNumber" : 934, "jobs" : [ "Produção de Bebidas", "Gestão Comercial" ], "favFruits" : [ "Maçã", "Goiaba" ], "movies" : [ { "title" : "Três Homens em Conflito (1966)", "rating" : 1.65 }, { "title" : "A Felicidade Não se Compra (1946)", "rating" : 2.57 }, { "title" : "Batman: O Cavaleiro das Trevas (2008)", "rating" : 0.75 } ], "cat" : { "name" : "Mario", "age" : 13 } }
{ "_id" : ObjectId("5e64438aee36625be4c99cd8"), "firstname" : "Mirko", "surname" : "Sala", "username" : "user162", "age" : 2, "email" : "Mirko.Sala@hotmail.com", "bloodType" : "B-", "id_num" : "472330052174", "registerDate" : ISODate("2019-09-10T17:18:20.083Z"), "ticketNumber" : 7900, "jobs" : [ "Ciências Naturais e Exatas" ], "favFruits" : [ "Laranja", "Tangerina" ], "movies" : [ { "title" : "12 Homens e uma Sentença (1957)", "rating" : 0.45 }, { "title" : "Star Wars, Episódio V: O Império Contra-Ataca (1980)", "rating" : 0.61 }, { "title" : "Batman: O Cavaleiro das Trevas (2008)", "rating" : 3.38 }, { "title" : "A Vida é Bela (1997)", "rating" : 1.92 }, { "title" : "12 Homens e uma Sentença (1957)", "rating" : 0.95 } ], "father" : { "firstname" : "Simona", "surname" : "Sala", "age" : 38 }, "cat" : { "name" : "Elena", "age" : 15 } }
{ "_id" : ObjectId("5e64438aee36625be4c99cfa"), "firstname" : "Rosa", "surname" : "Colombo", "username" : "user196", "age" : 4, "email" : "Rosa.Colombo@live.com", "bloodType" : "O-", "id_num" : "635220041144", "registerDate" : ISODate("2012-08-12T06:24:18.362Z"), "ticketNumber" : 9872, "jobs" : [ "Design de Moda", "Engenharia Nuclear" ], "favFruits" : [ "Melancia", "Uva", "Mamão" ], "movies" : [ { "title" : "A Origem (2010)", "rating" : 4.45 }, { "title" : "O Resgate do Soldado Ryan (1998)", "rating" : 3.8 }, { "title" : "Intocáveis (2011)", "rating" : 4.78 }, { "title" : "A Origem (2010)", "rating" : 0.55 } ], "cat" : { "name" : "Anna", "age" : 17 }, "dog" : { "name" : "Martina", "age" : 3 } }
{ "_id" : ObjectId("5e64438aee36625be4c99d31"), "firstname" : "Simona", "surname" : "Amato", "username" : "user251", "age" : 1, "email" : "Simona.Amato@uol.com.br", "bloodType" : "AB-", "id_num" : "713734754531", "registerDate" : ISODate("2017-08-17T15:03:19.509Z"), "ticketNumber" : 7776, "jobs" : [ "Papel e Celulose" ], "favFruits" : [ "Mamão", "Pêssego" ], "movies" : [ { "title" : "Parasita (2019)", "rating" : 3.43 } ], "cat" : { "name" : "Giusy", "age" : 2 }, "dog" : { "name" : "Paola", "age" : 7 } }
{ "_id" : ObjectId("5e64438aee36625be4c99d39"), "firstname" : "Rita", "surname" : "Farina", "username" : "user259", "age" : 9, "email" : "Rita.Farina@hotmail.com", "bloodType" : "AB+", "id_num" : "337321057236", "registerDate" : ISODate("2019-07-28T11:08:17.813Z"), "ticketNumber" : 54, "jobs" : [ "Medicina", "Ecologia" ], "favFruits" : [ "Tangerina", "Uva" ], "movies" : [ { "title" : "Pulp Fiction: Tempo de Violência (1994)", "rating" : 2.47 } ], "cat" : { "name" : "Rosa", "age" : 15 }, "dog" : { "name" : "Manuela", "age" : 12 } }
{ "_id" : ObjectId("5e64438aee36625be4c99d45"), "firstname" : "Gianni", "surname" : "Marchetti", "username" : "user271", "age" : 7, "email" : "Gianni.Marchetti@uol.com.br", "bloodType" : "AB+", "id_num" : "814088878206", "registerDate" : ISODate("2010-12-31T09:39:02.314Z"), "ticketNumber" : 634, "jobs" : [ "Gestão em Saúde", "Produção Cultural" ], "favFruits" : [ "Maçã", "Laranja" ], "movies" : [ { "title" : "A Felicidade Não se Compra (1946)", "rating" : 1.11 }, { "title" : "O Poderoso Chefão II (1974)", "rating" : 0.53 } ], "cat" : { "name" : "Cristina", "age" : 10 }, "dog" : { "name" : "Tiziana", "age" : 1 } }
{ "_id" : ObjectId("5e64438aee36625be4c99d52"), "firstname" : "Massimo", "surname" : "Vitali", "username" : "user284", "age" : 3, "email" : "Massimo.Vitali@yahoo.com", "bloodType" : "O-", "id_num" : "345583516183", "registerDate" : ISODate("2015-03-28T15:53:28.144Z"), "ticketNumber" : 3531, "jobs" : [ "Segurança no Trabalho", "Engenharia de Energia" ], "favFruits" : [ "Banana" ], "movies" : [ { "title" : "A Origem (2010)", "rating" : 3.68 } ], "cat" : { "name" : "Dario", "age" : 14 }, "dog" : { "name" : "Alessandro", "age" : 12 } }
{ "_id" : ObjectId("5e64438aee36625be4c99d68"), "firstname" : "Antonella", "surname" : "Russo", "username" : "user306", "age" : 4, "email" : "Antonella.Russo@live.com", "bloodType" : "O+", "id_num" : "356841516236", "registerDate" : ISODate("2014-10-21T04:07:52.183Z"), "ticketNumber" : 9965, "jobs" : [ "Ciência e Tecnologia de Alimentos", "Defesa e Gestão Estratégica Internacional" ], "favFruits" : [ "Goiaba", "Banana" ], "movies" : [ { "title" : "Os Bons Companheiros (1990)", "rating" : 1.9 }, { "title" : "Vingadores: Ultimato (2019)", "rating" : 0.18 }, { "title" : "Seven: Os Sete Crimes Capitais (1995)", "rating" : 4.75 }, { "title" : "12 Homens e uma Sentença (1957)", "rating" : 0.17 }, { "title" : "O Resgate do Soldado Ryan (1998)", "rating" : 0.5 } ], "cat" : { "name" : "Mirko", "age" : 15 }, "dog" : { "name" : "Giuseppe", "age" : 10 } }
{ "_id" : ObjectId("5e64438aee36625be4c99d6f"), "firstname" : "Alessia", "surname" : "Esposito", "username" : "user313", "age" : 4, "email" : "Alessia.Esposito@hotmail.com", "bloodType" : "A-", "id_num" : "462488164252", "registerDate" : ISODate("2008-04-04T16:23:41.932Z"), "ticketNumber" : 6938, "jobs" : [ "Música", "Ciências Exatas e Informática" ], "favFruits" : [ "Tangerina" ], "movies" : [ { "title" : "1917 (2019)", "rating" : 0.58 }, { "title" : "Harakiri (1962)", "rating" : 1.64 } ], "father" : { "firstname" : "Michele", "surname" : "Esposito", "age" : 28 }, "cat" : { "name" : "Daniele", "age" : 5 }, "dog" : { "name" : "Massimo", "age" : 8 } }
{ "_id" : ObjectId("5e64438bee36625be4c99d9b"), "firstname" : "Enrico", "surname" : "Sanna", "username" : "user357", "age" : 4, "email" : "Enrico.Sanna@outlook.com", "bloodType" : "AB+", "id_num" : "538537370608", "registerDate" : ISODate("2018-01-05T16:14:49.552Z"), "ticketNumber" : 5168, "jobs" : [ "Nutrição" ], "favFruits" : [ "Banana", "Tangerina", "Kiwi" ], "movies" : [ { "title" : "A Vida é Bela (1997)", "rating" : 4.55 }, { "title" : "A Viagem de Chihiro (2001)", "rating" : 1.75 }, { "title" : "Os Sete Samurais (1954)", "rating" : 4.76 }, { "title" : "A Viagem de Chihiro (2001)", "rating" : 3.28 } ], "cat" : { "name" : "Filipo", "age" : 16 }, "dog" : { "name" : "Salvatore", "age" : 16 } }
{ "_id" : ObjectId("5e64438bee36625be4c99dad"), "firstname" : "Daniele", "surname" : "Riva", "username" : "user375", "age" : 13, "email" : "Daniele.Riva@hotmail.com", "bloodType" : "A-", "id_num" : "552245430724", "registerDate" : ISODate("2010-04-01T19:14:51.041Z"), "ticketNumber" : 5467, "jobs" : [ "Agronomia", "Naturologia" ], "favFruits" : [ "Maçã", "Uva" ], "movies" : [ { "title" : "Seven: Os Sete Crimes Capitais (1995)", "rating" : 1.97 }, { "title" : "Batman: O Cavaleiro das Trevas (2008)", "rating" : 4.83 }, { "title" : "Pulp Fiction: Tempo de Violência (1994)", "rating" : 3.23 } ], "cat" : { "name" : "Veronica", "age" : 16 } }
{ "_id" : ObjectId("5e64438bee36625be4c99dba"), "firstname" : "Marco", "surname" : "Silvestri", "username" : "user388", "age" : 6, "email" : "Marco.Silvestri@uol.com.br", "bloodType" : "A-", "id_num" : "556532730738", "registerDate" : ISODate("2013-10-01T23:28:16.635Z"), "ticketNumber" : 1402, "jobs" : [ "Gestão da Tecnologia da Informação", "Gestão Ambiental" ], "favFruits" : [ "Maçã", "Kiwi" ], "movies" : [ { "title" : "Cidade de Deus (2002)", "rating" : 2.29 }, { "title" : "Vingadores: Ultimato (2019)", "rating" : 3.02 }, { "title" : "Um Sonho de Liberdade (1994)", "rating" : 3.55 }, { "title" : "Matrix (1999)", "rating" : 2.59 }, { "title" : "Interestelar (2014)", "rating" : 0.43 } ], "cat" : { "name" : "Cristina", "age" : 10 }, "dog" : { "name" : "Daniela", "age" : 2 } }
{ "_id" : ObjectId("5e64438bee36625be4c99dc6"), "firstname" : "Emanuela", "surname" : "Bellini", "username" : "user400", "age" : 6, "email" : "Emanuela.Bellini@yahoo.com", "bloodType" : "B+", "id_num" : "221776427164", "registerDate" : ISODate("2015-05-22T06:44:39.850Z"), "ticketNumber" : 300, "jobs" : [ "Engenharia Naval", "Gestão em Saúde" ], "favFruits" : [ "Tangerina", "Pêssego" ], "movies" : [ { "title" : "Vingadores: Ultimato (2019)", "rating" : 4.83 }, { "title" : "12 Homens e uma Sentença (1957)", "rating" : 2.22 }, { "title" : "Gladiador (2000)", "rating" : 2.65 }, { "title" : "A Origem (2010)", "rating" : 3.72 }, { "title" : "Guerra nas Estrelas (1977)", "rating" : 4.91 } ], "mother" : { "firstname" : "Simona", "surname" : "Bellini", "age" : 30 }, "cat" : { "name" : "Giorgia", "age" : 13 } }
{ "_id" : ObjectId("5e64438bee36625be4c99dca"), "firstname" : "Alberto", "surname" : "Rossi", "username" : "user404", "age" : 3, "email" : "Alberto.Rossi@uol.com.br", "bloodType" : "AB-", "id_num" : "121230316772", "registerDate" : ISODate("2010-11-01T21:25:31.619Z"), "ticketNumber" : 4606, "jobs" : [ "Ciências Contábeis" ], "favFruits" : [ "Maçã", "Mamão" ], "movies" : [ { "title" : "Os Sete Samurais (1954)", "rating" : 0.99 }, { "title" : "A Felicidade Não se Compra (1946)", "rating" : 2.81 } ], "cat" : { "name" : "Andrea", "age" : 6 } }
{ "_id" : ObjectId("5e64438bee36625be4c99dcd"), "firstname" : "Domenico", "surname" : "Bruno", "username" : "user407", "age" : 5, "email" : "Domenico.Bruno@uol.com.br", "bloodType" : "O-", "id_num" : "156754043531", "registerDate" : ISODate("2008-04-26T03:55:39.628Z"), "ticketNumber" : 4089, "jobs" : [ "Artes Visuais", "Saúde Coletiva" ], "favFruits" : [ "Melancia", "Banana", "Laranja" ], "movies" : [ { "title" : "12 Homens e uma Sentença (1957)", "rating" : 4.46 }, { "title" : "O Resgate do Soldado Ryan (1998)", "rating" : 3.52 }, { "title" : "Três Homens em Conflito (1966)", "rating" : 4.79 }, { "title" : "Seven: Os Sete Crimes Capitais (1995)", "rating" : 1.99 } ], "mother" : { "firstname" : "Massimiliano", "surname" : "Bruno", "age" : 30 }, "cat" : { "name" : "Enzo ", "age" : 13 } }
Type "it" for more


9 Liste as pessoas que tem o mesmo nome que seu bichano (gatou ou cachorro)
> db.italians.find({$or: [{"$expr": { "$eq": [ "$firstname" , "$cat.name" ]}}, {"$expr": { "$eq": [ "$firstname" , "$dog.name" ]}}]})</br>

{ "_id" : ObjectId("5e64438aee36625be4c99d15"), "firstname" : "Lorenzo", "surname" : "Russo", "username" : "user223", "age" : 17, "email" : "Lorenzo.Russo@uol.com.br", "bloodType" : "A+", "id_num" : "632641862782", "registerDate" : ISODate("2019-11-16T15:21:37.571Z"), "ticketNumber" : 9367, "jobs" : [ "Construção Civil", "Medicina Veterinária" ], "favFruits" : [ "Laranja", "Goiaba" ], "movies" : [ { "title" : "12 Homens e uma Sentença (1957)", "rating" : 1.14 }, { "title" : "Forrest Gump: O Contador de Histórias (1994)", "rating" : 4.7 } ], "cat" : { "name" : "Lorenzo", "age" : 9 }, "dog" : { "name" : "Giusy", "age" : 16 } }
{ "_id" : ObjectId("5e64438aee36625be4c99d1c"), "firstname" : "Rita", "surname" : "Marchetti", "username" : "user230", "age" : 72, "email" : "Rita.Marchetti@hotmail.com", "bloodType" : "A-", "id_num" : "745602420823", "registerDate" : ISODate("2017-07-09T22:37:39.523Z"), "ticketNumber" : 1591, "jobs" : [ "Defesa e Gestão Estratégica Internacional", "Zootecnia" ], "favFruits" : [ "Maçã" ], "movies" : [ { "title" : "A Lista de Schindler (1993)", "rating" : 1.42 } ], "cat" : { "name" : "Rita", "age" : 15 } }
{ "_id" : ObjectId("5e64438bee36625be4c99def"), "firstname" : "Marta", "surname" : "Rizzo", "username" : "user441", "age" : 13, "email" : "Marta.Rizzo@uol.com.br", "bloodType" : "O+", "id_num" : "043743488034", "registerDate" : ISODate("2013-03-15T05:23:06.802Z"), "ticketNumber" : 460, "jobs" : [ "Engenharia de Inovação" ], "favFruits" : [ "Banana", "Maçã" ], "movies" : [ { "title" : "12 Homens e uma Sentença (1957)", "rating" : 1.39 }, { "title" : "Interestelar (2014)", "rating" : 2.14 }, { "title" : "Forrest Gump: O Contador de Histórias (1994)", "rating" : 3.91 }, { "title" : "Gladiador (2000)", "rating" : 1.98 } ], "father" : { "firstname" : "Daniele", "surname" : "Rizzo", "age" : 33 }, "cat" : { "name" : "Marta", "age" : 12 } }
{ "_id" : ObjectId("5e64438bee36625be4c99ec6"), "firstname" : "Serena", "surname" : "Lombardo", "username" : "user656", "age" : 54, "email" : "Serena.Lombardo@gmail.com", "bloodType" : "B-", "id_num" : "880633470378", "registerDate" : ISODate("2014-07-12T03:52:43.486Z"), "ticketNumber" : 4309, "jobs" : [ "Oftálmica", "Sistemas Biomédicos" ], "favFruits" : [ "Kiwi", "Maçã", "Tangerina" ], "movies" : [ { "title" : "Coringa (2019)", "rating" : 3 } ], "cat" : { "name" : "Claudio", "age" : 5 }, "dog" : { "name" : "Serena", "age" : 15 } }
{ "_id" : ObjectId("5e64438cee36625be4c99f7c"), "firstname" : "Giuseppe", "surname" : "Sartori", "username" : "user838", "age" : 3, "email" : "Giuseppe.Sartori@hotmail.com", "bloodType" : "AB-", "id_num" : "336585274316", "registerDate" : ISODate("2016-08-26T18:48:33.543Z"), "ticketNumber" : 4500, "jobs" : [ "Biotecnologia" ], "favFruits" : [ "Pêssego", "Tangerina" ], "movies" : [ { "title" : "O Senhor dos Anéis: As Duas Torres (2002)", "rating" : 0.46 } ], "cat" : { "name" : "Giuseppe", "age" : 6 } }
{ "_id" : ObjectId("5e64438cee36625be4c99f89"), "firstname" : "Giorgia", "surname" : "Fiore", "username" : "user851", "age" : 34, "email" : "Giorgia.Fiore@live.com", "bloodType" : "AB-", "id_num" : "401832541584", "registerDate" : ISODate("2008-08-17T09:34:22.761Z"), "ticketNumber" : 8318, "jobs" : [ "Filosofia" ], "favFruits" : [ "Mamão", "Banana", "Kiwi" ], "movies" : [ { "title" : "Star Wars, Episódio V: O Império Contra-Ataca (1980)", "rating" : 3.43 }, { "title" : "Star Wars, Episódio V: O Império Contra-Ataca (1980)", "rating" : 2.33 }, { "title" : "Clube da Luta (1999)", "rating" : 4.78 } ], "cat" : { "name" : "Valentina", "age" : 6 }, "dog" : { "name" : "Giorgia", "age" : 5 } }
{ "_id" : ObjectId("5e64438cee36625be4c99f8a"), "firstname" : "Manuela", "surname" : "Carbone", "username" : "user852", "age" : 54, "email" : "Manuela.Carbone@hotmail.com", "bloodType" : "AB-", "id_num" : "164656148165", "registerDate" : ISODate("2019-08-04T10:46:46.773Z"), "ticketNumber" : 9935, "jobs" : [ "Dança" ], "favFruits" : [ "Melancia", "Kiwi" ], "movies" : [ { "title" : "Forrest Gump: O Contador de Histórias (1994)", "rating" : 0.61 }, { "title" : "Parasita (2019)", "rating" : 4.28 }, { "title" : "O Senhor dos Anéis: A Sociedade do Anel (2001)", "rating" : 4.65 } ], "father" : { "firstname" : "Alessandro", "surname" : "Carbone", "age" : 81 }, "cat" : { "name" : "Manuela", "age" : 4 }, "dog" : { "name" : "Federica", "age" : 7 } }
{ "_id" : ObjectId("5e64438cee36625be4c99fb4"), "firstname" : "Matteo", "surname" : "Gallo", "username" : "user894", "age" : 5, "email" : "Matteo.Gallo@live.com", "bloodType" : "A+", "id_num" : "622778018178", "registerDate" : ISODate("2015-08-30T12:26:37.867Z"), "ticketNumber" : 6663, "jobs" : [ "Psicologia", "Gestão de Segurança Privada" ], "favFruits" : [ "Kiwi", "Uva", "Kiwi" ], "movies" : [ { "title" : "Star Wars, Episódio V: O Império Contra-Ataca (1980)", "rating" : 4.43 }, { "title" : "Um Sonho de Liberdade (1994)", "rating" : 4.54 }, { "title" : "Os Sete Samurais (1954)", "rating" : 1.93 }, { "title" : "O Senhor dos Anéis: A Sociedade do Anel (2001)", "rating" : 1.4 }, { "title" : "Harakiri (1962)", "rating" : 4.82 } ], "cat" : { "name" : "Matteo", "age" : 3 } }
{ "_id" : ObjectId("5e64438cee36625be4c99fcf"), "firstname" : "Roberto", "surname" : "Pellegrini", "username" : "user921", "age" : 27, "email" : "Roberto.Pellegrini@yahoo.com", "bloodType" : "B+", "id_num" : "606425155581", "registerDate" : ISODate("2010-08-13T22:41:26.839Z"), "ticketNumber" : 2144, "jobs" : [ "Ciências Sociais" ], "favFruits" : [ "Mamão", "Kiwi" ], "movies" : [ { "title" : "O Senhor dos Anéis: O Retorno do Rei (2003)", "rating" : 4.51 } ], "dog" : { "name" : "Roberto", "age" : 2 } }
{ "_id" : ObjectId("5e64438cee36625be4c99fdd"), "firstname" : "Alessia", "surname" : "Conte", "username" : "user935", "age" : 76, "email" : "Alessia.Conte@live.com", "bloodType" : "B-", "id_num" : "513222440620", "registerDate" : ISODate("2007-02-18T14:02:27.499Z"), "ticketNumber" : 9799, "jobs" : [ "Produção Multimídia" ], "favFruits" : [ "Maçã", "Uva", "Mamão" ], "movies" : [ { "title" : "O Senhor dos Anéis: A Sociedade do Anel (2001)", "rating" : 1.05 }, { "title" : "Matrix (1999)", "rating" : 4.02 }, { "title" : "12 Homens e uma Sentença (1957)", "rating" : 4.65 }, { "title" : "Um Estranho no Ninho (1975)", "rating" : 0.56 }, { "title" : "À Espera de um Milagre (1999)", "rating" : 1.43 } ], "cat" : { "name" : "Alessia", "age" : 1 } }
{ "_id" : ObjectId("5e64438dee36625be4c9a075"), "firstname" : "Sabrina", "surname" : "Sanna", "username" : "user1087", "age" : 12, "email" : "Sabrina.Sanna@gmail.com", "bloodType" : "O-", "id_num" : "245748011768", "registerDate" : ISODate("2015-08-23T01:56:35.678Z"), "ticketNumber" : 8513, "jobs" : [ "Design" ], "favFruits" : [ "Uva", "Melancia", "Mamão" ], "movies" : [ { "title" : "Interestelar (2014)", "rating" : 1.06 }, { "title" : "Coringa (2019)", "rating" : 4.98 }, { "title" : "Star Wars, Episódio V: O Império Contra-Ataca (1980)", "rating" : 4.23 }, { "title" : "Batman: O Cavaleiro das Trevas (2008)", "rating" : 1.41 }, { "title" : "Seven: Os Sete Crimes Capitais (1995)", "rating" : 0.04 } ], "cat" : { "name" : "Claudio", "age" : 15 }, "dog" : { "name" : "Sabrina", "age" : 11 } }
{ "_id" : ObjectId("5e64438dee36625be4c9a122"), "firstname" : "Mario", "surname" : "Conte", "username" : "user1260", "age" : 51, "email" : "Mario.Conte@outlook.com", "bloodType" : "O-", "id_num" : "853002031584", "registerDate" : ISODate("2011-05-02T10:34:33.645Z"), "ticketNumber" : 2001, "jobs" : [ "Sistemas de Telecomunicações", "Processos Químicos" ], "favFruits" : [ "Tangerina" ], "movies" : [ { "title" : "Um Estranho no Ninho (1975)", "rating" : 4.25 } ], "cat" : { "name" : "Mario", "age" : 8 }, "dog" : { "name" : "Fabio", "age" : 5 } }
{ "_id" : ObjectId("5e64438dee36625be4c9a155"), "firstname" : "Enzo ", "surname" : "Palmieri", "username" : "user1311", "age" : 61, "email" : "Enzo .Palmieri@hotmail.com", "bloodType" : "O-", "id_num" : "461736042847", "registerDate" : ISODate("2016-04-18T23:22:54.165Z"), "ticketNumber" : 5927, "jobs" : [ "Sistemas de Telecomunicações", "Engenharia Agrícola" ], "favFruits" : [ "Kiwi", "Mamão", "Tangerina" ], "movies" : [ { "title" : "Star Wars, Episódio V: O Império Contra-Ataca (1980)", "rating" : 0.8 }, { "title" : "A Vida é Bela (1997)", "rating" : 2.15 }, { "title" : "Harakiri (1962)", "rating" : 3.31 }, { "title" : "O Poderoso Chefão (1972)", "rating" : 3.56 }, { "title" : "O Senhor dos Anéis: O Retorno do Rei (2003)", "rating" : 4.55 } ], "father" : { "firstname" : "Sabrina", "surname" : "Palmieri", "age" : 98 }, "cat" : { "name" : "Enzo ", "age" : 17 } }
{ "_id" : ObjectId("5e64438eee36625be4c9a239"), "firstname" : "Fabio", "surname" : "Orlando", "username" : "user1539", "age" : 18, "email" : "Fabio.Orlando@outlook.com", "bloodType" : "O+", "id_num" : "370300146150", "registerDate" : ISODate("2019-05-20T11:01:03.211Z"), "ticketNumber" : 4494, "jobs" : [ "Ciências Humanas" ], "favFruits" : [ "Kiwi", "Banana" ], "movies" : [ { "title" : "Clube da Luta (1999)", "rating" : 0.21 }, { "title" : "Um Sonho de Liberdade (1994)", "rating" : 3.12 } ], "father" : { "firstname" : "Cinzia", "surname" : "Orlando", "age" : 38 }, "cat" : { "name" : "Veronica", "age" : 6 }, "dog" : { "name" : "Fabio", "age" : 2 } }
{ "_id" : ObjectId("5e64438eee36625be4c9a262"), "firstname" : "Maria", "surname" : "Valentini", "username" : "user1580", "age" : 9, "email" : "Maria.Valentini@hotmail.com", "bloodType" : "B+", "id_num" : "758828672371", "registerDate" : ISODate("2013-03-22T22:34:01.740Z"), "ticketNumber" : 885, "jobs" : [ "Relações Internacionais" ], "favFruits" : [ "Maçã" ], "movies" : [ { "title" : "O Poderoso Chefão (1972)", "rating" : 2.66 }, { "title" : "1917 (2019)", "rating" : 1.15 }, { "title" : "Os Sete Samurais (1954)", "rating" : 4.57 }, { "title" : "A Felicidade Não se Compra (1946)", "rating" : 3.07 }, { "title" : "O Poderoso Chefão (1972)", "rating" : 3.07 } ], "cat" : { "name" : "Roberto", "age" : 5 }, "dog" : { "name" : "Maria", "age" : 6 } }
{ "_id" : ObjectId("5e64438eee36625be4c9a284"), "firstname" : "Luca", "surname" : "Ferretti", "username" : "user1614", "age" : 27, "email" : "Luca.Ferretti@yahoo.com", "bloodType" : "A-", "id_num" : "675030507530", "registerDate" : ISODate("2016-06-15T00:12:22.568Z"), "ticketNumber" : 9311, "jobs" : [ "Ciências Exatas e Informática" ], "favFruits" : [ "Tangerina", "Laranja" ], "movies" : [ { "title" : "O Poderoso Chefão II (1974)", "rating" : 2.56 } ], "mother" : { "firstname" : "Laura", "surname" : "Ferretti", "age" : 52 }, "cat" : { "name" : "Luca", "age" : 5 } }
{ "_id" : ObjectId("5e64438fee36625be4c9a378"), "firstname" : "Patrizia", "surname" : "Farina", "username" : "user1858", "age" : 72, "email" : "Patrizia.Farina@gmail.com", "bloodType" : "O+", "id_num" : "652348368087", "registerDate" : ISODate("2018-01-22T05:53:17.878Z"), "ticketNumber" : 3890, "jobs" : [ "Nutrição", "Gestão Desportiva e de Lazer" ], "favFruits" : [ "Pêssego", "Laranja" ], "movies" : [ { "title" : "Três Homens em Conflito (1966)", "rating" : 1.76 }, { "title" : "Os Bons Companheiros (1990)", "rating" : 1.68 }, { "title" : "Três Homens em Conflito (1966)", "rating" : 0.48 }, { "title" : "Três Homens em Conflito (1966)", "rating" : 2.06 }, { "title" : "Intocáveis (2011)", "rating" : 0.74 } ], "cat" : { "name" : "Patrizia", "age" : 8 } }
{ "_id" : ObjectId("5e64438fee36625be4c9a395"), "firstname" : "Daniele", "surname" : "Villa", "username" : "user1887", "age" : 4, "email" : "Daniele.Villa@uol.com.br", "bloodType" : "B+", "id_num" : "503171675255", "registerDate" : ISODate("2015-11-26T15:04:47.355Z"), "ticketNumber" : 1816, "jobs" : [ "Filosofia" ], "favFruits" : [ "Mamão", "Kiwi" ], "movies" : [ { "title" : "Um Sonho de Liberdade (1994)", "rating" : 0.51 }, { "title" : "À Espera de um Milagre (1999)", "rating" : 2.97 }, { "title" : "Um Estranho no Ninho (1975)", "rating" : 2.2 }, { "title" : "Um Sonho de Liberdade (1994)", "rating" : 3.93 } ], "mother" : { "firstname" : "Giorgio", "surname" : "Villa", "age" : 32 }, "cat" : { "name" : "Daniele", "age" : 15 } }
{ "_id" : ObjectId("5e64438fee36625be4c9a41d"), "firstname" : "Sara", "surname" : "Piras", "username" : "user2023", "age" : 4, "email" : "Sara.Piras@hotmail.com", "bloodType" : "O-", "id_num" : "751772256831", "registerDate" : ISODate("2016-03-16T10:59:51.979Z"), "ticketNumber" : 1556, "jobs" : [ "Libras" ], "favFruits" : [ "Laranja", "Tangerina", "Laranja" ], "movies" : [ { "title" : "Guerra nas Estrelas (1977)", "rating" : 1.91 }, { "title" : "Cidade de Deus (2002)", "rating" : 3.31 }, { "title" : "Guerra nas Estrelas (1977)", "rating" : 1.02 } ], "cat" : { "name" : "Manuela", "age" : 14 }, "dog" : { "name" : "Sara", "age" : 0 } }
{ "_id" : ObjectId("5e64438fee36625be4c9a44e"), "firstname" : "Patrizia", "surname" : "Grasso", "username" : "user2072", "age" : 14, "email" : "Patrizia.Grasso@hotmail.com", "bloodType" : "AB+", "id_num" : "732288622558", "registerDate" : ISODate("2007-05-28T08:00:37.484Z"), "ticketNumber" : 9233, "jobs" : [ "Pilotagem profissional de aeronaves", "Biotecnologia" ], "favFruits" : [ "Laranja", "Goiaba" ], "movies" : [ { "title" : "A Lista de Schindler (1993)", "rating" : 3.94 }, { "title" : "Batman: O Cavaleiro das Trevas (2008)", "rating" : 0.02 } ], "cat" : { "name" : "Patrizia", "age" : 0 } }
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

2. Liste as ações com perdas (limite a 10 novamente)

3. Liste as 10 ações mais rentáveis


4. Qual foi o setor mais rentável?

5. Ordene as ações pelo profit e usando um cursor, liste as ações.

6. Renomeie o campo “Profit Margin” para apenas “profit”.

7. Agora liste apenas a empresa e seu respectivo resultado

8. Analise as ações. É uma bola de cristal na sua mão... Quais as três ações você investiria?

9. Liste as ações agrupadas por setor





