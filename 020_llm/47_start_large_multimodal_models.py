# source: https://console.groq.com/docs/vision

#%% packages
from groq import Groq
import base64
import os

#%% Function to encode the image / model invocation
def encode_image(image_path):
    """
    This function reads an image file and encodes it in base64 format, 
    which is suitable for sending to the Groq API. The encoded string 
    can then be included in the request payload when invoking the model.
    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

# image_path = "rag_workflow.png"
image_path = "../images/G.jpg"  # Path to your image
user_question = "How many documents are shown in this image?"
base64_image = encode_image(image_path)
# %%
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables.")

client = Groq(api_key=api_key)
try:
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": user_question},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{base64_image}"
                        },
                    },
                ],
            },
        ],
        model="meta-llama/llama-4-scout-17b-16e-instruct",
    )

except Exception as e:
    print(f"An error occurred: {e}")

# %%
print("Model Output:\n")
print(chat_completion.choices[0].message.content)
# %%
