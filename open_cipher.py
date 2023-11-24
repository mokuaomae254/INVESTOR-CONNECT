import streamlit as st
import pandas as pd 
st.set_page_config(layout="wide")
def market_report():
		import pandas as pd
		import numpy as np
		import streamlit as st

		import base64
		from io import BytesIO
		from matplotlib.backends.backend_pdf import FigureCanvasPdf as FigureCanvas

		#from matplotlib.backends.backend_Agg import FigureCanvasAgg as FigureCanvas
		from matplotlib.figure import Figure

		#st.header("Top 100 Cryptocurrencies By Market Capitalization")
			#dataframe = dataframe.drop(columns=["ATH","% ATH"], axis=1)

		dataframe=pd.read_csv("satoshi 100 index data58.csv")
		#st.dataframe(data)
		dataframe.index.name = "rank"
		#converting column to list
		#dataframe=pd.read_csv("satoshi 100 index data58.csv")
		liquidity_risk=[ ]
		for index in dataframe.index:
				if (dataframe["24H Vol"][index])<(dataframe["Market Cap"][index]*0.05):
					liquidity_risk.append("illiquid")

				elif (dataframe["24H Vol"][index])>(dataframe["Market Cap"][index]*0.05) and (dataframe["24H Vol"][index])<=(dataframe["Market Cap"][index]*0.1):
					liquidity_risk.append("fairly liquid")
				elif (dataframe["24H Vol"][index]) > (dataframe["Market Cap"][index] * 0.1) and (dataframe["24H Vol"][index]) <= (dataframe["Market Cap"][index] * 0.3 ):
					liquidity_risk.append("highly liquid") 
				
				elif (dataframe["24H Vol"][index]) > (dataframe["Market Cap"][index] * 0.3) and (dataframe["24H Vol"][index]) <= (dataframe["Market Cap"][index] * 0.5):
					
					liquidity_risk.append("limited long term potential")
				elif (dataframe["24H Vol"][index]) > (dataframe["Market Cap"][index] * 0.5):
					liquidity_risk.append("stay off/sell off")
				
		dataframe['liquidity_risk'] = liquidity_risk
		dataframe.loc[dataframe['Name'].isin(['Tether USDT','USD Coin USDC','Binance USD BUSD','Dai DAI','Paxos Standard USDP','TrueUSD TUSD','USDD USDD','Neutrino USD USDN','Gemini Dollar GUSD',"cDAI. cdai","cUSDC. cusdc"]), 'liquidity_risk'] = 'stablecoin'
		#st.dataframe(dataframe)


			#streamlit run downloading_report.py
		#dataframe = pd.read_csv("satoshi 100 index data58.csv")
		#dataframe = pd.read_csv("satoshi 100 index data31.csv")
		#st.header("Top 100 Cryptocurrencies")
		st.header("Cryptocurrency Market Daily,Weekly and Monthly Report ")
		#data=pd.read_csv("satoshi 100 index data29.csv")
		#st.dataframe(dataframe)

		#print(df)
		i=0
		st.subheader("Today's Winners ")
		for i in range(10):
			
			data=dataframe.sort_values(by=['24H %'], ascending=False)
		st.dataframe(data)
		df = pd.DataFrame(data)

		if st.button("Download CSV1"):
			csv = df.to_csv(index=False)
			b64 = base64.b64encode(csv.encode()).decode()
			href = f'<a href="data:file/csv;base64,{b64}" download="mydata.csv">Download CSV File</a>'
			st.markdown(href, unsafe_allow_html=True)
		#csv_downloader()
		st.subheader("Today's Biggest Losers ")
		for i in range(10):
			
			data=dataframe.sort_values(by=['24H %'])
		st.dataframe(data)
		df = pd.DataFrame(data)

		if st.button("Download CSV2"):
			csv = df.to_csv(index=False)
			b64 = base64.b64encode(csv.encode()).decode()
			href = f'<a href="data:file/csv;base64,{b64}" download="mydata.csv">Download CSV File</a>'
			st.markdown(href, unsafe_allow_html=True)
		#csv_downloader()
		st.subheader("This week's Winners ")
		for i in range(10):

			data=dataframe.sort_values(by=['7D %'], ascending=False)
		st.dataframe(data)
		df = pd.DataFrame(data)

		if st.button("Download CSV3"):
			csv = df.to_csv(index=False)
			b64 = base64.b64encode(csv.encode()).decode()
			href = f'<a href="data:file/csv;base64,{b64}" download="mydata.csv">Download CSV File</a>'
			st.markdown(href, unsafe_allow_html=True)
		#csv_downloader()
		st.subheader("This week's Biggest lossers ")
		for i in range(10):
			
			data=dataframe.sort_values(by=['7D %'])
		st.dataframe(data)
		df = pd.DataFrame(data)

		if st.button("Download CSV4"):
			csv = df.to_csv(index=False)
			b64 = base64.b64encode(csv.encode()).decode()
			href = f'<a href="data:file/csv;base64,{b64}" download="mydata.csv">Download CSV File</a>'
			st.markdown(href, unsafe_allow_html=True)
		#csv_downloader()
		st.subheader("This Month's Winners ")
		for i in range(10):
			
			data=dataframe.sort_values(by=['30D %'], ascending=False)
		st.dataframe(data)
		df = pd.DataFrame(data)

		if st.button("Download CSV5"):
			csv = df.to_csv(index=False)
			b64 = base64.b64encode(csv.encode()).decode()
			href = f'<a href="data:file/csv;base64,{b64}" download="mydata.csv">Download CSV File</a>'
			st.markdown(href, unsafe_allow_html=True)
		#csv_downloader()
		st.subheader("This Month's Biggest Losers ")
		for i in range(10):
			
			data=dataframe.sort_values(by=['30D %'])
		st.dataframe(data)
		df = pd.DataFrame(data)

		if st.button("Download CSV6"):
			csv = df.to_csv(index=False)
			b64 = base64.b64encode(csv.encode()).decode()
			href = f'<a href="data:file/csv;base64,{b64}" download="mydata.csv">Download CSV File</a>'
			st.markdown(href, unsafe_allow_html=True)
#csv_downloader()
#streamlit run report_lidrisk.py
def macro_analysis():
    
	import streamlit as st
	import matplotlib.pyplot as plt
		#time.sleep(10)
	from PIL import Image
	#image = Image.open('MM4_Investor_sentiment_V3 (1).jpg')
	image2 = Image.open('20200317-the-psychology-of-a-market-cycle.png')
	image3 = Image.open('saupload_manias_bubbles.jpg')
	#st.text("MACRO IS KING")
	#st.image(image, caption='UNITED STATES CPI INFLATION DATA')
	st.image(image2, caption='EMOTIONAL ROLLERCOASTER.1')
	st.image(image3, caption='EMOTIONAL ROLLERCOASTER.2')

	#streamlit run sentiment.py
def media_socials():
	import streamlit as st

	# Set page configuration
	#st.set_page_config(page_title="Social Media Links", page_icon=":earth_americas:")
	st.write("Feel free reachout with the links below")
	SOCIAL_MEDIA = {
		"YouTube": "https://youtube.com",
		"LinkedIn": "https://linkedin.com",
		"GitHub": "https://github.com",
		"Twitter": "https://twitter.com",
	}

	# Add favicons to respective platform
	FAVICON = {
		"YouTube": "https://www.youtube.com/s/desktop/0356b1aa/img/favicon_32.png",
		"LinkedIn": "https://static-exp1.licdn.com/sc/h/7fx9nkd7mx8avdpqm5hqcbi97",
		"GitHub": "https://github.githubassets.com/favicons/favicon-dark.svg",
		"Twitter": "https://abs.twimg.com/favicons/twitter.ico",
	}

	# Display icons and links horizontally
	col1, col2, col3, col4 = st.columns(4)
	for platform, link in SOCIAL_MEDIA.items():
		favicon = FAVICON.get(platform)
		if favicon:
			col = None
			if platform == "YouTube":
				col = col1
			elif platform == "LinkedIn":
				col = col2
			elif platform == "GitHub":
				col = col3
			elif platform == "Twitter":
				col = col4
			with col:
				st.image(favicon, width=30)
				st.write(f"[{platform}]({link})")

	#streamlit run media_social.py
def investor_connect2():
		import streamlit as st
		import matplotlib.pyplot as plt
		from PIL import Image

		st.header("Investor Connect")
		st.text("Share your charts below")
		username = st.text_input("Enter your username")
		caption = st.text_input("What is the chart about")
		uploaded_files = st.file_uploader("Choose one or more files", accept_multiple_files=True)



		if uploaded_files is not None:
			
			for uploaded_file in uploaded_files:
				st.write("Posted by " + username)
				image = Image.open(uploaded_file)
				st.image(image, caption=caption)

		#streamlit run investor_connect2.py
def investor_connect():
    	
	st.header("investor connect")
	st.text("share your charts below")
	uploaded_file = st.file_uploader("Choose a file")
def investor_connect1():
		import streamlit as st
		import matplotlib.pyplot as plt
		from PIL import Image

		st.header("Investor Connect")
		st.text("Share your charts below")
		username = st.text_input("Enter your username")
		uploaded_file = st.file_uploader("Choose a file")
		if uploaded_file is not None:
			image = Image.open(uploaded_file)
			st.image(image, caption="EMOTIONAL ROLLERCOASTER.1")
			st.write("Posted by " + username)


#streamlit run investor_connect.py
	
def crypto_portfolio():
        import streamlit as st
        import matplotlib.pyplot as plt
        age= st.number_input("enter your age:") 
        if age>=18  and age<=200 :
            #st.header("Portfolio Design and Risk Management")
            st.subheader("Crypto portfolio")

            income = st.number_input("Enter your annual income:")
            investment = income * 0.1
            st.text("Invest 10% of your income, or $" + str(investment) + ", in crypto.")

            if income > 100 :
                #st.text("Allocate 30% of your portfolio to layer 1 and the remaining 70% to be equally allocated among layer 0, layer 2 and layer 3.")
                labels = 'LAYER 1', 'LAYER 0', 'LAYER 2', 'LAYER 3','INFRA COINS','AI COINS'
                sizes = [30, 10, 20, 20,10,10]
                mycolors = ["yellow", "hotpink", "purple", "green","pink","maroon"]
                explode = (0, 0, 0, 0,0,0)
                fig1, ax1 = plt.subplots()
                ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors = mycolors)
                ax1.axis('equal')
                st.pyplot(fig1)

            elif income > 100 and income <= 1000:
                #st.text("Allocate 30% of your portfolio to layer 1 and the remaining 70% to be equally allocated among layer 0, layer 2 and layer 3.")
                labels = 'LAYER 1', 'LAYER 0', 'LAYER 2', 'LAYER 3','INFRA COINS','AI COINS'
                sizes = [10, 20, 20, 20,10,20]
                mycolors = ["yellow", "hotpink", "purple", "green","pink","maroon"]
                explode = (0, 0, 0, 0,0,0)
                fig1, ax1 = plt.subplots()
                ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors = mycolors)
                ax1.axis('equal')
                st.pyplot(fig1)

            elif income > 1000 and income <= 10000:
                #st.text("Allocate 30% of your portfolio to layer 1 and the remaining 70% to be equally allocated among layer 0, layer 2 and layer 3.")
                labels = 'LAYER 1', 'LAYER 0', 'LAYER 2', 'LAYER 3','INFRA COINS','AI COINS'
                sizes = [20, 10, 20, 20,20,10]
                mycolors = ["yellow", "hotpink", "purple", "green","pink","maroon"]
                explode = (0, 0, 0, 0,0,0)
                fig1, ax1 = plt.subplots()
                ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors = mycolors)
                ax1.axis('equal')
                st.pyplot(fig1)
            elif income > 10000 and income <= 100000:
                #st.text("Allocate 30% of your portfolio to layer 1 and the remaining 70% to be equally allocated among layer 0, layer 2 and layer 3.")
                labels = 'LAYER 1', 'LAYER 0', 'LAYER 2', 'LAYER 3','INFRA COINS','AI COINS'
                sizes = [30, 10, 20, 20,10,10]
                mycolors = ["yellow", "hotpink", "purple", "green","pink","maroon"]
                explode = (0, 0, 0, 0,0,0)
                fig1, ax1 = plt.subplots()
                ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors = mycolors)
                ax1.axis('equal')
                st.pyplot(fig1)
            elif income > 100000 and income <= 1000000:
                #st.text("Allocate 30% of your portfolio to layer 1 and the remaining 70% to be equally allocated among layer 0, layer 2 and layer 3.")
                labels = 'LAYER 1', 'LAYER 0', 'LAYER 2', 'LAYER 3','INFRA COINS','AI COINS'
                sizes = [40, 10, 20, 10,10,10]
                mycolors = ["yellow", "hotpink", "purple", "green","pink","maroon"]
                explode = (0, 0, 0, 0,0,0)
                
                fig1, ax1 = plt.subplots()
                ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors = mycolors)
                ax1.axis('equal')
                st.pyplot(fig1)
            elif income > 1000000 and income <= 2000000:
                #st.text("Allocate 30% of your portfolio to layer 1 and the remaining 70% to be equally allocated among layer 0, layer 2 and layer 3.")
                labels = 'LAYER 1', 'LAYER 0', 'LAYER 2', 'LAYER 3','INFRA COINS','AI COINS'
                sizes = [50, 10, 10, 10,10,10]
                mycolors = ["yellow", "hotpink", "purple", "green","pink","maroon"]
                explode = (0, 0, 0, 0,0,0)
                fig1, ax1 = plt.subplots()
                ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors = mycolors)
                ax1.axis('equal')
                st.pyplot(fig1)
            elif income >  2000000:
                st.text("consult with Hedge Funds,private Equity Firms or Venture Capitals as you are regarded as an accredited investor An accredited investor is an individual or entity that meets certain financial and income criteria as established by the Securities and Exchange Commission (SEC). The criteria are intended to identify individuals and entities that have the financial sophistication and ability to bear the economic risks of investing in securities that are not registered with the SEC. Examples of accredited investors include individuals with a net worth of over $1 million (excluding the value of their primary residence), or an annual income of over $200,000 for the past two years (or $300,000 when combined with a spouse). Institutions such as banks, insurance companies, and investment companies also qualify as accredited investors.")
            else:
                st.text("The minimum amount you can buy in an exchange is 10 USD")	
            #"""streamlit run crypto_portfolio.py
def crypto_portfolio1():
	import streamlit as st
	import matplotlib.pyplot as plt

	#st.header("Portfolio Design and Risk Management")
	st.subheader("Crypto portfolio")

	income = st.number_input("Enter your annual income:")
	investment = income * 0.1
	st.text("Invest 10% of your income, or $" + str(investment) + ", in crypto.")

	if income > 100 :
		#st.text("Allocate 30% of your portfolio to layer 1 and the remaining 70% to be equally allocated among layer 0, layer 2 and layer 3.")
		labels = 'LAYER 1', 'LAYER 0', 'LAYER 2', 'LAYER 3','INFRA COINS','AI COINS'
		sizes = [30, 10, 20, 20,10,10]
		mycolors = ["yellow", "hotpink", "purple", "green","pink","maroon"]
		explode = (0, 0, 0, 0,0,0)
		fig1, ax1 = plt.subplots()
		ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors = mycolors)
		ax1.axis('equal')
		st.pyplot(fig1)

	elif income > 100 and income <= 1000:
		#st.text("Allocate 30% of your portfolio to layer 1 and the remaining 70% to be equally allocated among layer 0, layer 2 and layer 3.")
		labels = 'LAYER 1', 'LAYER 0', 'LAYER 2', 'LAYER 3','INFRA COINS','AI COINS'
		sizes = [10, 20, 20, 20,10,20]
		mycolors = ["yellow", "hotpink", "purple", "green","pink","maroon"]
		explode = (0, 0, 0, 0,0,0)
		fig1, ax1 = plt.subplots()
		ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors = mycolors)
		ax1.axis('equal')
		st.pyplot(fig1)

	elif income > 1000 and income <= 10000:
		#st.text("Allocate 30% of your portfolio to layer 1 and the remaining 70% to be equally allocated among layer 0, layer 2 and layer 3.")
		labels = 'LAYER 1', 'LAYER 0', 'LAYER 2', 'LAYER 3','INFRA COINS','AI COINS'
		sizes = [20, 10, 20, 20,20,10]
		mycolors = ["yellow", "hotpink", "purple", "green","pink","maroon"]
		explode = (0, 0, 0, 0,0,0)
		fig1, ax1 = plt.subplots()
		ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors = mycolors)
		ax1.axis('equal')
		st.pyplot(fig1)
	elif income > 10000 and income <= 100000:
		#st.text("Allocate 30% of your portfolio to layer 1 and the remaining 70% to be equally allocated among layer 0, layer 2 and layer 3.")
		labels = 'LAYER 1', 'LAYER 0', 'LAYER 2', 'LAYER 3','INFRA COINS','AI COINS'
		sizes = [30, 10, 20, 20,10,10]
		mycolors = ["yellow", "hotpink", "purple", "green","pink","maroon"]
		explode = (0, 0, 0, 0,0,0)
		fig1, ax1 = plt.subplots()
		ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors = mycolors)
		ax1.axis('equal')
		st.pyplot(fig1)
	elif income > 100000 and income <= 1000000:
		#st.text("Allocate 30% of your portfolio to layer 1 and the remaining 70% to be equally allocated among layer 0, layer 2 and layer 3.")
		labels = 'LAYER 1', 'LAYER 0', 'LAYER 2', 'LAYER 3','INFRA COINS','AI COINS'
		sizes = [40, 10, 20, 10,10,10]
		mycolors = ["yellow", "hotpink", "purple", "green","pink","maroon"]
		explode = (0, 0, 0, 0,0,0)
		
		fig1, ax1 = plt.subplots()
		ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors = mycolors)
		ax1.axis('equal')
		st.pyplot(fig1)
	elif income > 1000000 and income <= 2000000:
		#st.text("Allocate 30% of your portfolio to layer 1 and the remaining 70% to be equally allocated among layer 0, layer 2 and layer 3.")
		labels = 'LAYER 1', 'LAYER 0', 'LAYER 2', 'LAYER 3','INFRA COINS','AI COINS'
		sizes = [50, 10, 10, 10,10,10]
		mycolors = ["yellow", "hotpink", "purple", "green","pink","maroon"]
		explode = (0, 0, 0, 0,0,0)
		fig1, ax1 = plt.subplots()
		ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors = mycolors)
		ax1.axis('equal')
		st.pyplot(fig1)
	elif income >  2000000:
		st.text("consult with Hedge Funds,private Equity Firms or Venture Capitals as you are regarded as an accredited investor An accredited investor is an individual or entity that meets certain financial and income criteria as established by the Securities and Exchange Commission (SEC). The criteria are intended to identify individuals and entities that have the financial sophistication and ability to bear the economic risks of investing in securities that are not registered with the SEC. Examples of accredited investors include individuals with a net worth of over $1 million (excluding the value of their primary residence), or an annual income of over $200,000 for the past two years (or $300,000 when combined with a spouse). Institutions such as banks, insurance companies, and investment companies also qualify as accredited investors.")
	else:
		st.text("The minimum amount you can buy in an exchange is 10 USD")	
	#"""streamlit run crypto_portfolio.py
def dca():
	""" This code uses Streamlit to display the plot instead of using plt.show() at the end. The st.set_style("dark") sets the background of the plot to dark and st.pyplot() to show the plot."""
	import streamlit as st
	import pandas as pd
	import matplotlib.pyplot as plt
	import ta
	def dca_strat():
		import streamlit as st
		import pandas as pd

		st.title("Dollar Cost Averaging Strategy for Bitcoin")

		# Load data for bitcoin prices
		df = pd.read_csv("code_pain.csv")
		df.Date = pd.to_datetime(df.Date)
		df = df[df.Value > 0] # remove rows with closing price of 0 or less
		df.sort_values(by="Date", inplace=True)

		# Get user input for investment amount and interval
		investment_amount = st.number_input("Enter investment amount:", min_value=1, step=1)
		investment_interval = st.number_input("Enter investment interval (in days):", min_value=1, step=1)

		# Get user input for start and end date
		start_date = pd.to_datetime(st.date_input("Enter start date:"))
		end_date = pd.to_datetime(st.date_input("Enter end date:"))

		# Filter dataframe to include only rows within the start and end date range
		df = df[(df.Date >= start_date) & (df.Date <= end_date)]

		# Initialize variables to keep track of investment
		investment_count = 0
		total_invested = 0
		shares_bought = 0

		# Validation check for investment amount
		if investment_amount < 10:
			st.error("Investment amount must be greater than $10")
		else:
			# Iterate through the data and make investments at the specified intervals
			for index, row in df.iterrows():
				if investment_count % investment_interval == 0:
					# Make investment
					investment_count = 0
					shares_bought += investment_amount / row["Value"]
					total_invested += investment_amount
					st.write("Bought {:.8f} BTC for ${} on {}".format(investment_amount/row["Value"], investment_amount, row["Date"]))
				investment_count += 1

			# Print total invested and final value of investment
			if df.empty:
				st.warning("No data within the specified date range")
			else:
				final_value = shares_bought * row["Value"]
				st.write("Total invested: ${}".format(total_invested))
				st.write("Final value of investment: {:.2f}".format(final_value))

	#st.set_style("dark")

	df = pd.read_csv("code_pain.csv")[["Date","Value"]]
	df.Date = pd.to_datetime(df.Date)
	df = df[df.Value > 0]
	df.sort_values(by="Date", inplace=True)

	fig, (ax1, ax2) = plt.subplots(2, sharex=True)
	ax1.semilogy(df.Date, df.Value,linewidth=0.5)
	df["rsi"] = ta.momentum.rsi(close=df.Value, window=14)
	ax2.axhline(80, color="yellow",linewidth=0.8)
	ax2.axhline(95, color="red",linewidth=0.8)
	#ax2.axhline(50, color="black",linewidth=0.8)
	ax2.axhline(25, color="green",linewidth=0.8)
	ax2.axhline(10, color="green",linewidth=0.8)
	ax2.text(df.Date.iloc[-1], 85, 'Take Profit', fontsize=8, rotation=0,
			ha='left', va='center',color='blue',
			bbox=dict(boxstyle='round', ec='k', fc='w'))
	ax2.text(df.Date.iloc[-1], 15, 'Build a position', fontsize=8, rotation=0,
			ha='left', va='center',color='blue',
			bbox=dict(boxstyle='round', ec='k', fc='w'))
	if df["rsi"].iloc[-1] > 80:
		# Sell/DCA out
		st.write("RSI is above 80, time to sell/DCA out")
		dca_strat()
		
	elif df["rsi"].iloc[-1] < 25:
		# Buy/DCA in
		st.write("RSI is below 20, time to buy/DCA in")
		dca_strat()
		
	else:
		st.write("RSI is between 20 and 80, hold position")


	ax2.plot(df.Date, df.rsi,linewidth=0.5)
	st.set_option('deprecation.showPyplotGlobalUse', False)
	st.pyplot()
	#streamlit run momentum_strat.py
def topcryptos2():
    import streamlit as st
    import pandas as pd
    import numpy as np
    import time
    import matplotlib
    #import streamlit as st
    import matplotlib.pyplot as plt
    matplotlib.use('Agg')
    st.header("Top 100 Cryptocurrencies")
     #dataframe = dataframe.drop(columns=["ATH","% ATH"], axis=1)

    data=pd.read_csv("satoshi 100 index data58.csv")
    st.dataframe(data)
def topcryptos():
    import streamlit as st
    import pandas as pd
    import numpy as np
    import time
    import matplotlib
    #import streamlit as st
    import matplotlib.pyplot as plt
    matplotlib.use('Agg')
    st.header("Top 100 Cryptocurrencies By Market Capitalization")
     #dataframe = dataframe.drop(columns=["ATH","% ATH"], axis=1)

    dataframe=pd.read_csv("satoshi 100 index data58.csv")
    #st.dataframe(data)
    dataframe.index.name = "rank"
	#converting column to list
    #dataframe=pd.read_csv("satoshi 100 index data58.csv")
    liquidity_risk=[ ]
    for index in dataframe.index:
            if (dataframe["24H Vol"][index])<(dataframe["Market Cap"][index]*0.05):
                liquidity_risk.append("illiquid")

            elif (dataframe["24H Vol"][index])>(dataframe["Market Cap"][index]*0.05) and (dataframe["24H Vol"][index])<=(dataframe["Market Cap"][index]*0.1):
                liquidity_risk.append("fairly liquid")
            elif (dataframe["24H Vol"][index]) > (dataframe["Market Cap"][index] * 0.1) and (dataframe["24H Vol"][index]) <= (dataframe["Market Cap"][index] * 0.3 ):
                liquidity_risk.append("highly liquid") 
            
            elif (dataframe["24H Vol"][index]) > (dataframe["Market Cap"][index] * 0.3) and (dataframe["24H Vol"][index]) <= (dataframe["Market Cap"][index] * 0.5):
                
                liquidity_risk.append("limited long term potential")
            elif (dataframe["24H Vol"][index]) > (dataframe["Market Cap"][index] * 0.5):
                liquidity_risk.append("stay off/sell off")
            
    dataframe['liquidity_risk'] = liquidity_risk
    dataframe.loc[dataframe['Name'].isin(['Tether USDT','USD Coin USDC','Binance USD BUSD','Dai DAI','Paxos Standard USDP','TrueUSD TUSD','USDD USDD','Neutrino USD USDN','Gemini Dollar GUSD',"cDAI. cdai","cUSDC. cusdc"]), 'liquidity_risk'] = 'stablecoin'
    st.dataframe(dataframe)
    #streamlit run full_scrap.py
#streamlit run  static_riskl.py
def risk_environment():
	import streamlit as st
	import pandas as pd
	import matplotlib.pyplot as plt
	import ta

	df = pd.read_csv("code_pain.csv")[["Date","Value"]]
	df.Date = pd.to_datetime(df.Date)
	df = df[df.Value > 0]
	df.sort_values(by="Date", inplace=True)

	# Calculate the 200-day moving average
	df["ma"] = df["Value"].rolling(window=200).mean()

	fig, ax = plt.subplots()
	ax.semilogy(df.Date, df.Value, linewidth=0.5)
	ax.plot(df.Date, df.ma, color='red', linewidth=1)

	st.set_option('deprecation.showPyplotGlobalUse', False)
	st.pyplot()

	# Check if the Bitcoin price is above the 200-day moving average
	if df.Value.iloc[-1] > df.ma.iloc[-1]:
		st.write("We are in a risk-on environment!")
	else:
		st.write("We are in a risk-off environment!")
def scrapping():
	import pandas as pd
	import numpy as np
	import streamlit as st
	import requests
	#dataframe.index.name = "rank"
	r=requests.get("https://cryptoslate.com/coins/",verify=True)
	dataframe=pd.read_html(r.text)[0]
	dataframe.index.name = "rank"
	dataframe=dataframe[["Name","Price","Market Cap","24H Vol","24H %","7D %","30D %","ATH","% ATH"]]
	#dataframe = dataframe.drop(columns=[' '], axis=1)

	dataframe["Name"]=dataframe["Name"].apply(lambda x: x.split("  ")[0])#modify elements(entries) in x
	dataframe["Price"]=dataframe["Price"].apply(lambda x:x.replace(",","").replace("$",""))

	dataframe['Market Cap'] = dataframe['Market Cap'].str.replace(',', '').str.replace('$', '')
	dataframe["Market Cap"] = pd.to_numeric(dataframe["Market Cap"]).abs()
	dataframe["24H Vol"]=dataframe["24H Vol"].str.replace(',', '').str.replace('$', '')
	dataframe["24H Vol"] = pd.to_numeric(dataframe["24H Vol"]).abs()
	dataframe["ATH"]=dataframe["ATH"].str.replace(',', '').str.replace('$', '')

	#TO add % comment 
	dataframe["24H %"]=dataframe["24H %"].str.replace('%', '')
	dataframe["24H %"] = pd.to_numeric(dataframe["24H %"])
	dataframe["7D %"]=dataframe["7D %"].str.replace('%', '')
	dataframe["7D %"] = pd.to_numeric(dataframe["7D %"])
	dataframe["30D %"]=dataframe["30D %"].str.replace('%', '')
	dataframe["30D %"] = pd.to_numeric(dataframe["30D %"])
	dataframe["% ATH"]=dataframe["% ATH"].str.replace('%', '')
	dataframe["% ATH"] = pd.to_numeric(dataframe["% ATH"])
 

	data=dataframe.to_csv("satoshi 100 index data58.csv",index=True )#index true 0-99
	#st.dataframe(data)
	dataframe.index.name = "rank"
	#converting column to list
	dataframe=pd.read_csv("satoshi 100 index data58.csv")
	liquidity_risk=[ ]
	for index in dataframe.index:
			if (dataframe["24H Vol"][index])<(dataframe["Market Cap"][index]*0.05):
				liquidity_risk.append("illiquid")

			elif (dataframe["24H Vol"][index])>(dataframe["Market Cap"][index]*0.05) and (dataframe["24H Vol"][index])<=(dataframe["Market Cap"][index]*0.1):
				liquidity_risk.append("fairly liquid")
			elif (dataframe["24H Vol"][index]) > (dataframe["Market Cap"][index] * 0.1) and (dataframe["24H Vol"][index]) <= (dataframe["Market Cap"][index] * 0.3 ):
				liquidity_risk.append("highly liquid") 
			
			elif (dataframe["24H Vol"][index]) > (dataframe["Market Cap"][index] * 0.3) and (dataframe["24H Vol"][index]) <= (dataframe["Market Cap"][index] * 0.5):
				
				liquidity_risk.append("limited long term potential")
			elif (dataframe["24H Vol"][index]) > (dataframe["Market Cap"][index] * 0.5):
				liquidity_risk.append("stay off")
			
	dataframe['liquidity_risk'] = liquidity_risk
	dataframe.loc[dataframe['Name'].isin(['Tether USDT','USD Coin USDC','Binance USD BUSD','Dai DAI','Paxos Standard USDP','TrueUSD TUSD','USDD USDD','Neutrino USD USDN','Gemini Dollar GUSD',"cDAI. cdai","cUSDC. cusdc"]), 'liquidity_risk'] = 'stablecoin'
	st.dataframe(dataframe)
	#streamlit run full_scrap.py

def altcoinseason():
	import pandas as pd
	import streamlit as st
	import matplotlib.pyplot as plt

	st.title("Altcoin Season Indicator")

	# Read in dataframe
	dataframe = pd.read_csv("satoshi 100 index data58.csv")
	stablecoins = ['Tether USDT','USD Coin USDC','Binance USD BUSD','Dai DAI','Paxos Standard USDP','TrueUSD TUSD','USDD USDD','Neutrino USD USDN','Gemini Dollar GUSD',"cDAI. cdai","cUSDC. cusdc","cETH. ceth","Wrapped Bitcoin WBTC"]
	dataframe = dataframe[~dataframe['Name'].isin(stablecoins)]
	#Check if the dataframe is empty or not
	if dataframe.empty:
		st.error("Dataframe is empty")
	else:
		# Select top 99 coins
		top_99 = dataframe.head(99)

		# Check if there is "Bitcoin BTC" in the dataframe
		bitcoin_24H_perc = dataframe.loc[dataframe["Name"] == "Bitcoin BTC", "24H %"]
		if bitcoin_24H_perc.empty:
			st.error("Bitcoin BTC not found in dataframe")
		else:
			# Prompt user to input the timeframe
			timeframe = st.selectbox("Select a timeframe:", ["Daily", "Weekly", "Monthly"])

			# Use the selected timeframe to select the appropriate column from the dataframe
			if timeframe == "Daily":
				selected_column = "24H %"
			elif timeframe == "Weekly":
				selected_column = "7D %"
			elif timeframe == "Monthly":
				selected_column = "30D %"
			else:
				st.error("Invalid timeframe selected")
				#return

			# Create a new column that calculates the percentage difference between each coin's selected column and Bitcoin BTC's selected column
			top_99["Difference"] = top_99[selected_column] - bitcoin_24H_perc.values[0]

			# Create a new column that indicates whether each coin outperforms Bitcoin BTC or not
			top_99["Outperforms"] = top_99["Difference"] > 0

			# Count the number of coins that outperform Bitcoin BTC
			outperformers = top_99["Outperforms"].sum()

			# Calculate the percentage of coins that outperform Bitcoin BTC
			percent_outperform = (outperformers / len(top_99)) * 100

			# Create a pie chart to visualize the results
			labels = ["Altcoin Season", "Bitcoin BTC Season"]
			mycolors = ["yellow","b"]
			sizes = [percent_outperform, 100 - percent_outperform]
			st.set_option('deprecation.showPyplotGlobalUse', False)
			plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90,colors=mycolors)
			plt.axis('equal')
			st.pyplot()
   
			if percent_outperform > 95 and percent_outperform<100:
				st.warning("The altcoins are so overvalued in the timeframe take profits agressively into stablecoins,BTC and ETH")
			elif percent_outperform > 90 and percent_outperform<=95:
				st.warning("Take some profits into BTC,ETH and stablecoins")
			elif percent_outperform > 80 and percent_outperform<=90:
				st.warning("Research on coins that could have reached a local top (potential short the reap)")
			elif percent_outperform > 10 and percent_outperform<=20:
				st.warning("Research on coins that could have reached a local bottom (potential buy the dip coins gradually)")    
			elif percent_outperform > 5 and percent_outperform<=10:
				st.warning("Sell some BTC into altcoins")
			elif percent_outperform > 1 and percent_outperform<=5:
				st.warning("The altcoins are so undervalued in the timeframe sell stablecoins,BTC and ETH gradually into the altcoins")
			else:
				st.error("stay in your positions")

			
def crypto_quantitative_analysis():
    
	import streamlit as st
	import pandas as pd
	import numpy as np
	import time
	import matplotlib
	#import streamlit as st
	import matplotlib.pyplot as plt
	matplotlib.use('Agg')


	#st.set_page_config(layout="wide")
	tab1, tab2, tab3,tab4,tab5,tab6,tab7,tab8,tab9 = st.tabs(["RISK DISCLAIMER","Top 100 Cryptocurrencies","Macro Analysis", "Sentiment Analysis","Risk Mode", "portfolio design and risk management","Altcoin Season Index","Profit taking and DCA","Market Report"])
	with tab1:
		st.header("RISK DISCLAIMER")
		
		st.text(" \n\r       Before deciding to participate in the Crypto market,you should carefully consider your investment objectives, \n\rlevel of experience and risk appetite.Most importantly, do not invest money you cannot afford to lose.\n\rCrypto trading is very risky and you may lose all or some of your investments. \n\rAll the information, analyses, opinions, news, research, prices, or other information  are provided as general market commentary,\n\rand do not constitute or imply any investment advice.\n\rUnder no circumstances will OpenCipher  accept any liability for any loss or damage, including, any loss of profit, \n\rwhich may arise directly or indirectly from the use of or complete reliance on information contained in the given articles or in any analyses.")

	with tab2:
		
		#topcryptos()
		scrapping()
	
	

	with tab3:
		st.header("Macro Analysis")
		import streamlit as st
		import matplotlib.pyplot as plt
			#time.sleep(10)
		from PIL import Image
		image = Image.open('analysis USIRYY_2023-03-11_15-45-25.png')
		image2 = Image.open('analysis USCCPI_2023-03-11_11-12-48.png')
		image3 = Image.open('analysis UNRATE_2023-03-11_11-29-40.png')
		image4 = Image.open('analysis T10Y2Y_2023-03-11_11-25-19.png')
		image5 = Image.open('analysis FEDFUNDS_2023-03-11_11-22-47.png')
		
		st.text("MACRO IS KING")
		st.image(image, caption='UNITED STATES HEADLINE INFLATION DATA')
		st.image(image2, caption='UNITED STATES CORE INFLATION DATA')
		st.image(image3, caption='UNITED STATES UNEMPLOYMENT RATE')
		st.image(image4, caption='RECESSION CALLS')
		st.image(image5, caption='UNITED STATES INTEREST RATES')
		
  
	
	

	with tab4:
		import pandas as pd
		import numpy as np
		import matplotlib.pyplot as plt
		import streamlit as st

		st.set_option('deprecation.showPyplotGlobalUse', False)

		def sentiment_analysis():
			st.header("Sentiment Analysis")

			# Read the CSV file
			dataframe = pd.read_csv("add_now.csv")
			dataframe = dataframe.iloc[::-1]

			# Ensure the "Value" column contains only numeric data
			dataframe['Value'] = pd.to_numeric(dataframe['Value'], errors='coerce')
			dataframe = dataframe.dropna(subset=['Value'])

			# Calculate the 200wma
			dataframe['200wma'] = dataframe['Value'].rolling(window=1400).mean()

			# Extract dates and convert 'Date' to datetime format
			dataframe['Date'] = pd.to_datetime(dataframe['Date'], format='%d/%m/%Y')
			dates = dataframe['Date']

			# Sort DataFrame by 'Date'
			dataframe = dataframe.sort_values(by='Date')

			# Select every 30th row for monthly data
			monthly = dataframe[::30]

			# Calculate percentage monthly increase in 200wma
			distance = monthly['200wma'].pct_change() * 100

			# Plotting
			plt.style.use("dark_background")

			plt.semilogy(dates, dataframe['Value'], color="grey", zorder=1)
			plt.semilogy(dates, dataframe['200wma'], color="purple", zorder=2)

			plt.scatter(monthly['Date'], monthly['Value'], c=distance, cmap='rainbow', vmin=0, vmax=16, zorder=4)

			cbar = plt.colorbar()
			cbar.set_label("% monthly increase in 200wma")
			cbar.ax.yaxis.set_label_position("left")

			# Display the plot in Streamlit
			st.pyplot()

			# Save the updated DataFrame to a new CSV file
			dataframe.to_csv("code_pain.csv", index=False)

		# Call the function
		sentiment_analysis()
		"""
		st.header("Sentiment Analysis")
		import pandas as pd
		import matplotlib.pyplot as plt
		matplotlib.use('Agg')
		
			
			#time.sleep(10)
		dataframe = pd.read_csv("code_pain.csv")
		dataframe = dataframe.iloc[::-1]
		dataframe['200wma'] = dataframe['Value'].rolling(window = 1400).mean()

		dataframe = dataframe[1400:]
		dates = pd.to_datetime(dataframe['Date'])

		monthly = dataframe[::30]

		distance = monthly['200wma'].pct_change() * 100





		plt.style.use("dark_background")

		plt.semilogy(dates, dataframe['Value'], color = "grey", zorder = 1)
		plt.semilogy(dates, dataframe['200wma'], color = "purple", zorder = 2)

			
		plt.scatter(monthly['Date'], monthly['Value'], c = distance, cmap = 'rainbow', vmin = 0, vmax = 16, zorder = 4 )
			
		cbar = plt.colorbar()
		cbar.set_label("% monthly increase in 200wma")
		cbar.ax.yaxis.set_label_position("left")
			
		
		st.set_option('deprecation.showPyplotGlobalUse', False)

		st.pyplot( )
		macro_analysis()"""
	with tab5:
		risk_environment()

	with tab6:
		#st.header("portfolio design and risk management")
		st.subheader("Crypto and the legacy market portfolio")
		age= st.number_input("enter your age:")    
		#age=int(input("enter your age:"))
		#print("your age is",age)
		#age=18
		if age==18:
			#print("you are of age.")
			st.text("you are of age.")
			#print("allocate 50% of your portfolio to BTC")
			st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
			#st.text("allocate 50% of your portfolio to crypto and 50 % between the SP500,DJIA and NASDAQ indices")
			import streamlit as st
			import matplotlib.pyplot as plt
			#time.sleep(10)
			
			# Pie chart, where the slices will be ordered and plotted counter-clockwise:
			labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ','Fine Art'
			sizes = [40, 15,15,15,15]
			mycolors = ["yellow", "hotpink", "b", "#4CAF50","maroon"]
			explode = (0, 0.1, 0, 0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')
			fig1, ax1 = plt.subplots()
			ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
				shadow=True, startangle=90,colors = mycolors)
			ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

			st.pyplot(fig1)
		
				
		elif age>18 and age<=30:
			#print("allocate 50% of your portfolio to BTC")
			st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
			#st.text("allocate 50% of your portfolio to crypto and 50 % between the SP500,DJIA and NASDAQ indices")
			import streamlit as st
			import matplotlib.pyplot as plt
			#time.sleep(10)
			# Pie chart, where the slices will be ordered and plotted counter-clockwise:
			labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ','Fine Art'
			sizes = [40, 15,15,15,15]
			mycolors = ["yellow", "hotpink", "b", "#4CAF50","maroon"]
			explode = (0, 0.1, 0, 0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')
			fig1, ax1 = plt.subplots()
			ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
				shadow=True, startangle=90,colors = mycolors)
			ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

			st.pyplot(fig1)
			
		elif age>30 and age<=40:
			#print("allocate 40% of your portfolio to BTC")
			st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
			#st.text("allocate 40% of your portfolio to crypto and 60 % between the SP500,DJIA and NASDAQ indices")
			import streamlit as st
			import matplotlib.pyplot as plt
			#time.sleep(10)
			# Pie chart, where the slices will be ordered and plotted counter-clockwise:
			labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ','Fine Art'
			sizes = [35, 16.25, 16.25, 16.25,16.25]
			mycolors = ["yellow", "hotpink", "b", "#4CAF50","maroon"]
			explode = (0, 0.1, 0, 0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')
			fig1, ax1 = plt.subplots()
			ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
				shadow=True, startangle=90,colors = mycolors)
			ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

			st.pyplot(fig1)
			
		elif age>40 and age<=50:
			#print("allocate 30% of your portfolio to BTC")
			st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
			#st.text("allocate 30% of your portfolio to crypto and 70 % between the SP500,DJIA and NASDAQ indices")
			import streamlit as st
			import matplotlib.pyplot as plt
			#time.sleep(10)
			# Pie chart, where the slices will be ordered and plotted counter-clockwise:
			labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ','Fine Art'
			sizes = [30, 17.5, 17.5, 17.5,17.5]
			mycolors = ["yellow", "hotpink", "b", "#4CAF50","maroon"]
			explode = (0, 0.1, 0, 0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')
			fig1, ax1 = plt.subplots()
			ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
				shadow=True, startangle=90,colors = mycolors)
			ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

			st.pyplot(fig1)
			

		elif age>50 and age<=60:
			#print("allocate 20% of your portfolio to BTC")
			st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
			#st.text("allocate 20% of your portfolio to crypto and 80 % between the SP500,DJIA and NASDAQ indices")
			import streamlit as st
			import matplotlib.pyplot as plt
			#time.sleep(10)
			# Pie chart, where the slices will be ordered and plotted counter-clockwise:
			labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ','Fine Art'
			sizes = [25, 18.75, 18.75, 18.75,18.75]
			mycolors = ["yellow", "hotpink", "b", "#4CAF50","maroon"]
			explode = (0, 0.1, 0, 0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')
			fig1, ax1 = plt.subplots()
			ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
				shadow=True, startangle=90,colors = mycolors)
			ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

			st.pyplot(fig1)
			
			
		elif age>60 and age<=70:
			#print("allocate 10% of your portfolio to BTC")
			st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
			#st.text("allocate 10% of your portfolio to crypto and 90 % between the SP500,DJIA and NASDAQ indices")
			import streamlit as st
			import matplotlib.pyplot as plt
			#time.sleep(10)
			# Pie chart, where the slices will be ordered and plotted counter-clockwise:
			labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ','Fine Art'
			sizes = [20, 20, 20, 20,20]
			mycolors = ["yellow", "hotpink", "b", "#4CAF50","maroon"]
			explode = (0, 0.1, 0, 0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')
			fig1, ax1 = plt.subplots()
			ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
				shadow=True, startangle=90,colors = mycolors)
			ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

			st.pyplot(fig1)
			
			
		elif age>70 and age<=200:
			#print("allocate 5% of your portfolio to BTC")
			st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
			#st.text("allocate 5% of your portfolio to crypto and 95 % between the SP500,DJIA and NASDAQ indices")
			import streamlit as st
			import matplotlib.pyplot as plt
			#time.sleep(10)
			# Pie chart, where the slices will be ordered and plotted counter-clockwise:
			labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ','Fine Art'
			sizes = [10, 22.5,22.5,22.5,22.5]
			mycolors = ["yellow", "hotpink", "b", "#4CAF50","maroon"]
			explode = (0, 0.1, 0, 0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')
			fig1, ax1 = plt.subplots()
			ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
				shadow=True, startangle=90,colors = mycolors)
			ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
			st.pyplot(fig1)
			
			
		else:
			st.text("can not access the model.")
		crypto_portfolio1()	
		
	with tab7:
		altcoinseason()
	
	with tab8:
		dca()	
	with tab9:
		market_report()
		

import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data



def main():
	"""Simple Login App"""

	#st.title("Simple Login App")
	import streamlit as st
	menu = ["Home","Login","SignUp","Logout","Reset Password","Help"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		#st.subheader("Home")
		#st.write("Welcome to our platform!")
		#topcryptos()
		scrapping()
	elif choice == "Login":
		username = st.sidebar.text_input("User Name")
		password = st.sidebar.text_input("Password",type='password')
		if st.sidebar.checkbox("Login"):
			# if password == '12345':
			create_usertable()
			hashed_pswd = make_hashes(password)

			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:

				st.success("Logged In as {}".format(username))

				#crypto_quantitative_analysis()
				task = st.selectbox("Task",["Qualitative Analysis","Quantitative Analysis","Profiles"])
				if task == "Qualitative Analysis":
					st.subheader("Add Your Post")
					#investor_connect()
					#investor_connect1()
					investor_connect2()
					media_socials()
					
					comments = st.text_input('Leave a Comment Below: ')
					st.button('Submit Comment')
					

				elif task == "Quantitative Analysis":
		
					
					st.subheader("Quantitative Analysis")
					crypto_quantitative_analysis()
					
					
				elif task == "Profiles":
					
					if(username=="mokua254"):
						st.subheader("User Profiles")
						user_result = view_all_users()
						clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
						st.dataframe(clean_db)
					else:
						st.warning("can not access profiles ")
			else:
				st.warning("Incorrect Username/Password")
	elif choice == "Logout":
			st.subheader("Logout Section")
			logout_button = st.button("Logout")
			if logout_button:
				st.sidebar.empty()
				st.warning("You have been logged out")

	elif choice == "Reset Password":
		st.subheader("Reset Password")
		username = st.text_input("Username")
		old_password = st.text_input("Old Password", type='password')
		new_password = st.text_input("New Password", type='password')

		if st.button("Reset"):
			create_usertable()
			hashed_pswd = make_hashes(old_password)

			result = login_user(username, check_hashes(old_password, hashed_pswd))
			if result:
				reset_password(username, new_password)

			else:
				st.warning("Incorrect Username/Password")


	elif choice == "SignUp":
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')

		if st.button("Signup"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.success("You have successfully created a valid Account")
			st.info("Go to Login Menu to login")

	elif choice == "Help":
		st.subheader("Risk Disclaimer")
		st.text(" \n\r       Risk is fundamental to the investment process, but remains a concept that is not particularly well understood by most regular investors.\n\rThe objective this disclaimer is not only to explain to the investor the nature of the risks involved in the volatile \n\rcrypto market investment vehicles being offered, but also to ensure that there can be no lawsuits if things go badly. ")
		st.subheader("Top 100 Cryptos")
		st.text(" \n\r       The Lindy Effect essentially states that the longer a non-perishable item has been around, the longer it's likely to persist into the future.\n\rThis can translate to technological ideas like cryptocurrencies.This being the first macro correction of bitcoins and other altcoins\n\r most altcoins will trend to zero and give room to quality projects to emerge and loss their market share to existing\n\r fundamentally strong projects.Using the top 100 cryptocurrencies presents a conservative way of investing in this risk off environment.")
		st.subheader("Macro Analysis")
		st.text(" \n\r       Headline inflation refers to the overall change in the price level of goods and services in an economy, including all items in the \n\r Consumer Price Index (CPI) basket, which is used to measure inflation. This includes food, energy, and other volatile items that can\n\r experience  significant price swings in short periods of time. Core CPI, on the other hand, is a measure of inflation that \n\rexcludes food and energy prices, which are typically more volatile than other prices. \n\rThis is done to provide a more stable measure of underlying inflation trends, as food and energy prices can be influenced by factors such as \n\rweather events or geopolitical events that can cause temporary price spikes.")
		st.subheader("Sentiment Analysis")
		st.text(" \n\r       Warren Buffett once said that it is wise for investors to be “fearful when others are greedy, and greedy when others are fearful.\n\rThis statement is somewhat of a contrarian view on capital markets and relates directly to the price of an asset: \n\rwhen others are greedy, prices typically boil over, and one should be cautious lest they overpay for an asset that \n\rsubsequently leads to anemic returns.When others are fearful, it may present a good value investment opportunity.\n\rSince the price is what you pay, and value is what you get, paying too high a price can decimate returns.\n\r According to the indicator the ranges between 0-violet -2-light blue present good buy opportunity from a risk to reward \n\rstandpoint(usually calls micro and macro bottoms).According to the indicator the ranges between 14-orange -16-red present good \n\rselling opportunity from a risk to reward standpoint(usually calls micro and macro tops).\n\r The ranges between 4-blue and 12-yellow present an opportunity to hodl your positions for an optimal exit in the future. ")
		st.subheader("Risk Mode")
		st.text(" \n\r       Whenever price action goes above the 200 daily MA we transion to a risk on environment.\n\rTherefore investors should have some skin in the game incase the bottom was in :have exposure to some \n\raltcoins.But whenever the price action is below the 200 daily MA ,investors ought to start derisking\n\r and taking profits Aggressively as were are potentially moving into a risk of environment. ")
		st.subheader("portfolio design and risk management")
		st.text(" \n\r       We help you design an all weather portfolio that can withstand any market conditions . \n\rDepending on your age we help your deploy capital into to the legacy markets and the crypto markets.\n\rDepending on your annual income  we help your deploy capital across the different  crypto narratives.")
		st.subheader("Altcoin Season Index")
		st.text(" \n\r       Altcoin season is a crypto phenomenon, where most cryptocurrency prices surge with the exception of Bitcoin(outperform Bitcoin). \n\rDuring an altcoin season you should a significant exposure to alcoins but in a bitcoin season you should have a significant exposure to Bitcoin.\n\rWhenever more than 80% of the altcoins outperform bitcoins it is usually a good time to start hedging your portfolio.\n\rHedging can be done in two ways :conservatively or Aggressively.\n\rBy being conservative you can sell  a portion of your altcoins  into stablecoins. By taking the Aggressive path you sell a portion of your\n\r altcoins into bitcoin and ethereum(which is a longterm hodl position) or you can open short positions(only for experienced traders). \n\rIf Bitcoin outperforms more than 80% of the altcoins it is usually a good time to start having a significant exposure to some altcoins ,\n\ras this indicates undervaluation of alcoins and vv.")
		st.subheader("Profit Taking and DCA")
		st.text(" \n\r       The success of any retail investor or the trader is measured by how much profits they take home.  \n\rTo achieve this we use the  Dollar-cost averaging (DCA)  an investment strategy in which the intention is to minimize the impact of volatility\n\r when investing or purchasing a fixed large block of a financial asset or instrument over a given period in a fixed  interval.\n\r The strategy is deployed whenever the Relative Strength Index(RSI)is between 80 and 95 or whenever the RSI is below the 25 mark.\n\rHistorically whenever the Relative Strength Index(RSI)is between 80 and 95 it is usually regarded a good time take some partial profits  or\n\r historically whenever the RSI is below the 25 mark it is usually a good time to start building positions(longing,buying coins)")
		st.subheader("Market Report")
		st.text(" \n\r       It shows the top gainers and lossers on the daily,weekly and monthly timeframes. \n\rIf you are using a momentum investing and trend following strategy this could come in handy. \n\rIn addition,if on the daily,weekly or monthly timeframes the top gainers or biggest lossers are stablecoins  this could help predict\n\r the investor behaviour.If stablecoins comprise of the biggest gainers in any timeframe this means investors are moving from\n\r the coins(btc,eth and altcoins)  into the sideline which consequently,means loss of confidence by investors within that timeframe .\n\r If stablecoins comprise of the biggest lossers in any timeframe this means investors are moving from  the sideline into the \n\rcoins(btc,eth and altcoins) which consequently,means gaining of confidence by investors within that timeframe .")

if __name__ == '__main__':
	main()
#streamlit run streamlit_login.py
#streamlit run open_cipher.py

# Megatron1080
#python.exe -m pip install --upgrade pip --user