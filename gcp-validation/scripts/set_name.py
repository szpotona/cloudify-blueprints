#!/usr/bin/python
import sqlite3

from cloudify import ctx

ctx.logger.info("Connecting to db: %s" % ctx.node.properties['db_name'])
conn = sqlite3.connect(ctx.node.properties['db_name'])
ctx.logger.info("Opened database successfully")
node_type = ctx.node.id.split('_')[0]

conn.isolation_level = None
assigned_name = ''
try:
    c = conn.cursor()
    c.execute('SELECT * FROM IDS WHERE NODE_TYPE=?', (node_type,))
    assigned_nodes = c.fetchall()
    assigned_name = node_type + str(len(assigned_nodes) + 1)
    c.execute('INSERT INTO IDS(NODE_TYPE,NAME,VOLUME_ID) VALUES (?, ?, ?)',
              (node_type, assigned_name, ctx.instance.id))
    conn.commit()
    fqdn = assigned_name + ctx.node.properties['domain']
    ctx.instance.runtime_properties['fqdn'] = fqdn
    ctx.instance.runtime_properties['name'] = fqdn
    ctx.logger.info('Assigned name {0} for the VM'.format(assigned_name))
except conn.Error as e:
    ctx.logger.info('Assigning id failed. Rolling back. Error: %s' % e.message)
    c.execute("rollback")
finally:
    conn.close()

userdata = '''
#!/bin/bash
touch /home/centos/userdata_finished'''

if assigned_name:
    with open('/tmp/{}'.format(assigned_name), 'w') as f:
        f.write(userdata)

ctx.instance.runtime_properties['script'] = userdata