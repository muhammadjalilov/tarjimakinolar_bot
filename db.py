import os
import aiopg


class Database:
    def __init__(self):
        self.dsn = (f"dbname={os.getenv('database_name')} "
                    f"user={os.getenv('postgres_user')} "
                    f"password={os.getenv('postgres_password')} "
                    f"host=127.0.0.1")

    async def insert_user(self, user_id):
        insert_user_sql = """
            insert into users (user_id) values (%s);
        """
        async with aiopg.connect(self.dsn) as conn:
            async with conn.cursor() as cursor:
                await cursor.execute(insert_user_sql, (user_id,))

    async def search_id_from_db(self, user_id):
        search_id = """
            select user_id from users where user_id = %s;
        """
        async with aiopg.connect(self.dsn) as conn:
            async with conn.cursor() as cursor:
                await cursor.execute(search_id, (user_id,))
                result = await cursor.fetchone()
                if result:
                    return False
                else:
                    return True
