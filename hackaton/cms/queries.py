from django.db import connection


def select_query(query_str):
    with connection.cursor() as cursor:
        cursor.execute(
            query_str
        )
        rows = cursor.fetchall()
    return rows


def insert(query_str):
    with connection.cursor() as cursor:
        cursor.execute(
            query_str
        )
        returning_id = cursor.fetchall()
    return returning_id


def update(query_str):
    with connection.cursor() as cursor:
        cursor.execute(
            query_str
        )
        returning_id = cursor.fetchall()
    return returning_id


def delete(query_str):
    with connection.cursor() as cursor:
        cursor.execute(
            query_str
        )
