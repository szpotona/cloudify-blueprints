from cloudify import ctx

BOOT_VOLUME = 'boot_volume'

volume_id = ctx.target.instance.runtime_properties['external_id']
ctx.source.instance.runtime_properties[BOOT_VOLUME] = volume_id

ctx.source.instance.runtime_properties['cluster'] = \
    ctx.target.instance.runtime_properties.get('cluster', '')

ctx.source.instance.runtime_properties['name'] = \
    ctx.target.instance.runtime_properties.get('name', '')

ctx.source.instance.runtime_properties['fqdn'] = \
    ctx.target.instance.runtime_properties.get('fqdn', '')

ctx.logger.info('Runtime properties: {}'.format(str(ctx.source.instance.runtime_properties)))
