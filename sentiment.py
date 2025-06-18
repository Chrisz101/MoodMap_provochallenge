import openai

openai.api_key = "Your open-API key"

def analyze_emotion(text):
    prompt = f"What is the primary emotional tone of the following post? Return one word only: Joy, Sadness, Anger, Anxiety, Hope, or Neutral.\nPost: \"{text}\""
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"
