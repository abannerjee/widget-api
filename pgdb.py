import psycopg2
import logging

def connect(options):
    constr = "dbname='{}' user='{}' host='{}' port='{}'".format(
        options['db'],
        options['user'],
        options['host'],
        options['db_port']
    )
    logging.info('Connected to DB {}'.format(options['db']))
    return psycopg2.connect(constr)