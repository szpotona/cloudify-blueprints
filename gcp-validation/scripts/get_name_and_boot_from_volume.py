from cloudify import ctx
from cloudify_gcp import constants

ctx.source.instance.runtime_properties['name'] = \
    ctx.target.instance.runtime_properties['name']
ctx.source.instance.runtime_properties['script'] = \
    ctx.target.instance.runtime_properties['script']
ctx.source.instance.runtime_properties['cluster'] = \
    ctx.target.instance.runtime_properties.get('cluster') \
    or ctx.source.node.properties.get('cluster_name', '')
ctx.source.instance.runtime_properties['fqdn'] = \
    ctx.target.instance.runtime_properties['fqdn']
disk_body = ctx.target.instance.runtime_properties[constants.DISK]
disk_body['boot'] = True
ctx.source.instance.runtime_properties[constants.DISK] = disk_body
ctx.logger.info('Compute runtime_properties: {0}'.format(str(
    ctx.source.instance.runtime_properties)))
