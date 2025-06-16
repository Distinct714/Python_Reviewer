import logging

# It's the best practice to not use root logger and create your own logger in your modules
logger = logging.getLogger(__name__)
logger.info("Just notify for no reason.")