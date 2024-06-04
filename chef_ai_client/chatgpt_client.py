import openai

# openai.base_url = "https://api.zhizengzeng.com"
# openai.api_key="sk-zk208e97e138e62eb26595c6b426f37c814665f71483ee15"


__client = openai.OpenAI(
    base_url="https://api.zhizengzeng.com/v1/",
    api_key="sk-zk208e97e138e62eb26595c6b426f37c814665f71483ee15",
)


def send_request(content:str):
    if content is None or content == "":
        return
    stream = __client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": content}],
    stream=False,
)

    for chunk in stream:
        print(chunk)


