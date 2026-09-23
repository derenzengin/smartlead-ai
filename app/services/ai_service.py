import requests
from config import Config


class AIServiceError(Exception):
    """Yapay zeka servisi hatalari icin ozel hata sinifi."""
    pass


class AIService:
    def __init__(self):
        self.api_key = Config.GROQ_API_KEY
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"

    def _sistem_talimati(self):
        return Config.BUSINESS_CONTEXT

    def yanit_uret(self, mesaj, gecmis=None):
        if not self.api_key:
            return "Demo modu: Yapay zeka API anahtari bulunamadi."

        if gecmis is None:
            gecmis = []

        messages = [
            {
                "role": "system",
                "content": self._sistem_talimati()
            }
        ]

        messages.extend(gecmis)

        messages.append(
            {
                "role": "user",
                "content": mesaj
            }
        )

        try:
            response = requests.post(
                self.api_url,
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "openai/gpt-oss-120b",
                    "messages": messages
                },
                timeout=30
            )

            response.raise_for_status()
            data = response.json()

            return data["choices"][0]["message"]["content"]

        except requests.RequestException as error:
            raise AIServiceError(
                "Yapay zeka servisine baglanirken hata olustu."
            ) from error


ai_service = AIService()