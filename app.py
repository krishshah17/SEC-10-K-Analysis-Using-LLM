import streamlit as st
from pathlib import Path
from time import sleep
import subprocess
import sys
from sec_edgar_downloader import Downloader
import os
import requests
import json
from transformers import pipeline
from secapiworking import *
from awan import * 

def display_summary_as_bullet_points(summary):
    points = summary.replace("`", "").split('* ')
    points = [point.strip() for point in points if point.strip()]
    for point in points:
        st.markdown(f"- {point}")

dl = Downloader("USERNAME", "username@gmail.com")
headers={"User-Agent":"username@gmail.com"}
st.set_page_config(page_title="LLM based 10-K Inference",layout="wide",initial_sidebar_state="collapsed")
st.header("LLM based 10-K Inference",divider='red')

## company tickers can be found by a get request to SEC's official website at: https://www.sec.gov/files/company_tickers.json
with open("/PATH/TO/company_tickers.json", 'r') as file:
	companyTickers = json.load(file)

companyTickers = [ companyTickers[i]["ticker"] for i in companyTickers]

col1, col2 = st.columns(2)
with col1:
	with st.form("Ticker Form"):
		title = st.selectbox(label="Ticker", options=companyTickers, index=None)
		number = st.number_input("Number of Years of Filings", min_value=1, max_value=25, step=1)	
		submitted = st.form_submit_button("Submit")
		if submitted:
			if(title not in os.listdir("/PATH/TO/sec-edgar-filings")):
				st.write("Downloading 10-K Filings for", title)
				#st.write(os.listdir())
				dl.get("10-K", title, limit = number, download_details=True)
			else:
				st.write("Files already present locally")
			st.write("Downloaded 10-K Filings for", title)

with col2:
	title = st.selectbox(label="Ticker", options=[i for i in os.listdir("/PATH/TO/sec-edgar-filings") if i != ".DS_Store"], index=None)
	if st.button("Run Inference"):
		text_contents = []
		file_path = os.path.join("/Users/krishshah/Desktop/Projects/FinTech-SEC/sec-edgar-filings",title+"/10-K")
		for root, dirs, files in os.walk(file_path):
			for dir_name in dirs:
				filing_folder_path = os.path.join(root, dir_name)
				for filename in os.listdir(filing_folder_path):
					if filename.endswith('.txt'):
						# Reading the text content of the file
						file_path = os.path.join(filing_folder_path, filename)
						text_contents.append(get_text(file_path))

    
		summary = get_summary("".join(text_contents))
		display_summary_as_bullet_points(summary)
