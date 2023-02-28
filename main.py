from sqlalchemy import create_engine
import config


class DWH_Migration:
    def __init__(self, stg_hostname, stg_username,
                 stg_password, stg_database, prod_hostname,
                 prod_username, prod_password, prod_database):
        self.stg_hostname = stg_hostname
        self.stg_username = stg_username
        self.stg_password = stg_password
        self.stg_database = stg_database
        self.prod_hostname = prod_hostname
        self.prod_username = prod_username
        self.prod_password = prod_password
        self.prod_database = prod_database

    def get_stg_data(self):
        self.stg_database = config.sys_stg[0]
        self.stg_hostname = config.sys_stg[1]
        self.stg_username = config.sys_stg[2]
        self.stg_password = config.sys_stg[3]
        engine = create_engine(f'postgresql://{self.stg_username}:'
                               f'{self.stg_password}@{self.stg_hostname}/'
                               f'{self.stg_database}')

        with engine.connect() as conn:
            query = "select * from table1"
            data = conn.execute(query)
        return data

    def get_prod_data(self):
        self.prod_database = config.sys_prod[0]
        self.prod_hostname = config.sys_prod[1]
        self.prod_username = config.sys_prod[2]
        self.prod_password = config.sys_prod[4]
        engine = create_engine(f'postgresql://{self.prod_database}:'
                               f'{self.prod_password}@{self.prod_hostname}/'
                               f'{self.prod_database}')

        with engine.connect() as conn:
            query = "select * from table2"
            data = conn.execute(query)
        return data
