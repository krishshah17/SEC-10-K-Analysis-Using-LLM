# SEC 10-K Analysis Using LLM
 An LLM based analysis for SEC 10-K filings, submitted as an assignment for recruitment at Georgia Tech FinTech Lab

# Tech Stack Used:
- Python
- Streamlit
- sec-edgar-downloader
- sec-api [https://sec-api.io/]
- Awan LLM [https://www.awanllm.com/]

# Metrics chosen for inference: Risk Factors (1A of 10-K Filing)
## Why?
  - ### Unsystematic risks
    An investor needs to know the unsystematic risks like, management risks, internal flaws involved with a company. It highlights only the company's flaws, whereas a systematic risk would affect the industry. This helps investors asses their investment with the risk associated with the company
  - ### Long term risk analysis
    By making use of historical data we also see how to company's risk taking ability has evolved over time and how this has been impacted the company's leadership changes, if any.
    This also helps us infer the company's risk capacity to profit ratio helping with investment analysis
# How to run this?
### Requirements
```
pip install -r requirements.txt
```
Then edit the path's as required
Replace API Key's
```
API_KEY = 'ENTER SEC API KEY HERE'

AWAN_API = "ENTER AWAN LLM API KEY HERE"

```
and then
```
streamlit run app.py
```
On a browser go to:
```
localhost:8501
```
# Project Demo
https://www.loom.com/share/1cb509e1f65e4cc08acf3c2f5fe3bec5?sid=bd5fcbb9-0b6f-4b3d-a2c4-aaa12fd30a9c

# Screenshots 
<img width="1512" alt="Screenshot 2024-05-10 at 4 10 55 PM" src="https://github.com/krishshah17/SEC-10-K-Analysis-Using-LLM/assets/26605210/9edff1a4-d422-4489-8dba-f0dffe8e8f19">

<img width="1512" alt="Screenshot 2024-05-11 at 12 23 25 AM" src="https://github.com/krishshah17/SEC-10-K-Analysis-Using-LLM/assets/26605210/25516b2b-81b1-4854-9d14-6a14a2220e18">

# In Depth Explaination
[10-k Filing Analysis_.pdf](https://github.com/krishshah17/SEC-10-K-Analysis-Using-LLM/files/15278896/10-k.Filing.Analysis_.pdf)

# Future Work
- Containerize so it can be deployed anywhere
- Parse XBRL data for more effecient data scraping
- Plot graphs as well. 
