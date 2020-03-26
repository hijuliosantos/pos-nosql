1. Crie a tabela com 2 famílias de colunas:
a. Personal-data
b. professional-data

>create 'italians', 'personal-data', 'professional-data'

2. Import o arquivo via linha de comando

>hbase shell /tmp/italians.txt

</br>
</br>
</br>

1. Adicione mais 2 italianos mantendo adicionando informações como data de nascimento nas informações pessoais e um atributo de anos de experiência nas informações profissionais;

>put 'italians', '11', 'personal-data:name',  'Daniel Carlos'</br>
>put 'italians', '11', 'personal-data:city',  'Brazil'</br>
>put 'italians', '11', 'personal-data:birth',  '12/17/1980'</br>
>put 'italians', '11', 'professional-data:role',  'Comunicacao Institucional'</br>
>put 'italians', '11', 'professional-data:salary',  '9000'</br>
>put 'italians', '11', 'professional-data:years',  '20'</br></br>

>put 'italians', '12', 'personal-data:name',  'Joaquim Silva'</br>
>put 'italians', '12', 'personal-data:city',  'Brazil'</br>
>put 'italians', '12', 'personal-data:birth',  '12/17/1990'</br>
>put 'italians', '12', 'professional-data:role',  'Comunicacao Institucional'</br>
>put 'italians', '12', 'professional-data:salary',  '5000'</br>
>put 'italians', '12', 'professional-data:years',  '12'

2. Adicione o controle de 5 versões na tabela de dados pessoais.

>alter 'italians', NAME => 'personal-data', VERSIONS => 5

3. Faça 5 alterações em um dos italianos;

>put 'italians', '12', 'personal-data:years',  '20'</br>
>put 'italians', '12', 'personal-data:city',  'Peru'</br>
>put 'italians', '12', 'personal-data:city',  'Venezuela'</br>
>put 'italians', '12', 'personal-data:city',  'Argentina'</br>
>put 'italians', '12', 'personal-data:city',  'Uruguay'

4. Com o operador get, verifique como o HBase armazenou o histórico.

>get 'italians', 12, {COLUMN=>'personal-data:city', VERSIONS=>5}

>personal-data:city                                          timestamp=1585180676609, value=Uruguay</br>
 personal-data:city                                          timestamp=1585180674971, value=Argentina</br>
 personal-data:city                                          timestamp=1585180674943, value=Venezuela</br>
 personal-data:city                                          timestamp=1585180674915, value=Peru</br>
 personal-data:city                                          timestamp=1585179900506, value=Brazil


5. Utilize o scan para mostrar apenas o nome e profissão dos italianos.

>scan 'italians', {COLUMNS =>['personal-data:name', 'professional-data:role']}

6. Apague os italianos com row id ímpar

>deleteall 'italians', 1</br>
>deleteall 'italians', 3</br>
>deleteall 'italians', 5</br>
>deleteall 'italians', 7</br>
>deleteall 'italians', 9</br>
>deleteall 'italians', 11

7. Crie um contador de idade 55 para o italiano de row id 5

>incr 'italians', 5, 'personal-data:age', 55
>get_counter 'italians', 5, 'personal-data:age'

8. Incremente a idade do italiano em 1

>incr 'italians', 5, 'personal-data:age', 1





