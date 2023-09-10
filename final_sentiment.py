import pandas as pd
import numpy as np
import matplotlib
import streamlit as st
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
def Sentiment_Analysis():
    st.header("Sentiment_ Analysis")
    import pandas as pd
    import matplotlib.pyplot as plt
    matplotlib.use('TkAgg')
    
        
        #time.sleep(10)
    dataframe = pd.read_csv("BCHAIN-MKPRU.csv")
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

st.header("portfolio design and risk management")
st.subheader("Crypto and the legacy market portfolio")
age= st.number_input("enter your age:")    

if age==18:
    #print("you are of age.")
    st.text("you are of age.")
    #print("allocate 50% of your portfolio to BTC")
    st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
    Sentiment_Analysis()
    st.text("allocate 50% of your portfolio to crypto and 50 % between the SP500,DJIA and NASDAQ indices")
    import streamlit as st
    import matplotlib.pyplot as plt
    #time.sleep(10)
    
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ'
    sizes = [50, 16.67, 16.67, 16.67]
    mycolors = ["yellow", "hotpink", "b", "#4CAF50"]
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90,colors = mycolors)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)

        
elif age>18 and age<=30:
    #print("allocate 50% of your portfolio to BTC")
    st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
    Sentiment_Analysis()
    st.text("allocate 50% of your portfolio to crypto and 50 % between the SP500,DJIA and NASDAQ indices")
    import streamlit as st
    import matplotlib.pyplot as plt
    #time.sleep(10)
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ'
    sizes = [50, 16.67, 16.67, 16.67]
    mycolors = ["yellow", "hotpink", "b", "#4CAF50"]
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90,colors = mycolors)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)
    
elif age>30 and age<=40:
    #print("allocate 40% of your portfolio to BTC")
    st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
    Sentiment_Analysis()
    st.text("allocate 40% of your portfolio to crypto and 60 % between the SP500,DJIA and NASDAQ indices")
    import streamlit as st
    import matplotlib.pyplot as plt
    #time.sleep(10)
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ'
    sizes = [40, 20, 20, 20]
    mycolors = ["yellow", "hotpink", "b", "#4CAF50"]
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90,colors = mycolors)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)
    
elif age>40 and age<=50:
    #print("allocate 30% of your portfolio to BTC")
    st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
    Sentiment_Analysis()
    st.text("allocate 30% of your portfolio to crypto and 70 % between the SP500,DJIA and NASDAQ indices")
    import streamlit as st
    import matplotlib.pyplot as plt
    #time.sleep(10)
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ'
    sizes = [30, 23.33, 23.33, 23.33]
    mycolors = ["yellow", "hotpink", "b", "#4CAF50"]
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90,colors = mycolors)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)
    

elif age>50 and age<=60:
    #print("allocate 20% of your portfolio to BTC")
    st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
    Sentiment_Analysis()
    st.text("allocate 20% of your portfolio to crypto and 80 % between the SP500,DJIA and NASDAQ indices")
    import streamlit as st
    import matplotlib.pyplot as plt
    #time.sleep(10)
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ'
    sizes = [20, 26.67, 26.67, 26.67]
    mycolors = ["yellow", "hotpink", "b", "#4CAF50"]
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90,colors = mycolors)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)
    
    
elif age>60 and age<=70:
    #print("allocate 10% of your portfolio to BTC")
    st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
    Sentiment_Analysis()
    st.text("allocate 10% of your portfolio to crypto and 90 % between the SP500,DJIA and NASDAQ indices")
    import streamlit as st
    import matplotlib.pyplot as plt
    #time.sleep(10)
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ'
    sizes = [10, 30, 30, 30]
    mycolors = ["yellow", "hotpink", "b", "#4CAF50"]
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90,colors = mycolors)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)
    
    
elif age>70 and age<=200:
    #print("allocate 5% of your portfolio to BTC")
    st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
    Sentiment_Analysis()
    st.text("allocate 5% of your portfolio to crypto and 95 % between the SP500,DJIA and NASDAQ indices")
    import streamlit as st
    import matplotlib.pyplot as plt
    #time.sleep(10)
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ'
    sizes = [5, 31.67, 31.67, 31.67]
    mycolors = ["yellow", "hotpink", "b", "#4CAF50"]
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90,colors = mycolors)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)
    
    
else:
    st.write("can not access the model.")
#streamlit run final_sentiment.py
#python -m venv open_cipher
#python -m venv open_cipher

