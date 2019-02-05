from cloudify import ctx

ctx.logger.info("Hi there")
ctx.logger.info(str(ctx.node.properties['some_property']))
ctx.logger.info(str(ctx.get_resource_and_render(ctx.node.properties['template'], {'test_value': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'})))
