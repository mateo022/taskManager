import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # Carga variables de entorno

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def create_simple_task(task):
    if not client.api_key:
        return "Error: OpenAI API key is not set. Please check your .env file."

    try:
        prompt = f"""Break down the following complex task into a list of 3 to 5 simple, actionable subtasks.
Task: {task}

Formatting:
- Subtask 1
- Subtask 2
- Subtask 3
etc.
Return only the list of subtasks, one per line, each starting with a hyphen.
"""

        params = {
            "model": "gpt-4o-mini",  # modelo actualizado
            "messages": [
                {
                    "role": "system",
                    "content": "You are an assistant that breaks down complex tasks into simple subtasks."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "max_tokens": 150
        }

        response = client.chat.completions.create(**params)
        content = response.choices[0].message.content.strip()

        subtasks = []

        for line in content.split("\n"):
            line = line.strip()
            if line.startswith("-"):
                subtask = line[1:].strip()
                if subtask:
                    subtasks.append(subtask)

        return subtasks if subtasks else f"Error: No subtasks generated. Response content: {content}"

    except Exception as e:
        return f"Error: Not connected to OpenAI API. Details: {str(e)}"