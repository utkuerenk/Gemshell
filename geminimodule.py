import google.generativeai as genai;import json
with open("data.json","r") as f:data=json.load(f);genai.configure(api_key=data["key"])
generation_config={"temperature":1,"top_p": 0.95,"top_k":64,"max_output_tokens":8192,"response_mime_type":"text/plain",}
model=genai.GenerativeModel(model_name="gemini-1.5-flash",generation_config=generation_config,);chat_session=model.start_chat(history=[])
def AISend(x):response=chat_session.send_message(x);return response.text