from cloudify import ctx

ctx.source.instance.runtime_properties['cluster'] = \
    ctx.source.node.properties.get('cluster_name', '') \
    or ctx.target.instance.runtime_properties.get('cluster', '')
ctx.logger.info('Cluster name: {0} Name: {1}'.format(
                    ctx.source.instance.runtime_properties.get('cluster'),
                    ctx.source.instance.runtime_properties.get('name')))
