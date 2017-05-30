#import libraries
import csv

def data(x):
	#Load Data, delete non-essential columns
	election_new = pd.read_csv("/Users/christinele/Desktop/SoSe17/DBS/Projekt/american-election-tweets.csv", index_col=0)
	del election_new['in_reply_to_screen_name']
	del election_new['is_quote_status']
	del election_new['source_url']
	del election_new['truncated']
print election_new.shape
election_new.head()

election_new.to_csv('/Users/christinele/Desktop/SoSe17/DBS/Projekt/election_new.csv', index=False)