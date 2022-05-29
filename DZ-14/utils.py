import sqlite3
from collections import Counter


class DbConnect:
    def __init__(self, path):
        self.con = sqlite3.connect(path)
        self.cur = self.con.cursor()

    def __del__(self):
        self.cur.close()
        self.con.close()


def get_search_by_title(title):
    """ Поиск по вхождению в названии фильма"""
    db_connect = DbConnect('netflix.db')
    db_connect.cur.execute(f"""
        SELECT title, country, release_year, listed_in, description
        FROM netflix
        WHERE title LIKE '%{title}%'
        ORDER BY release_year DESC
        LIMIT 1
        """)
    data = db_connect.cur.fetchone()
    return {
        "title": data[0],
        "country": data[1],
        "release_year": data[2],
        "genre": data[3],
        "description": data[4]
    }


def search_by_year(s1, s2):
    """ Поиск по временному периоду"""
    db_connect = DbConnect('netflix.db')
    db_connect.cur.execute(f"""
            SELECT title, release_year
            FROM netflix
            WHERE release_year BETWEEN {s1} AND {s2}
            ORDER BY release_year DESC
            LIMIT 100
            """)
    data = db_connect.cur.fetchall()
    data_list = []
    for title in data:
        data_list.append({"title": title[0],
                          "release_year": title[1]})
    return data_list


def search_by_rating(rating):
    """ Поиск по рейтингу"""
    db_connect = DbConnect('netflix.db')
    rating_param = {
        "children": "'G'",
        "family": "'G', 'PG', 'PG-13'",
        "adult": "'R', 'NC-17'"
    }
    if rating not in rating_param:
        return "Такой группы нет"
    db_connect.cur.execute(f"""
                SELECT title, rating, description
                FROM netflix
                WHERE rating in ({rating_param[rating]})
                """)
    data = db_connect.cur.fetchall()
    data_list = []
    for title in data:
        data_list.append({"title": title[0],
                          "rating": title[1],
                          "description": title[2]})
    return data_list


def search_by_genry(genry):
    """ Поиск по жанру 10 свежих фильмов"""
    db_connect = DbConnect('netflix.db')
    db_connect.cur.execute(f"""
                SELECT title, description
                FROM netflix
                WHERE listed_in LIKE '%{genry}%'
                ORDER BY release_year DESC
                LIMIT 10
                """)
    data = db_connect.cur.fetchall()
    data_list = []
    for title in data:
        data_list.append({"title": title[0],
                          "description": title[1]})
    return data_list


def search_by_partners(act1, act2):
    """ Поиск партнеров, сыгравших с введенными более 2 раз"""
    db_connect = DbConnect('netflix.db')
    db_connect.cur.execute(f"""
                SELECT `cast`
                FROM netflix
                WHERE `cast` LIKE '%{act1}%' AND `cast` LIKE '%{act2}%'
                """)
    data = db_connect.cur.fetchall()
    act_list = []
    for cast in data:
        act_list.extend(cast[0].split(', '))
    counters = Counter(act_list)
    rezult_list = []
    for act, count in counters.items():
        if act not in [act1, act2] and count > 2:
            rezult_list.append(act)
    return rezult_list


def search_movie_by_param(type_m, release_year, genry):
    """ Поиск фильмов по параметрам и получение списка названия картин в JSON"""
    db_connect = DbConnect('netflix.db')
    db_connect.cur.execute(f"""
                SELECT title, description
                FROM netflix
                WHERE type = '{type_m}' 
                AND release_year = {release_year}
                AND listed_in LIKE '%{genry}%'
                """)
    data = db_connect.cur.fetchall()
    data_list = []
    for title in data:
        data_list.append({"title": title[0],
                          "description": title[1]})
    return data_list
