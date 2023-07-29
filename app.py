import streamlit as st
import pandas as pd
import os
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import plotly.express as px
from prophet import Prophet
import yfinance as yf


def get_live_stock_data(symbol, start_date, end_date):
    df = yf.download(symbol, start=start_date, end=end_date)
    return df.reset_index()

with st.sidebar:
    st.title("AutoTimeSeries Predictor")
    choice = st.radio("Navigation", ["Upload", "Analytics", "Predict"])

if choice == "Upload":
    st.title("TimeSeries Dataset for Predictions")
    data_source = st.radio("Data Source", ["CSV File", "Live Stock Data"])

    if data_source == "CSV File":
        file = st.file_uploader("Upload TimeSeries Dataset Here (CSV)")
        if file:
            data = pd.read_csv(file, index_col=None)
            data.to_csv("inputdata.csv", index=None)
            st.dataframe(data)

    elif data_source == "Live Stock Data":
        st.write("Enter a stock symbol and date range to fetch live stock data.")
        symbol = st.text_input("Stock Symbol (e.g., AAPL for Apple Inc.)")
        start_date = st.date_input("Start Date")
        end_date = st.date_input("End Date", pd.to_datetime('today'))

        if st.button("Fetch Live Stock Data"):
            try:
                data = get_live_stock_data(symbol, start_date, end_date)
                st.dataframe(data)
                data.to_csv("inputdata.csv", index=None)
                st.success(f"Live stock data for {symbol} fetched successfully.")               

                    
            except Exception as e:
                st.error(f"Error fetching live stock data: {str(e)}")

if os.path.exists("inputdata.csv"):
    data = pd.read_csv("inputdata.csv", index_col=None)

if choice == "Analytics":
    st.title("AutoEDA")

    numeric_columns = data.select_dtypes(include=['int64', 'float64']).columns.tolist()
    if not numeric_columns:
        st.error("No numeric columns found in the dataset. Please ensure your dataset has numeric columns to plot.")
    else:
        selected_column = st.selectbox('Select a numeric column to plot:', numeric_columns)
        fig = px.line(data, x='Date', y=selected_column, title='Stock Price')
        fig.update_xaxes(title_text="Date")
        fig.update_yaxes(title_text=selected_column)
        st.plotly_chart(fig)

    profile = ProfileReport(data, title="Analytics Report")
    st_profile_report(profile)

if choice == "Predict":
    st.title("Time Series Forecasting")

    numeric_columns = data.select_dtypes(include=['int64', 'float64']).columns.tolist()
    selected_column = st.selectbox('Select a numeric column for forecasting:', numeric_columns)

    forecast_days = st.number_input("Enter the number of days to forecast:", min_value=1, value=30, step=1)

    if st.button("Generate Forecast"):
        df_prophet = data.rename(columns={'Date': 'ds', selected_column: 'y'})
        df_prophet['ds'] = pd.to_datetime(df_prophet['ds'])

        model = Prophet()
        model.fit(df_prophet)

        future = model.make_future_dataframe(periods=forecast_days)

        forecast = model.predict(future)

        st.subheader(f"Forecast for {forecast_days} days")
        forecast_df = forecast[['ds', 'yhat']].tail(forecast_days + 1)
        forecast_df = forecast_df.rename(columns={'ds': 'Date', 'yhat': 'Predictions'})
        st.dataframe(forecast_df, hide_index=True)
        fig = px.line(data, x=forecast_df["Date"], y=forecast_df["Predictions"], title='Stock Price Prediction')
        fig.update_xaxes(title_text="Date")
        fig.update_yaxes(title_text="Predictions")
        st.plotly_chart(fig)