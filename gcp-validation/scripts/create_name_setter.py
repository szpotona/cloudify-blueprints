#!/usr/bin/python
import sqlite3
from cloudify import ctx
from cloudify.state import ctx_parameters as inputs

db = inputs['database_name']
conn = sqlite3.connect(db)
conn.execute('''CREATE TABLE IDS
       (VOLUME_ID      TEXT     PRIMARY_KEY,
        NODE_TYPE      TEXT    NOT NULL,
        NAME           TEXT    NOT NULL UNIQUE);''')
ctx.logger.info('Table IDS in database for id naming created in %s' % db)
conn.close()