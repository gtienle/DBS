def data(x):
	#Load Data, delete non-essential columns
	election = pd.read_csv("/Users/christinele/Desktop/SoSe17/DBS/Projekt/american-election-tweets.csv", index_col=0)
	del election['in_reply_to_screen_name']
	del election['is_quote_status']
	del election['source_url']
	del election['truncated']