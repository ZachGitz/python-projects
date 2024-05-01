import requests


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"



stock_params = {
    "function" :"TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": "TEO62KFLKZB5VB44"
}

news_params = {
    "apiKey":"b9a66afd63d040dfb5e79b434c9d72e9",
    "qInTitle": COMPANY_NAME
}

data = requests.get(STOCK_ENDPOINT, params=stock_params).json()["Time Series (Daily)"]

list_s = [value for (key,value) in data.items()]

stock_close_last =float(list_s[1]["4. close"])
stock_close_today=float(list_s[0]["4. close"])
diff_in_price = abs(stock_close_last - stock_close_today)


    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

diff_perc =  round((diff_in_price/stock_close_last)*100,2)





if(diff_perc>=5):
    articles = requests.get(NEWS_ENDPOINT,params=news_params).json()["articles"]
    three_articles = articles[:3]
    new_list = [f"Headline:{i['title']}\n Brief: {i['description']}" for i in three_articles]
    print(new_list)





    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 



#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

