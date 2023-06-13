import openai

class Npc:
    def __init__(self) -> None:
        openai.api_key = ""

    def changeText(self, text):
        todo = f"""Change the following input  that the meaning ramains the same but the content is different
                        """
        completion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [
                {"role": "user", "content": todo + text}
            ]
        )
        return completion['choices'][0]['message']['content']