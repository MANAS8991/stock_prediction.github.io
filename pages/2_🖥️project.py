import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
from pandas_datareader import data as pdr
from keras.models import load_model
import yfinance as yfin
yfin.pdr_override()

#menu
#pip install streamlit-option-menu
st.title('Stock Trend Prediction')
image =Image.open('dpp.png')
st.image(image, width=600)
user_input=st.text_input('Enter Stock Ticker', 'GOOGL')
df=pdr.get_data_yahoo(user_input,start="2010-01-01",end="2023-01-01")







# describing data
# Colorful subheader for the table
st.markdown("<h3 style='color: orange;'>Data From 2010-2023</h3>", unsafe_allow_html=True)

# Display the table with colorful styling
st.write(df.describe().style.set_table_styles([
    {'selector': 'th', 'props': [('background-color', 'orange'), ('color', 'white')]},
    {'selector': 'td', 'props': [('background-color', 'lightblue')]}
]))

# Colorful subheader for the bar chart
st.markdown("<h3 style='color: orange;'>Data Bar Chart</h3>", unsafe_allow_html=True)

st.bar_chart(df)
 

# Add a colored subheader and a paragraph below the chart
st.markdown("<h3 style='color: yellow;'>Chart Explanation</h3>", unsafe_allow_html=True)
st.markdown("""
The Data Bar Chart provides a visual representation of the data from 2010-2023 in the form of bars. Each bar represents a category, and its length corresponds to the respective value. The chart allows for easy comparison of values across different categories. The subheader and chart are displayed in orange color to add emphasis. The bars are colored using the 'Set2' color palette to enhance visual appeal and distinguish between categories. This colorful presentation makes it easier to interpret the data and identify patterns or trends.
""")
 # visualization


st.markdown("<h3 style='color: orange;'>Closing Price vs Time Chart</h3>", unsafe_allow_html=True)
# Set the size of the figure
fig, ax = plt.subplots(figsize=(12, 6))

# Plot the Closing Price against Time with a colorful palette
sns.lineplot(x=df.index, y=df['Close'], ax=ax, color='blue', linewidth=2)

# Set labels and title
ax.set_xlabel('Time', fontsize=12)
ax.set_ylabel('Closing Price', fontsize=12)
ax.set_title('Closing Price vs Time', fontsize=14)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Display the chart
st.pyplot(fig)

# Add a subheader and a colorful paragraph below the chart
st.markdown("<h3 style='color: yellow;'>Chart Explanation</h3>", unsafe_allow_html=True)
st.markdown("""
This line chart displays the Closing Price of an asset plotted against Time. The chart uses a blue color and a line width of 2 for the line. It helps visualize the price movement and fluctuations over the given period, allowing for analysis of trends and potential price changes.
""")

st.markdown("<h3 style='color: orange;'>Closing Price vs Time Chart With 100MA</h3>", unsafe_allow_html=True)

# Calculate the 100-day Moving Average
ma100 = df['Close'].rolling(100).mean()

# Set the size of the figure
fig, ax = plt.subplots(figsize=(12, 6))

# Plot the 100-day Moving Average with a colorful palette
sns.lineplot(x=df.index, y=ma100, ax=ax, color='blue', linewidth=2, label='100-day MA')

# Plot the Closing Price against Time with a colorful palette
sns.lineplot(x=df.index, y=df['Close'], ax=ax, color='orange', linewidth=2, label='Closing Price')

# Set labels and title
ax.set_xlabel('Time', fontsize=12)
ax.set_ylabel('Price', fontsize=12)
ax.set_title('Closing Price vs Time with 100MA', fontsize=14)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Display the chart
st.pyplot(fig)

# Add a colored subheader and a paragraph below the chart
st.markdown("<h3 style='color: yellow;'>Chart Explanation</h3>", unsafe_allow_html=True)
st.markdown("""
The Closing Price vs Time Chart with 100MA (Moving Average) is a graphical representation that displays the closing prices of an asset plotted against time. It includes a line representing the 100-day Moving Average (100MA). The Closing Price is plotted in orange, and the 100-day MA line is plotted in blue. This chart helps visualize the price movement over time and provides insights into the asset's long-term trend by smoothing out short-term fluctuations.
""")


st.markdown("<h3 style='color: orange;'>Closing Price vs Time Chart With 100MA & 200MA</h3>", unsafe_allow_html=True)

ma100 = df['Close'].rolling(100).mean()
ma200 = df['Close'].rolling(200).mean()

# Set the size of the figure
fig, ax = plt.subplots(figsize=(12, 6))

# Plot the 100-day Moving Average with a red color
ax.plot(ma100, color='red', label='100-day MA')

# Plot the 200-day Moving Average with a green color
ax.plot(ma200, color='green', label='200-day MA')

# Plot the Closing Price with a blue color
ax.plot(df['Close'], color='blue', label='Closing Price')

# Set labels and title
ax.set_xlabel('Time', fontsize=12)
ax.set_ylabel('Price', fontsize=12)
ax.set_title('Closing Price vs Time with 100MA & 200MA', fontsize=14)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Display the chart
st.pyplot(fig)

# Add a colored subheader and a paragraph below the chart
st.markdown("<h3 style='color: yellow;'>Chart Explanation</h3>", unsafe_allow_html=True)
st.markdown("""
The Closing Price vs Time Chart with 100MA and 200MA is a graphical representation that displays the closing prices of an asset plotted against time. It includes lines representing the 100-day Moving Average (100MA) and the 200-day Moving Average (200MA). The 100MA line is plotted in red, the 200MA line is plotted in green, and the Closing Price is plotted in blue. This chart helps visualize the long-term trend of the asset by smoothing out short-term fluctuations. The crossing of the 100MA and 200MA lines can provide signals for potential changes in the asset's trend.
""")

data_training=pd.DataFrame(df['Close'][0:int(len(df)*0.70)])
data_testing=pd.DataFrame(df['Close'][int(len(df)*0.70):int(len(df))])

from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler(feature_range=(0,1))

data_training_array=scaler.fit_transform(data_training)

# splitting data into x_trin & y_train



#load my model

model=load_model('keras_model.h5')

#testing part
past_100_days=data_training.tail(100)
final_df=past_100_days.append(data_testing,ignore_index=True)
input_data=scaler.fit_transform(final_df)

x_test=[]
y_test=[]
for i in range(100,input_data.shape[0]):
    x_test.append(input_data[i-100: i])
    y_test.append(input_data[i, 0])

x_test,y_test=np.array(x_test), np.array(y_test)
y_predicted=model.predict(x_test)

scalar=scaler.scale_

scale_factor=1/scalar[0]
y_predicted=y_predicted * scale_factor
y_test=y_test * scale_factor

# final graph
st.markdown("<h3 style='color: orange;'>Prediction vs Original</h3>", unsafe_allow_html=True)

fig2 = plt.figure(figsize=(12, 6))
plt.plot(y_test, color='blue', label='Original Price')
plt.plot(y_predicted, color='red', label='Predicted Price')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()

# Customize the colors of the grid lines
plt.grid(color='gray', linestyle='--', linewidth=0.5)

# Add a title to the plot
plt.title('Prediction vs Original Price')

# Display the chart
st.pyplot(fig2)

# Add a colored subheader and a paragraph below the chart
st.markdown("<h3 style='color: yellow;'>Chart Explanation</h3>", unsafe_allow_html=True)
st.markdown("""
The Prediction vs Original graph compares the predicted prices (in red) with the original prices (in blue) over time. It provides a visual representation of how well the prediction model performs in estimating the future prices. The x-axis represents time, while the y-axis represents the price. The graph helps assess the accuracy of the prediction model by comparing it with the actual values. The legend indicates which line represents the original prices and the predicted prices. By analyzing the chart, insights can be gained regarding the model's ability to forecast future price movements.
""")




st.markdown('<h1 style="color:blue;">Be Aware Of:</h1>', unsafe_allow_html=True)
st.markdown("""
It's important to note that no prediction method can guarantee accurate forecasts. Investors should consider these risks and conduct thorough research, diversify their portfolios, and consult with financial professionals before making investment decisions.
""")


st.markdown('<h1 style="color:red;">Stock Market Prediction Risks</h1>', unsafe_allow_html=True)

st.markdown("<h3 style='color: green;'>Market Volatility</h3>", unsafe_allow_html=True)
st.write("The stock market is known for its fluctuations and volatility. Prices can change rapidly due to various factors such as economic indicators, geopolitical events, and investor sentiment. Predicting these short-term price movements accurately can be challenging.")

st.markdown("<h3 style='color: green;'>Economic Factors</h3>", unsafe_allow_html=True)
st.write("Economic conditions play a significant role in stock market performance. Factors like interest rates, inflation, GDP growth, and government policies can impact stock prices. Accurately predicting how these factors will evolve in the future is complex and subject to uncertainty.")

st.markdown("<h3 style='color: green;'>External Event</h3>", unsafe_allow_html=True)
st.write("Unexpected events, such as natural disasters, political instability, or global crises, can have a significant impact on stock markets. These events can be challenging to predict and may lead to sudden price fluctuations.")

st.markdown("<h3 style='color: green;'>Company-Specific Risks</h3>", unsafe_allow_html=True)
st.write("Each company has its unique set of risks. Factors like management changes, competitive pressures, legal issues, or product failures can significantly affect stock prices. Analyzing and predicting company-specific risks require detailed research and analysis.")

st.markdown("<h3 style='color: green;'>Data Limitations</h3>", unsafe_allow_html=True)
st.write("Stock market prediction relies on historical data and statistical models. However, the quality and availability of data can vary, leading to potential inaccuracies in predictions. Additionally, unforeseen changes in market dynamics may render historical patterns less reliable.")

st.markdown("<h3 style='color: green;'>Behavioral Biases</h3>", unsafe_allow_html=True)
st.write("Investor behavior and emotions can influence stock market movements. Sentiment swings, irrational exuberance, or panic selling can lead to price distortions that are challenging to predict based on fundamentals alone.")

st.markdown("<h3 style='color: green;'>Model Limitation</h3>", unsafe_allow_html=True)
st.write("Stock market prediction models, including machine learning algorithms, have their limitations. They are based on historical patterns and assumptions, which may not always hold true in the future. Models can also be sensitive to input data, parameter choices, and overfitting issues.")