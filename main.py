import os, sys
from dotenv import load_dotenv
from google import genai

load_dotenv()

if len(sys.argv) != 2:
    print("incorrect number of arguments passed")
    sys.exit(1)
else:
    prompt = sys.argv[1]
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=f"{prompt}")
    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
