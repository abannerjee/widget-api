import psycopg2
import logging

def connect(config):
    constr = "dbname='{}' user='{}' host='{}' port='{}'".format(
        config['db'],
        config['user'],
        config['host'],
        config['db_port']
    )
    logging.info('Connected to DB {}'.format(config['db']))
    return psycopg2.connect(constr)