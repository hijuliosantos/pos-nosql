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
