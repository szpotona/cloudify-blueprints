from cloudify import ctx
from cloudify.state import ctx_parameters as inputs

BOOT_VOLUME = 'boot_volume'

volume_id = ctx.target.instance.runtime_properties[BOOT_VOLUME]
ctx.source.instance.runtime_properties['fqdn'] = ctx.target.instance.runtime_properties['fqdn']
ctx.source.instance.runtime_properties[BOOT_VOLUME] = volume_id
ctx.source.instance.runtime_properties['cluster'] = \
    ctx.target.instance.runtime_properties.get('cluster') \
    or ctx.source.node.properties.get('cluster_name', '')
name = ctx.target.instance.runtime_properties['name']
ctx.source.instance.runtime_properties['name'] = name
server = ctx.source.instance.runtime_properties.get('server', {})
server.update(
    {'name': ctx.target.instance.runtime_properties['fqdn'],
     'block_device_mapping': {'vda': '{}:::0'.format(volume_id)},
     'userdata': {'type': 'http', 'url': 'http://{0}:{1}/{2}'.format(inputs['file_server_ip'],
                                                                     inputs['file_server_port'],
                                                                     name)}})
ctx.source.instance.runtime_properties['server'] = server
ctx.logger.info('Runtime properties: {}'.format(str(ctx.source.instance.runtime_properties)))
