import openai
import server_settings


class OpenAIClient:
    def __init__(self, base_url: str, api_key: str, model: str) -> None:
        self.__base_url = base_url
        self.__api_key = api_key
        self.__model = model
        self.__clent = openai.OpenAI(
            base_url=self.__base_url,
            api_key=self.__api_key,
        )
        pass

    def send_request(self, content: str, stream: bool):
        if content is None or content == "":
            return

        try:
            stream = self.__clent.chat.completions.create(
                model=self.__model,
                messages=[{"role": "user", "content": content}],
                stream=stream,
            )

            if stream:
                 for chunk in stream:
                    yield chunk

            else:
                return stream
        except Exception as e:
            # TODO: need to log
            print(e)


openai_client = OpenAIClient(
    base_url=server_settings.OPEN_AI_BASIC_URL,
    api_key=server_settings.OPEN_AI_API_KEY,
    model=server_settings.OPEN_AI_MODEL,
)
