"""
created by Tobias Leong
v1.0.1

Scrape any HWZ thread!
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup as soup 
import pandas as pd 
import argparse
from textblob import TextBlob
import os

# set up CLI tools
def setupCLI():
	parser = argparse.ArgumentParser(description='Scrape a HWZ post and returns a CSV file.\nBy: Tobias Leong')
	parser.add_argument('URL', metavar='URL', type=str, help='Specify the URL of the post here')
	parser.add_argument('--output', metavar='Output Directory', help='Specify the path of the output directory here')
	args = parser.parse_args()
	return parser, args
	
# welcome msg
print('Starting HWZ scrapper...')

# url is a post on "any netflix shows to recommend" in HWZ EDMW
my_url = args.URL

# open connection
client = urlopen(my_url)
page_html = client.read()
client.close()

# parse html using soup
page_soup = soup(page_html, "html.parser")

# get no. of pages
y = page_soup.find("div", {"class":"pagination"})
if y is None:
	# this means that it is single page !
	total_pages = 1
else:
	total_pages = int(y.span.text.split(" ")[-1])

# loop for page
pg = 1
count = 0

# initialise lists
username_list = []
content_list = []
sentiment_polarity_list = []
sentiment_subj_list = []
datetime_list = []

while pg <= total_pages:
	print("Scrapping page: ", pg, "....")
	url_loop = my_url.split(".html")[0] + '-' + str(pg) + ".html"
	pg += 1

	# open connection
	client = urlopen(url_loop)
	page_html = client.read()
	client.close()

	# parse html using soup
	page_soup = soup(page_html, "html.parser")

	# get posts
	# all posts in HWZ are under this div class
	posts = page_soup.findAll("div", {"class": "post-wrapper"})

	for post in posts:
		count += 1
		username = post.find("a", {"class":"bigusername"}).text
		post_content = post.find("div",{"class":"post_message"}).text
		datetime_post = post.find("td", {"class":"thead"}).text.strip()

		# get sentiment polarity and subj
		sentiment_polarity, sentiment_subj = TextBlob(post_content).sentiment

		# append into lists
		username_list.append(username)
		content_list.append(post_content)
		sentiment_polarity_list.append(sentiment_polarity)
		sentiment_subj_list.append(sentiment_subj)
		datetime_list.append(datetime_post)

		print("Scrapped %s post. Post: %d" % (username, count))

# create dataframe
df = pd.DataFrame({
	'datetime':datetime_list,
	'username':username_list,
	'content':content_list,
	'polarity': sentiment_polarity_list,
	'subjectivity': sentiment_subj_list})

print("Scrapping complete!")

if args.output:
	if os.path.isfile(os.path.join(os.getcwd(),args.output,'hwzdata.csv')):
		os.remove(os.path.join(os.getcwd(),args.output,'hwzdata.csv'))
		print("hwzdata.csv file found at output directory location...\ndeleting...")
	print("Creating csv...")
	df.to_csv(os.path.join(os.getcwd(),args.output,'hwzdata.csv'))
else:
	if os.path.isfile('hwzdata.csv'):
		print("hwzdata.csv file found at output directory location...\ndeleting...")
		os.remove('hwzdata.csv')
	print("Creating csv...")
	df.to_csv('hwzdata.csv')