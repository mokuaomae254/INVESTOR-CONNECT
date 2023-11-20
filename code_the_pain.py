'''solution 1'''
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

#streamlit run code_the_pain.py
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