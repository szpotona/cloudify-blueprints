from cloudify import ctx

ctx.logger.info("Establish source: {0} target: {1}".format(ctx.source.instance.id, ctx.target.instance.id))