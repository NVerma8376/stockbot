from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.interpolate import make_interp_spline

# Replace 'YOUR_API_KEY' with your actual Alpha Vantage API key
API_KEY = '1I1QYECE05PE3PA7'

def stock_bot(symbol):
    ts = TimeSeries(key=API_KEY, output_format='pandas')
    
    # Fetch intraday stock data
    data, meta_data = ts.get_intraday(symbol=symbol, interval='1min', outputsize='full')
    
    print(meta_data)
    print(data.head())

    # Create plot
    plt.figure(figsize=(12,6))

    # Get x and y values
    x = np.arange(len(data))
    y = data['4. close'].values

    # Convert minutes to days
    x_days = x / (60 * 24)  # 60 minutes per hour, 24 hours per day
    
    # Create interpolated spline
    X_Y_Spline = make_interp_spline(x_days, y)
    
    # Generate evenly spaced x values
    X_ = np.linspace(x_days.min(), x_days.max(), 300)
    
    # Generate corresponding y values
    Y_ = X_Y_Spline(X_)
    
    # Plot the smooth curve
    plt.plot(X_, Y_, label='Close Price')
    
    # Plot original data points
    plt.scatter(x_days, y, color='red', alpha=0.5, label='Original Data Points')
    
    # Add title and labels
    plt.title(f'{symbol} Stock Price - Last {round(x_days.max())} days')
    plt.xlabel('Days')
    plt.ylabel('Price ($)')
    plt.legend(loc='upper left')
    
    # Show gridlines
    plt.grid(True)
    
    # Display the plot
    plt.show()

if __name__ == "__main__":
    symbol = input("Enter stock symbol: ")
    stock_bot(symbol)
