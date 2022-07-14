from telethon import events, TelegramClient
from yahoo_fin import stock_info as si
import traceback

# Initialize TelegramClient
API_ID = "API_ID HERE"      # remove the quotes for API_ID
API_HASH = "API_HASH HERE"
start_msg = "STONKS! \nPress /help for more info"
command_msg = "Commands: \n\t\t/getval - Returns Current Price \n\t\t/getholders - Returns Major Holders"

client = TelegramClient('stocksinfo', API_ID, API_HASH).start(bot_token='bot_token here')


# Handlers
@client.on(events.NewMessage(pattern="/start"))
async def handle_start(e):
    await e.reply(start_msg)


@client.on(events.NewMessage(pattern="/help"))
async def handle_help(e):
    await e.reply(command_msg)


@client.on(events.NewMessage(pattern="/getval"))
async def handle_getval(e):
    ticker = e.raw_text+".NS"
    ticker = ticker.split(" ")[1]
    price = None
    try:
        price = si.get_live_price(ticker)
        await e.reply("Current Price: {:.2f}".format(price))
    except:
        await e.reply("Enter valid ticker.")
        traceback.print_exc()


@client.on(events.NewMessage(pattern="/getholders"))
async def handle_getholders(e):
    ticker = e.raw_text+".NS"
    ticker = ticker.split(" ")[1]
    holdings = None
    try:
        holdings = si.get_holders(ticker)
        await e.reply("Major Holders of {} are as follow:\n".format(ticker)
                      + str(holdings['Direct Holders (Forms 3 and 4)']
                            ['Holder']))
    except:
        await e.reply("Enter valid ticker.")

# Start Client

with client:
    print("Bot Started")
    client.run_until_disconnected()
