import requests
import json
import nltk
from nltk.corpus import stopwords
# nltk.download('stopwords') uncomment this for first run to download stop words

MAX_TOKENS = 8192
AWAN_API = "ENTER AWAN LLM API KEY HERE"
def remove_stopwords(text):
    # Tokenize the text into words 
    words = nltk.word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.lower() not in stop_words]
    filtered_text = ' '.join(filtered_words)
    return filtered_text

url = "https://api.awanllm.com/v1/completions"

headers = {
  'Content-Type': 'application/json',
  'Authorization': f"Bearer {AWAN_API}"
}

def process_long_text(text):
    chunks = [text[i:i+MAX_TOKENS] for i in range(0, len(text), MAX_TOKENS)]
    # creating chuknks due to token limits and for preserving context 
    processed_chunks = [remove_stopwords(chunk) for chunk in chunks]
    summaries=[]
    for text in processed_chunks:
      payload = json.dumps({
      "model": "Meta-Llama-3-8B-Instruct",
      "prompt": f"""Assume you are a great financial analyst 
              Provide a brief summary of the risk factors section in the company's 10-K filing for the specified fiscal year which delimited by triple backticks.
              Return your response which covers the key risk factors of company as well as the Potential Impact on Business Operations.Only summarize do not generate code.Use points, limit to 200 words.  
            ```{text}```
              SUMMARY:
            """
      })
      response = requests.request("POST", url, headers=headers, data=payload)
      #print(response.json()["choices"][0]["text"])
      summaries.append(response.json()["choices"][0]["text"])
      #print(chunk)
    return ''.join(summaries)

def process_summary(text):
      summaries=[]
      payload = json.dumps({
      "model": "Meta-Llama-3-8B-Instruct",
      "prompt": f"""You are a great financial analyst 
              Provide a brief summary of the risk factors section in the company's 10-K filing for the specified fiscal year which delimited by triple backticks.
              Return your response which covers the key risk factors of company as well as the Potential Impact on Business Operations.Only summarizea and provide it in points. THERE SHOULD BE NO CODE.Use points, limit to 200 words.  
            ```{text}```
              SUMMARY:
            """
      })
      response = requests.request("POST", url, headers=headers, data=payload)
      #print(response.json()["choices"][0]["text"])
      summaries.append(response.json()["choices"][0]["text"])
      #print(chunk)
      return ''.join(summaries)

def get_summary(text):
  text = "".join(text.split())
  summary=process_long_text(text)
  summary=process_summary(summary)
  return summary;

