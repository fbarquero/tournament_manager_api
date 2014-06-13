# coding: utf8
# try something like
__author__ = 'Mordigan'
import random
import math

@service.json
def algo():
    personas = db.tournament.ALL
    print "test"
algo()



def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@request.restful()
def get_initial_bracket():
    def GET(belt,initial_weight, end_weight, gender, year_of_born):
        db(fighter.name)
        return dict()


def generate_bracket():

    match_maker(shuffle_players(players))


def shuffle_players(players):
    amount_of_players = len(players) - 1
    while amount_of_players != 0:
        random_generated = random.randint(0, amount_of_players)
        aux_player = players[random_generated]
        players[random_generated] = players[amount_of_players]
        players[amount_of_players] = aux_player
        amount_of_players -= 1
    return players


def match_maker(shuffled_players):
    # Object that will represents the bracket
    bracket = []
    # Represents the round matches
    matches = {'teams':[], 'results':[]}
    # Number of matches in the first round
    byes = 0
    count = 0
    byed_players = []
    if is_power_of_two(len(shuffled_players)):
        while count != len(shuffled_players) / 2:
            matches['teams'].append([shuffled_players[count], shuffled_players[(len(shuffled_players) - 1) - count]])
            matches['results'].append([0, 0])
            count += 1
        bracket.append(matches)
    else:
        next_higher_power_of_two = get_next_higher_power_of_two(len(shuffled_players))
        byes = next_higher_power_of_two - len(shuffled_players)
        random_used = []
        count = 0
        while count < byes:
            while True:
                rand_num = random.randint(0, len(shuffled_players)-1)
                if not rand_num in random_used:
                    random_used.append(rand_num)
                    break
            byed_players.append(shuffled_players[random_used[count]])
            shuffled_players.remove(byed_players[count])
            count += 1
        count = 0
        bye_count = 0
        non_byed_player_matches = 0
        if len(shuffled_players) > len(byed_players):
            while count != len(shuffled_players) / 2:
                if bye_count < len(byed_players):
                    matches['teams'].append([byed_players[count], '-- -- --'])
                    matches['results'].append([0, -1])
                    bye_count += 1
                if len(shuffled_players)/2 > non_byed_player_matches:
                    matches['teams'].append([shuffled_players[count], shuffled_players[(len(shuffled_players) - 1) - count]])
                    matches['results'].append([0, 0])
                    non_byed_player_matches += 1
                count += 1
        else:
            while count != next_higher_power_of_two / 2:
                if bye_count < len(byed_players):
                    matches['teams'].append([byed_players[count], '-- -- --'])
                    matches['results'].append([0, -1])
                    bye_count += 1
                if len(shuffled_players)/2 > non_byed_player_matches:
                    matches['teams'].append([shuffled_players[count], shuffled_players[(len(shuffled_players) - 1) - count]])
                    matches['results'].append([0, 0])
                    non_byed_player_matches += 1
                count += 1
    print "Matches dict:"
    print matches
    return matches

def is_power_of_two(number):
    if number == 0:
        return False
    else:
        return (number & (number - 1) == 0) and (number != 0)

def get_next_higher_power_of_two(number_of_players):
    result = 0
    count = 1
    while result < number_of_players:
        result = int(math.pow(2,count))
        count += 1
    return result

def get_exponent_base_two(number):
    exponent = 0
    while number > 1:
        number /= 2
        exponent += 1
    return exponent


#single_elimination_bracket_generation(["1", "2", "3", "4", "5", "6"])

