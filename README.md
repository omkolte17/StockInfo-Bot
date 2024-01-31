# StocksInfo-Bot
This bot provides the live price of Indian stocks listed on NSE and BSE.
Previously it was used by a community of over 2000 people on Telegram.

## Features
 - Live price of stocks listed on NSE and BSE.
 - Top 10 investors of the stock.
 
## Variables

update the bot.py file to add the following data.

`API_HASH` - Telegram API HASH.

`API_ID` - Telegram API ID.

`BOT_TOKEN` - Bot Token. Get from Bot Father.

## Commands
`/start` - Check if the bot is running.

`/help` - Get help.

`/getval` - Get the live price. `/getval tickername`

`/getholders` - Get the top 10 investors. `/getholders tickername`

Note: It will throw error if tickername is not provided.

Tickername is the code name of the stock. For example for SBI commands will be as follows:
 - `/getval SBIN`
 - `/getholders SBIN`

### ~~Try the bot at [@stonks02_bot](https://t.me/stonks02_bot)~~
