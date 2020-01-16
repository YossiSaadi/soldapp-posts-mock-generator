import random
import time
import itertools

LIST_SIZE = 1000


def str_time_prop(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%d/%m/%Y', prop)


def rand(lst):
    return random.choice(lst)


if __name__ == '__main__':

    # where
    places_cities_israel = open("cities_israel.txt", "r", encoding="utf8").read().splitlines()

    festivals_international = open("festivals_international.txt", "r", encoding="utf8").read().splitlines()

    festivals_israel = open("festivals_israel.txt", "r", encoding="utf8").read().splitlines()

    places_basketball_stadiums_israel = open("places_basketball_stadiums_israel.txt", "r",
                                             encoding="utf8").read().splitlines()

    places_football_stadiums_international = open("places_football_stadiums_international.txt", "r",
                                                  encoding="utf8").read().splitlines()
    places_football_stadiums_israel = open("places_football_stadiums_israel.txt", "r",
                                           encoding="utf8").read().splitlines()

    places_shows_stadiums_israel = open("places_shows_stadiums_israel.txt", "r", encoding="utf8").read().splitlines()

    shows_standup_band_israel = open("shows_standup_band_israel.txt", "r", encoding="utf8").read().splitlines()
    shows_standup_single_israel = open("shows_standup_single_israel.txt", "r", encoding="utf8").read().splitlines()

    singers_band_israel = open("singers_band_israel.txt", "r", encoding="utf8").read().splitlines()
    singers_single_international = open("singers_single_international.txt", "r", encoding="utf8").read().splitlines()
    singers_single_israel = open("singers_single_israel.txt", "r", encoding="utf8").read().splitlines()

    sport_basketball_teams_international = open("sport_basketball_teams_international.txt", "r",
                                                encoding="utf8").read().splitlines()
    sport_basketball_teams_israel = open("sport_basketball_teams_israel.txt", "r", encoding="utf8").read().splitlines()

    sport_basketball_tournaments_international = open("sport_basketball_tournaments_international.txt", "r",
                                                      encoding="utf8").read().splitlines()
    sport_basketball_tournaments_israel = open("sport_basketball_tournaments_israel.txt", "r",
                                               encoding="utf8").read().splitlines()

    sport_football_teams_international = open("sport_football_teams_international.txt", "r",
                                              encoding="utf8").read().splitlines()
    sport_football_teams_israel = open("sport_football_teams_israel.txt", "r", encoding="utf8").read().splitlines()

    sport_football_tournaments_international = open("sport_football_tournaments_international.txt", "r",
                                                    encoding="utf8").read().splitlines()
    sport_football_tournaments_israel = open("sport_football_tournaments_israel.txt", "r",
                                             encoding="utf8").read().splitlines()

    actions = [
        'מוכר',
        'קונה',
        'מחפש לקנות',
        'למכירה',
        'מחפש למכור'
    ]

    when = [
        'למחר',
        'להיום',
        'ליום ראשון',
        'ליום שני',
        'ליום שלישי',
        'ליום רביעי',
        'ליום חמישי',
        'ליום שישי',
        'ליום שבת',
        'לשבוע הבא',
        'לחודש הבא',
    ]

    prices = [
        'שח',
        'ש"ח',
        'שקל',
        'שקלים',
        'דולר',
        'יורו'
    ]

    # # # PLACES # # #

    singers_and_standups_places = list(itertools.chain(places_cities_israel, places_shows_stadiums_israel))

    sport_basketball_israel_places = places_basketball_stadiums_israel
    sport_football_israel_places = places_football_stadiums_israel
    sport_football_international_places = places_football_stadiums_international

    # # # ENTITIES # # #

    singers_israel_entities = list(itertools.chain(singers_single_israel, singers_band_israel))
    singers_international_entities = singers_single_international

    standup_israel_entities = list(itertools.chain(shows_standup_single_israel, shows_standup_band_israel))

    basketball_israel_entities = sport_basketball_teams_israel
    basketball_international_entities = sport_basketball_teams_international

    football_israel_entities = sport_football_teams_israel
    football_international_entities = sport_football_teams_international

    # # # TOURNAMENTS AND FESTIVALS # # #

    singers_festivals_israel_tourandfest = festivals_israel
    singers_festivals_international_tourandfest = festivals_international

    basketball_tournaments_tourandfest = list(itertools.chain(sport_basketball_tournaments_israel,
                                                              sport_basketball_tournaments_international))
    football_tournaments_tourandfest = list(itertools.chain(sport_basketball_tournaments_israel,
                                                            sport_basketball_tournaments_international))


    def mock_generator(places, entities, what, for_what, of, inn, is_more_than_one=False, is_vs=False):
        dates = when[::]
        for x in range(5):
            dates.append('ב ' + random_date("1/1/2020", "1/5/2020", random.random()))

        action = rand(actions)
        date = rand(dates)

        place = rand(places)

        entity = rand(entities)
        entity2 = rand(entities)

        price_prefix = 'במחיר של'
        price = str(random.randrange(20, 1500, 10))
        price_suffix = rand(prices)

        to_print = action + " " + \
                   what + " " + \
                   for_what + " " + \
                   of + " " + \
                   entity + " "

        if is_vs:
            to_print += "נגד " + entity2 + " "
        elif is_more_than_one:
            to_print += "ו" + entity2 + " "

        to_print += date + " " + \
                    inn + \
                    place + " " + \
                    price_prefix + " " + \
                    price + " " + \
                    price_suffix

        return to_print


    def write_to_file(lst, name):
        file = open("ready/" + name + "_file.txt", "w+", encoding="utf8")
        for line in lst:
            file.write(line + "\n")


    def create_posts(lst, entities, places, for_what, is_more_than_one=False, is_vs=False):
        for i in range(LIST_SIZE):
            lst.append(mock_generator(places, entities, 'כרטיס', for_what, 'של', 'ב', is_more_than_one, is_vs))


    lstt = singers_and_standups_solo_list = []
    places = singers_and_standups_places
    entities = rand(list(itertools.chain(
        singers_israel_entities,
        standup_israel_entities
    )))
    create_posts(lstt, entities, places, 'להופעה')

    lstt = singers_and_standups_together_list = []
    places = singers_and_standups_places
    entities = rand(list(itertools.chain(
        singers_israel_entities,
        standup_israel_entities
    )))
    create_posts(lstt, entities, places, 'להופעה', True)

    lstt = singers_international_solo_list = []
    places = singers_and_standups_places
    entities = list(itertools.chain(
        singers_international_entities
    ))
    create_posts(lstt, entities, places, 'להופעה')

    lstt = singers_international_together_list = []
    places = singers_and_standups_places
    entities = list(itertools.chain(
        singers_international_entities
    ))
    create_posts(lstt, entities, places, 'להופעה', True)

    lstt = football_matches_israel_list = []
    places = sport_football_israel_places
    entities = list(itertools.chain(
        football_israel_entities
    ))
    create_posts(lstt, entities, places, 'למשחק', True, True)

    lstt = football_matches_international_list = []
    places = sport_football_international_places
    entities = list(itertools.chain(
        football_international_entities
    ))
    create_posts(lstt, entities, places, 'למשחק', True, True)

    lstt = basketball_matches_israel_list = []
    places = sport_basketball_israel_places
    entities = list(itertools.chain(
        basketball_israel_entities
    ))
    create_posts(lstt, entities, places, 'למשחק', True, True)

    write_to_file(singers_and_standups_solo_list, 'singers_and_standups_solo_list')
    write_to_file(singers_and_standups_together_list, 'singers_and_standups_together_list')
    write_to_file(singers_international_solo_list, 'singers_international_solo_list')
    write_to_file(singers_international_together_list, 'singers_international_together_list')
    write_to_file(football_matches_israel_list, 'football_matches_israel_list')
    write_to_file(football_matches_international_list, 'football_matches_international_list')
    write_to_file(basketball_matches_israel_list, 'basketball_matches_israel_list')
