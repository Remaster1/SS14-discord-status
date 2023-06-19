import logging
import requests


class StatusWebhook:
    _webhook_url: str = ""
    _server_url: str = ""
    _message_id: int = None

    def __init__(self, webhook_url: str, server_url: str, message_id: int = None) -> None:
        self._webhook_url = webhook_url
        self._server_url = server_url
        self._message_id = message_id

    def fetch(self) -> dict:
        try:
            logging.info("Fetching status from server has successfully")
            return requests.get(self._server_url).json()
        except requests.exceptions.ConnectionError:
            logging.error("Error connecting to server to get status")
            return None

    def send(self, data: dict) -> None:
        if not data == None:
            if not self._message_id == None:
                send = requests.patch(f"{self._webhook_url}/messages/{self._message_id}", json=self.generate_embed(
                    data["name"], data["players"], data["soft_max_players"]), headers={"Content-Type": "application/json"})
            else:
                send = requests.post(self._webhook_url+"?wait=true", json=self.generate_embed(
                    data["name"], data["players"], data["soft_max_players"]), headers={"Content-Type": "application/json"})

            if send.status_code == 400:
                logging.error("Discord api send bad request")
            elif send.status_code == 200:
                self._message_id = send.json()["id"]
                logging.info("Send message has successfully")

    def generate_embed(self, name: str, players: str, max_players: str) -> str:
        embed = {
            "embeds": [
                {
                    "title": "Статус сервера:",
                    "description": "",
                    "color": 59647,
                    "fields": [
                        {
                            "name": "Название сервера:",
                            "value": name

                        },
                        {
                            "name": "Количество игроков:",
                            "value": f"{players}/{max_players}"
                        }
                    ]
                }
            ],
        }
        return embed
