# coding: utf8
# try something like
__author__ = 'Mordigan'
import random
import math
import json
import sys
from gluon.debug import qdb_debugger

def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

@request.restful()
def belt():
    response.view = 'generic.json'
    def GET(*args,**vars):
        patterns = [
            "/color[belt]"
        ]
        parser = db.parse_as_rest(patterns,args,vars)
        if parser.status == 200:
            return dict(content=parser.response)
        else:
            raise HTTP(parser.status,parser.error)

    def POST(**vars):
        try:
             return dict(message = db.belt.bulk_insert(vars['content']))
        except:
            raise HTTP (400, "Unexpected error: %s" % sys.exc_info()[0], message = sys.exc_info()[0])
            #db.commit()
        #except:
            #db.rollback()
    def PUT(**vars):
        try:
            db(db.belt.id == 7).validate_and_update(description = 'whiteUpdated')
            db.commit()
        except:
            db.rollback()
    return locals()

def single_elimination_bracket_generation(players):
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
        if len(shuffled_players) > len(byed_players):
            while count != len(shuffled_players) / 2:
                if count < len(byed_players):
                    matches['teams'].append([byed_players[count], '-- -- --'])
                    matches['results'].append([0, -1])
                    count += 1
                matches['teams'].append([shuffled_players[count], shuffled_players[(len(shuffled_players) - 1) - count]])
                matches['results'].append([0, 0])
                count += 1
        else:
            while count != next_higher_power_of_two / 2:
                matches['teams'].append([byed_players[count], '-- -- --'])
                matches['results'].append([0, -1])
                if count < len(shuffled_players)/2:
                    matches['teams'].append([shuffled_players[count], shuffled_players[(len(shuffled_players) - 1) - count]])
                    matches['results'].append([0, 0])
                    count += 1
                count += 1
        #bracket.append(matches)
        #print "Byed Players:"
        #print byed_players
        #print "shufled players after bye process:"
        #print shuffled_players
    #bracket = generate_next_rounds(len(shuffled_players), bracket, byed_players)
    #bracket.append([None])
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

#single_elimination_bracket_generation(["alonso", "darian", "michael", "lunita", "5", "6", "7", "8", "alonso2", "darian2", "michael2", "lunita2", "5_2", "6_2", "7_2", "8_2"])
#single_elimination_bracket_generation(["alonso", "darian", "michael", "josue", "lucia", "servet tezagul"])
#single_elimination_bracket_generation(["alonso", "michael", "aaron cook"])
#single_elimination_bracket_generation(["Aroon cook", "Tezaqul", "Tuncat", "Steven L", "nikpah"])
#single_elimination_bracket_generation(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15","16"])
#single_elimination_bracket_generation(["1", "2", "3", "4", "5", "6"])
