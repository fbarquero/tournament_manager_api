__author__ = 'Mordigan'
import random
import math
import datetime


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
    matches = {'teams': [], 'results': []}
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
                rand_num = random.randint(0, len(shuffled_players) - 1)
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
                matches['teams'].append(
                    [shuffled_players[count], shuffled_players[(len(shuffled_players) - 1) - count]])
                matches['results'].append([0, 0])
                count += 1
        else:
            while count != next_higher_power_of_two / 2:
                matches['teams'].append([byed_players[count], '-- -- --'])
                matches['results'].append([0, -1])
                if count < len(shuffled_players) / 2:
                    matches['teams'].append(
                        [shuffled_players[count], shuffled_players[(len(shuffled_players) - 1) - count]])
                    matches['results'].append([0, 0])
                    count += 1
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
        result = int(math.pow(2, count))
        count += 1
    return result


def get_exponent_base_two(number):
    exponent = 0
    while number > 1:
        number /= 2
        exponent += 1
    return exponent


def format_fighers_data(data, belt_info, weight_cat_info, age_cat_info):
    fighterDict = {'athlete': []}
    belt_id = 0
    weight_cat_id = 0
    age_cat_id = 0
    age_cat = ''
    weight_cat = ''
    elite = 0

    for fighterData in data.split('\n').strip():
        fighterDataSplited = fighterData.split(';')
        belt_id = (fighterDataSplited[1], belt_info)
        # Getting age cat for fighter:
        age_cat = get_age_cat(fighterDataSplited[6], age_cat_info)
        weight_cat = get_weight_cat(age_cat, fighterDataSplited[3], fighterDataSplited[2])
        if len(fighterDataSplited) == 7:
            elite = 1
        else:
            elite = 0
        for weight_catategy in weight_cat_info:
            fighterDict['athlete'].append(dict(name=fighterDataSplited[0].strip(),
                                               gender=fighterDataSplited[2].strip(),
                                               weight=fighterDataSplited[3],
                                               year=fighterDataSplited[6],
                                               elite=elite))


def get_belt(description, belt_info):
    for belt in belt_info:
        if belt['description'] == description:
            belt_id = belt['id']


def get_age_cat(year, age_cat_info):
    age_cat = '';
    currentYear = datetime.now().year
    if (currentYear - year) < 12:
        age_cat = 'Infantil'
    elif ((currentYear - year) > 12 and (currentYear - year) <= 14):
        age_cat = 'Cadete'
    elif ((currentYear - year) >= 15 and (currentYear - year) <= 17):
        age_cat = 'Junior'
    elif ((currentYear - year) >= 18 and (currentYear - year) <= 34):
        age_cat = 'Senior'
    elif ((currentYear - year) > 34):
        age_cat = 'Ejecutivo'
    return age_cat


def get_weight_cat(age_cat, weight, gender):
    weight_cat = ''

    # Cadete e Infantil Masculino
    if age_cat == 'Infantil' or 'Cadete' and gender == 'M':
        if 15 <= weight <= 33:
            weight = 'Fin'
        elif 34 <= weight <= 37:
            weight = 'Fly'
        elif 38 <= weight <= 41:
            weight = 'Bantam'
        elif 42 <= weight <= 45:
            weight = 'Feather'
        elif 46 <= weight <= 49:
            weight = 'Light'
        elif 50 <= weight <= 53:
            weight = 'Welter'
        elif 54 <= weight <= 57:
            weight = 'Light Middle'
        elif 58 <= weight <= 61:
            weight = 'Middle'
        elif 62 <= weight <= 63:
            weight = 'Light Heavy'
        elif 64 <= weight:
            weight = 'Heavy'

    # Cadete e Infantil Femenino
    if age_cat == 'Infantil' or 'Cadete' and gender == 'F':
        if 15 <= weight <= 29:
            weight = 'Fin'
        elif 30 <= weight <= 33:
            weight = 'Fly'
        elif 34 <= weight <= 37:
            weight = 'Bantam'
        elif 38 <= weight <= 41:
            weight = 'Feather'
        elif 42 <= weight <= 44:
            weight = 'Light'
        elif 45 <= weight <= 47:
            weight = 'Welter'
        elif 48 <= weight <= 51:
            weight = 'Light Middle'
        elif 52 <= weight <= 55:
            weight = 'Middle'
        elif 56 <= weight <= 59:
            weight = 'Light Heavy'
        elif 60 <= weight:
            weight = 'Heavy'

    # Juvenil Masculino
    if age_cat == 'Junior' and gender == 'M':
        if 15 <= weight <= 45:
            weight = 'Fin'
        elif 46 <= weight <= 48:
            weight = 'Fly'
        elif 49 <= weight <= 51:
            weight = 'Bantam'
        elif 52 <= weight <= 55:
            weight = 'Feather'
        elif 56 <= weight <= 59:
            weight = 'Light'
        elif 60 <= weight <= 63:
            weight = 'Welter'
        elif 64 <= weight <= 68:
            weight = 'Light Middle'
        elif 69 <= weight <= 73:
            weight = 'Middle'
        elif 74 <= weight <= 78:
            weight = 'Light Heavy'
        elif 79 <= weight:
            weight = 'Heavy'

    # Juvenil Femenino
    if age_cat == 'Junior' and gender == 'F':
        if 15 <= weight <= 42:
            weight = 'Fin'
        elif 43 <= weight <= 44:
            weight = 'Fly'
        elif 45 <= weight <= 46:
            weight = 'Bantam'
        elif 47 <= weight <= 49:
            weight = 'Feather'
        elif 50 <= weight <= 52:
            weight = 'Light'
        elif 53 <= weight <= 55:
            weight = 'Welter'
        elif 56 <= weight <= 59:
            weight = 'Light Middle'
        elif 60 <= weight <= 63:
            weight = 'Middle'
        elif 64 <= weight <= 68:
            weight = 'Light Heavy'
        elif 69 <= weight:
            weight = 'Heavy'

    # Senior y Ejecutivo Masculino
    if age_cat == 'Junior' and gender == 'M':
        if 15 <= weight <= 54:
            weight = '-54'
        elif 55 <= weight <= 58:
            weight = '-58'
        elif 59 <= weight <= 63:
            weight = '-63'
        elif 64 <= weight <= 68:
            weight = '-68'
        elif 69 <= weight <= 74:
            weight = '-74'
        elif 75 <= weight <= 80:
            weight = '-80'
        elif 81 <= weight <= 86:
            weight = '-87'
        elif 87 <= weight:
            weight = '+87'

    # Senior y Ejecutivo Femenino
    if age_cat == 'Junior' and gender == 'F':
        if 15 <= weight <= 46:
            weight = '-46'
        elif 47 <= weight <= 49:
            weight = '-49'
        elif 50 <= weight <= 53:
            weight = '-53'
        elif 54 <= weight <= 57:
            weight = '-57'
        elif 58 <= weight <= 62:
            weight = '-62'
        elif 63 <= weight <= 67:
            weight = '-67'
        elif 68 <= weight <= 73:
            weight = '-73'
        elif 74 <= weight:
            weight = '+74'


def test():
    '''
    athletes = {'athlete': []}
    athletes['athlete'].append(dict(name = 'name', fecha = 'fecha', persona = 'persona'))
    '''
    if 56 <= 57.02 <= 58:
        print 'works'


#single_elimination_bracket_generation(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15","16"])
#single_elimination_bracket_generation(["1", "2", "3", "4", "5", "6"])

