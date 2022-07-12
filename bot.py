from telethon import events, TelegramClient
from yahoo_fin import stock_info as si

# Initialize TelegramClient
API_ID = "API ID HERE"
API_HASH = "API HASH HERE"

client = TelegramClient('stocksinfo', API_ID, API_HASH).start(
    bot_token='bot token here')

# Handlers


@client.on(events.NewMessage(pattern="/start"))
async def handle_start(e):
    await e.reply("STONKS\n"+"Press /help for more information.")


@client.on(events.NewMessage(pattern="/help"))
async def handle_help(e):
    await e.reply("Commands:\nGet Current Price - /getval <tickername>\n" +
                  "Get Major Holders - /getholders")


@client.on(events.NewMessage(pattern="/getval"))
async def handle_getval(e):
    tickerPrice = e.raw_text+".NS"
    tickerPrice = tickerPrice.split(" ")
    tickerPrice = tickerPrice[1]
    price = None
    try:
        price = si.get_live_price(tickerPrice)
        await e.reply("Current Price: {:.2f}".format(price))
    except:
        await e.reply("Enter valid ticker.")
        print("/getval error")


@client.on(events.NewMessage(pattern="/getholders"))
async def handle_getholders(e):
    tickerHoldings = e.raw_text+".NS"
    tickerHoldings = tickerHoldings.split(" ")
    tickerHoldings = tickerHoldings[1]
    holdings = None
    try:
        holdings = si.get_holders(tickerHoldings)
        await e.reply("Major Holders of {} are as follow:\n".format(tickerHoldings)
                      + str(holdings['Direct Holders (Forms 3 and 4)']
                            ['Holder']))
    except:
        await e.reply("Enter valid ticker.")
        print("/getholders error")

# Start Client

with client:
    print("Bot Started")
    client.run_until_disconnected()
