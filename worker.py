from celery import Celery
from celery.utils.log import get_task_logger
import time

# Create the celery app and get the logger
celery_app = Celery('tasks', broker='amqps://myckiisx:FESPKk_IgaXEy4MIo4JxrfWmKeRtL9vn@hornet.rmq.cloudamqp.com/myckiisx')
logger = get_task_logger(__name__)

# create a task
@celery_app.task
def process(queryString):
    time.sleep(60)

    res = "string processed "+queryString
    logger.info(res)

    return res