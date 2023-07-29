# Automated TimeSeries Predictor

AutoTimeSeries Predictor is a web-based application, built with Streamlit and Python, that provides tools for conducting Exploratory Data Analysis (EDA), fetching live stock data and performing time series predictions on the uploaded or fetched datasets.

## Features

* Upload: This feature allows the user to upload a dataset in CSV format or fetch live stock data using the stock symbol. The fetched/loaded data is displayed in a tabular format.

* Analytics: This feature provides automated Exploratory Data Analysis (EDA) on the uploaded dataset or live fetched stock data. The user can choose to visualize a particular numeric column over time. Additionally, the user gets a comprehensive report using the YData's Profiling package which gives insights about the dataset.

* Predict: This feature allows the user to perform time series forecasting on the chosen numeric column. The user can define the number of days to forecast. The output is displayed in both a table and a line graph.

## Getting Started

### Prerequisites
Python 3.6 or higher
Streamlit
Pandas
Prophet (for time series forecasting)
Plotly (for visualization)
yfinance (for fetching live stock data)
ydata_profiling (for automated EDA)
streamlit_pandas_profiling (for integrating pandas profiling with streamlit)

### Installing
To install the required packages, run the following command:

``` bash
pip install streamlit pandas prophet plotly yfinance ydata_profiling streamlit_pandas_profiling
```
### Running the application
Navigate to the directory where the app.py is located and run the following command:

``` bash
streamlit run main.py
```
### Usage

1. After running the script, a new window will open in your default web browser with the Streamlit application interface.

2. There is a sidebar with three choices: Upload, Analytics and Predict.

3. Upload: You can either upload your own TimeSeries dataset in CSV format or you can fetch live stock data by providing the stock symbol (e.g., AAPL for Apple Inc.) and a date range.

4. Analytics: Here, you can select a numeric column to plot over time. Also, a comprehensive automated EDA report is displayed.

5. Predict: Select a numeric column for forecasting, enter the number of days to forecast and click on Generate Forecast to get the prediction for the selected number of days.
