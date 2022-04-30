import psycopg2
from modules.work_with_files import File


class Database:
    db_config_loc = "database.ini"

    @classmethod
    def querying_db_data(cls, query):
        connection = None
        query_data = []
        try:
            connection = psycopg2.connect(File.postgresql_config_parser(cls.db_config_loc))
            cursor = connection.cursor()
            cursor.execute(query)
            query_data = cursor.fetchall()
            return query_data
        finally:
            if connection is not None:
                connection.close()

    @classmethod
    def insert_to_db(cls, query):
        connection = None
        try:
            connection = psycopg2.connect(File.postgresql_config_parser(cls.db_config_loc))
            connection.autocommit = True
            cursor = connection.cursor()
            cursor.execute(query)
        finally:
            if connection is not None:
                connection.close()

    @classmethod
    def is_name_original(cls, name):
        name_query = f"SELECT userpassword FROM users WHERE username = '{name}';"
        if len(cls.querying_db_data(name_query)) == 0:
            return True
        return False

    @classmethod
    def update_user_score(cls, user_name, win_points):
        query_for_update = f"""UPDATE leader_board
                               SET userscore = userscore + {win_points}
                               WHERE username = '{user_name}';"""
        cls.insert_to_db(query_for_update)
