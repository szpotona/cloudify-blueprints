from cloudify import ctx

ctx.logger.info("Delete {0}".format(ctx.instance.id))
