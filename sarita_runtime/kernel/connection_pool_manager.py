import os
import psycopg2
from psycopg2 import pool
import logging

class ConnectionPoolManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConnectionPoolManager, cls).__new__(cls)
            cls._instance.initialize_pools()
        return cls._instance

    def initialize_pools(self):
        db_url = os.getenv("DATABASE_URL")
        if db_url:
            self.pg_pool = psycopg2.pool.SimpleConnectionPool(1, 20, dsn=db_url)
            logging.info("PostgreSQL Connection Pool initialized.")

    def get_connection(self):
        return self.pg_pool.getconn()

    def release_connection(self, conn):
        self.pg_pool.putconn(conn)

if __name__ == "__main__":
    cpm = ConnectionPoolManager()
    # conn = cpm.get_connection()
    # cpm.release_connection(conn)
