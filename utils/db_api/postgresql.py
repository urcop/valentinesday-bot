import asyncpg
import self as self
import telegram as telegram
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config


class Database:

    def __init__(self):
        self.pool: Pool = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.IP,
            database=config.db
        )

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False
                      ):
        async with self.pool.acquire() as connect:
            connect: Connection
            async with connect.transaction():
                if fetch:
                    result = await connect.fetch(command, *args)
                elif fetchval:
                    result = await connect.fetchval(command, *args)
                elif fetchrow:
                    result = await connect.fetchrow(command, *args)
                elif execute:
                    result = await connect.execute(command, *args)
            return result

    @staticmethod
    def format_kwargs(sql, params: dict):
        sql += ' AND '.join([
            f'{item} = ${num}' for num, item in enumerate(params.keys(), start=1)
        ])
        return sql, tuple(params.values())

    # создание таблиц
    async def create_table_users(self):
        sql = '''
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                fullname VARCHAR(255) NOT NULL,
                username varchar(255) NULL,
                tg_id BIGINT NOT NULL UNIQUE
            );
        '''
        await self.execute(sql, execute=True)

    # команды api
    async def select_all_users(self):
        sql = '''SELECT * FROM users;'''
        return await self.execute(sql, fetch=True)

    async def select_user(self, **kwargs):
        sql = ''' SELECT * FROM users WHERE '''
        sql, params = self.format_kwargs(sql, params=kwargs)
        return await self.execute(sql, *params, fetchrow=True)

    async def add_user(self, fullname, username, tg_id):
        sql = '''
            INSERT INTO users (fullname, username, tg_id) VALUES ($1, $2, $3) returning *
        '''
        return await self.execute(sql, fullname, username, tg_id, fetchrow=True)

    async def update_user_fullname(self, fullname, tg_id):
        sql = "UPDATE users SET fullname=$1 WHERE tg_id=$2"
        return await self.execute(sql, fullname, tg_id, execute=True)

    async def delete_user(self, tg_id):
        sql = "DELETE FROM users WHERE tg_id=$1"
        return await self.execute(sql, tg_id, execute=True)


if __name__ == '__main__':
    pass
