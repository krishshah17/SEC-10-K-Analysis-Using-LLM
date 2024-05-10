API_KEY = 'ENTER SEC API KEY HERE'

from sec_api import ExtractorApi, XbrlApi

extractorApi = ExtractorApi(API_KEY)
xbrlApi = XbrlApi(API_KEY)

def url_builder(cik,acn,file):
	return f'https://www.sec.gov/Archives/edgar/data/{cik}/{acn}/{file}'


def extract_info_from_sec_document(sec_document):	
	lines=[]
	with open(sec_document, 'r', encoding='utf-8') as file:
		lines = file.readlines()

	accession_number = None
	cik = None
	file_name = None
	flag =0
	for line in lines:
		line=line.strip()
		if line.startswith("ACCESSION NUMBER:"):
			print(line)
			accession_number = line.split(":")[1].strip().replace("-", "")
		elif line.startswith("CENTRAL INDEX KEY:"):
			print(line)
			cik = line.split(":")[1].strip()
		elif ((not flag) and line.startswith("<FILENAME>")):
			flag=1
			print(line)
			file_name = line.split(">")[1].strip()
	
	return url_builder(cik,accession_number,file_name)



def get_text(file_path):
	url = extract_info_from_sec_document(file_path)
	#item_1_text    = extractorApi.get_section(url, '1', 'text')
	item_1_a_text  = extractorApi.get_section(url, '1A', 'text')
	#item_1_b_text  = extractorApi.get_section(url, '1B', 'text')
	# item_2_text    = extractorApi.get_section(url, '2', 'text')
	# item_3_text    = extractorApi.get_section(url, '3', 'text')
	# item_4_text    = extractorApi.get_section(url, '4', 'text')
	# item_5_text    = extractorApi.get_section(url, '5', 'text')
	# item_6_text    = extractorApi.get_section(url, '6', 'text')
	# item_7_text    = extractorApi.get_section(url, '7', 'text')
	# item_7_a_text  = extractorApi.get_section(url, '7A', 'text')
	# item_8_text    = extractorApi.get_section(url, '8', 'text')
	# item_9_text    = extractorApi.get_section(url, '9', 'text')
	# item_9_a_text  = extractorApi.get_section(url, '9A', 'text')
	# item_9_b_text  = extractorApi.get_section(url, '9B', 'text')
	# item_10_text   = extractorApi.get_section(url, '10', 'text')
	# item_11_text   = extractorApi.get_section(url, '11', 'text')
	# item_12_text   = extractorApi.get_section(url, '12', 'text')
	# item_13_text   = extractorApi.get_section(url, '13', 'text')
	# item_14_text   = extractorApi.get_section(url, '14', 'text')
	# item_15_text   = extractorApi.get_section(url, '15', 'text')
	# all above comment's are to get different sections of the 10-K filing
	return item_1_a_text; 


# url = extract_info_from_sec_document()
# get_text("/PATH/TO/sec-edgar-filings/AAPL/10-K/0000320193-23-000106/full-submission.txt")
