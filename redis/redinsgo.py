import redis
import json
import re

COUNT = 'count'
SCORES = 'scores'
CARDS = 'cards'
PARTICIPANTS = 'participants'
USER = 'user:'
CARD = 'card:'
SCORE = 'score:'
redis = redis.Redis('localhost')

class Participant:
    def __init__(self, name: str, bcartela: str, bscore: str) -> None:
        self.name = name
        self.bcartela = bcartela
        self.bscore = bscore

def game() -> None:
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
    redis.set(COUNT, 0)
    while int(redis.get(COUNT)) < 50:
        position = str(int(redis.incr(COUNT)))
        set_cards_participant(position)
        set_score_participant(position)
        p = Participant(USER + position, CARD + position, SCORE + position)
        redis.set(USER + position, json.dumps(p.__dict__))
        
def set_score_participant(hash_position: str) -> None:
    redis.zadd(SCORES, {SCORE + hash_position: 0})

def set_cards_participant(hash_position: str) -> None:
    while redis.scard(CARD + hash_position) < 15:
        redis.sadd(CARD + hash_position, redis.srandmember(CARDS))

def generate_cards(hash: str) -> None:
    redis.set(COUNT, 0)
    while int(redis.get(COUNT)) < 99:
        redis.sadd(hash, int(redis.incr(COUNT)))

if __name__ == '__main__':
    redis.flushall()
    game()
    

