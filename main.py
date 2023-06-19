import logger
import logging
import config
from webhook import StatusWebhook
import schedule
import time

logger.setup()
logging.info("Start webhook")
st = StatusWebhook(config.discord_webhook, config.server_url, config.custom_message_id)


@schedule.repeat(schedule.every(config.update_duration_min).minutes)
def job():
    st.send(st.fetch())


while True:
    schedule.run_pending()
    time.sleep(1)
