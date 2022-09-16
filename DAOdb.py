import sqlite3


def search_for_query(query_param):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()

        query = f"""
                    SELECT title, country, release_year, listed_in, description
                    FROM netflix
                    WHERE title LIKE ?
                    ORDER BY release_year DESC
                    LIMIT 1

                    """

        cursor.execute(query, ('%' + query_param + '%',))

        result = cursor.fetchall()
        return result


def search_for_release_year(lower, upper):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()

        query = """
                    SELECT title, release_year
                    FROM netflix
                    WHERE release_year BETWEEN ? AND ?
                    LIMIT 100
                    """
        cursor.execute(query, (lower, upper))

        result = cursor.fetchall()
        return result


def search_for_rating_g():
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()

        query = """
                    SELECT title, rating, description
                    FROM netflix
                    WHERE rating LIKE 'G'
                    LIMIT 100"""

        cursor.execute(query)

        result = cursor.fetchall()

        return result


def search_for_rating_family():
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()

        query = """
                    SELECT title, rating, description
                    FROM netflix
                    WHERE rating IN ('G', 'PG', 'PG-13')
                    LIMIT 100"""

        cursor.execute(query)

        result = cursor.fetchall()

        return result


def search_for_rating_adult():
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()

        query = """
                    SELECT title, rating, description
                    FROM netflix
                    WHERE rating IN ('R', 'NC-17')
                    LIMIT 100"""

        cursor.execute(query)

        result = cursor.fetchall()

        return result
