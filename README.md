# Cryptocurrency Price Monitoring System

## Project Overview

This project is a Python-based system designed to monitor the price of cryptocurrencies and send SMS alerts when significant price changes occur. 
It utilizes the Dex Screener API for real-time price data and Twilio's API for sending SMS notifications. I am tracking a particular meme token but you can edit the API call to track any token you like, or even multiple tokens. You could even edit this to track stock prices and be notified via text by changing the API. 

## Features

- **Real-Time Price Monitoring**: Fetches the latest cryptocurrency prices from the Dex Screener API.
- **SMS Alerts**: Sends an SMS through Twilio when the price crosses predefined thresholds.
- **Dynamic Thresholds**: Thresholds adjust dynamically based on recent price changes to ensure relevant notifications.

## Technologies Used

- Python 3.x
- Twilio API
- Dex Screener API
- Requests library
- Time library

## Setup and Installation

### Prerequisites

- Python 3.6 or above
- Twilio account with an SMS-capable phone number
- API key for the Dex Screener

### Installing Dependencies

Install the required Python packages using pip:

```bash
pip install requests twilio
