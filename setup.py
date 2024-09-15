import json
def main():
    try:
       i=input("Enter your Gemini API Key (https://aistudio.google.com/app/apikey): ");writ={"key":i} 
       with open("data.json","w") as f:f.write(json.dumps(writ));input("[Success]: Press any key to close")
    except Exception as e:input(f"[Error]: {e}")
if __name__=="__main__":main()