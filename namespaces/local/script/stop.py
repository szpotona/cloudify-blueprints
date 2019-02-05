from cloudify import ctx

ctx.logger.info("Stop {0}".format(ctx.instance.id))
