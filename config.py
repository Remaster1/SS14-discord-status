import dotenv

env = dotenv.dotenv_values(".env")
discord_webhook = env["DISCORD_WEBHOOK"]
server_url = env["SERVER_URL"]
update_duration_min = 2
# insert here custom message id which message will change (insert None for create new message)
custom_message_id = None
