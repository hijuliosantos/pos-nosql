import json
import re

import redis

COUNT = 'count'
SCORES = 'scores'
CARDS = 'cards'
PARTICIPANTS = 'participants'
USER = 'user:'
CARD = 'card:'
SCORE = 'score:'
redis = redis.Redis('localhost')

class Participant:
    """
    Classe correspondente ao participante do jogo. Uilizada para gerar a estrutura de json.
    
    Parameters:
        name: hash correspondente ao nome do participante
        bcartela: hash das cartelas do participante
        bscore: hash correspondente ao score do participante
    """
    def __init__(self, name: str, bcartela: str, bscore: str) -> None:
        self.name = name
        self.bcartela = bcartela
        self.bscore = bscore

def game() -> None:
    """
    Método correspondente ao funcionamento do jogo. Ele gerá os participantes e sorteia as cartelas (80)
    para o jogo. A cada sorteio, a cartela será listada. Quando algum participante  atingir 15 pontos,
    o método listará o parcipante e será finalizado. Se não houver vencedores, será listado.
    """
    generate_cards(CARDS)
    generate_participants()

    print('Start of the game!!')
    numbers = redis.spop(CARDS, 80)
    for index, number in enumerate(numbers):
        number = int(number)
        print(f'Round {index+1}: {number}')
        round_winners = ''
        for i in range(1, 51):
            i = str(i)
            if redis.sismember(CARD + i, number):
                redis.zincrby(SCORES, 1, SCORE + i)
                round_winners += f'player {i} - score {redis.zscore("scores", SCORE + i)} | '

        print('Round winners: ' + round_winners)           
        winners = redis.zrangebyscore(SCORES, 15, 15)
        if winners:
            winners = [re.sub(r'\D', '', str(s)) for s in winners]
            print('Winning participant(s): ' + str(winners))
            print('End of the game')
            return
    print('No winner...')

def generate_participants() -> None:
    """Cria no redis 50 participanes e define os seus componentes (cartelas e score)."""
    redis.set(COUNT, 0)
    while int(redis.get(COUNT)) < 50:
        position = str(int(redis.incr(COUNT)))
        set_cards_participant(position)
        set_score_participant(position)
        p = Participant(USER + position, CARD + position, SCORE + position)
        redis.set(USER + position, json.dumps(p.__dict__))
        
def set_score_participant(hash_position: str) -> None:
    """
    Cria o score do participante com um valor inicial de 0.
    
    Parameters:
        hash_position: número do usuário.
    """
    redis.zadd(SCORES, {SCORE + hash_position: 0})

def set_cards_participant(hash_position: str) -> None:
    """
    Cria as cartelas do participante.

    Parameters:
        hash_position: número do usuário.
    """
    while redis.scard(CARD + hash_position) < 15:
        redis.sadd(CARD + hash_position, redis.srandmember(CARDS))

def generate_cards(hash: str) -> None:
    """
    Cria cartelas com os números de 1-99.

    Parameters:
        hash: hash das cartelas.
    """
    redis.set(COUNT, 0)
    while int(redis.get(COUNT)) < 99:
        redis.sadd(hash, int(redis.incr(COUNT)))

if __name__ == '__main__':
    redis.flushall()
    game()
    

