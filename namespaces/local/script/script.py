from cloudify import ctx

ctx.logger.info("Hi there")
ctx.logger.info(str(ctx.node.properties['some_property']))
