from smartapi import SmartConnect, SmartWebSocket
import document_detail_Lax
import time
import datetime
import pandas as pd

api_key = document_detail_Lax.api_key
secret_key = document_detail_Lax.secret_key
user_id = document_detail_Lax.user_id
password = document_detail_Lax.password

script_list = {
	"MARUTI-EQ": "10999",
	"LALPATHLAB-EQ": "11654",
	"IDFCFIRSTB-EQ": "11184",
	"CONCOR-EQ": "4749",
	"PEL-EQ": "2412",
	"MUTHOOTFIN-EQ": "23650",
	"ESCORTS-EQ": "958",
	"PIDILITIND-EQ": "2664",
	"JSWSTEEL-EQ": "11723",
	"ACC-EQ": "22",
	"SAIL-EQ": "2963",
	"ICICIPRULI-EQ": "18652",
	"GRASIM-EQ": "1232",
	"ASTRAL-EQ": "14418",
	"BHARATFORG-EQ": "422",
	"ATUL-EQ": "263",
	"IPCALAB-EQ": "1633",
	"BEL-EQ": "383",
	"PNB-EQ": "10666",
	"HDFCLIFE-EQ": "467",
	"NATIONALUM-EQ": "6364",
	"DELTACORP-EQ": "15044",
	"UPL-EQ": "11287",
	"APOLLOHOSP-EQ": "157",
	"CIPLA-EQ": "694",
	"WHIRLPOOL-EQ": "18011",
	"DALBHARAT-EQ": "8075",
	"INFY-EQ": "1594",
	"FEDERALBNK-EQ": "1023",
	"ALKEM-EQ": "11703",
	"AMBUJACEM-EQ": "1270",
	"TITAN-EQ": "3506",
	"OBEROIRLTY-EQ": "20242",
	"CUMMINSIND-EQ": "1901",
	"NMDC-EQ": "15332",
	"SUNPHARMA-EQ": "3351",
	"ADANIENT-EQ": "25",
	"LTTS-EQ": "18564",
	"PIIND-EQ": "24184",
	"CHOLAFIN-EQ": "685",
	"BHEL-EQ": "438",
	"MFSL-EQ": "2142",
	"M&MFIN-EQ": "13285",
	"LUPIN-EQ": "10440",
	"GUJGASLTD-EQ": "10599",
	"SUNTV-EQ": "13404",
	"ICICIGI-EQ": "21770",
	"STAR-EQ": "7374",
	"PVR-EQ": "13147",
	"GRANULES-EQ": "11872",
	"MCX-EQ": "31181",
	"INDHOTEL-EQ": "1512",
	"SBICARD-EQ": "17971",
	"M&M-EQ": "2031",
	"PFIZER-EQ": "2643",
	"INDUSTOWER-EQ": "29135",
	"VEDL-EQ": "3063",
	"BALKRISIND-EQ": "335",
	"SIEMENS-EQ": "3150",
	"HAVELLS-EQ": "9819",
	"DRREDDY-EQ": "881",
	"BERGEPAINT-EQ": "404",
	"IOC-EQ": "1624",
	"LT-EQ": "11483",
	"BANKBARODA-EQ": "4668",
	"DABUR-EQ": "772",
	"LAURUSLABS-EQ": "19234",
	"FSL-EQ": "14304",
	"TORNTPOWER-EQ": "13786",
	"GMRINFRA-EQ": "13528",
	"MARICO-EQ": "4067",
	"INDIACEM-EQ": "1515",
	"EICHERMOT-EQ": "910",
	"BANDHANBNK-EQ": "2263",
	"GODREJPROP-EQ": "17875",
	"BHARTIARTL-EQ": "10604",
	"BPCL-EQ": "526",
	"NAUKRI-EQ": "13751",
	"HINDALCO-EQ": "1363",
	"ITC-EQ": "1660",
	"POLYCAB-EQ": "9590",
	"CADILAHC-EQ": "7929",
	"SBILIFE-EQ": "21808",
	"DIXON-EQ": "21690",
	"HEROMOTOCO-EQ": "1348",
	"TATAPOWER-EQ": "3426",
	"ICICIBANK-EQ": "4963",
	"SBIN-EQ": "3045",
	"HINDPETRO-EQ": "1406",
	"POWERGRID-EQ": "14977",
	"ABFRL-EQ": "30108",
	"LICHSGFIN-EQ": "1997",
	"TRENT-EQ": "1964",
	"TVSMOTOR-EQ": "8479",
	"DIVISLAB-EQ": "10940",
	"GODREJCP-EQ": "10099",
	"GAIL-EQ": "4717",
	"MINDTREE-EQ": "14356",
	"BAJAJFINSV-EQ": "16675",
	"VOLTAS-EQ": "3718",
	"APLLTD-EQ": "25328",
	"DEEPAKNTR-EQ": "19943",
	"TATACONSUM-EQ": "3432",
	"HINDUNILVR-EQ": "1394",
	"ULTRACEMCO-EQ": "11532",
	"ASIANPAINT-EQ": "236",
	"CANBK-EQ": "10794",
	"EXIDEIND-EQ": "676",
	"IEX-EQ": "220",
	"JUBLFOOD-EQ": "18096",
	"CHAMBLFERT-EQ": "637",
	"HDFC-EQ": "1330",
	"WIPRO-EQ": "3787",
	"L&TFH-EQ": "24948",
	"MOTHERSUMI-EQ": "4204",
	"INDUSINDBK-EQ": "5258",
	"COLPAL-EQ": "15141",
	"CANFINHOME-EQ": "583",
	"HDFCAMC-EQ": "4244",
	"NTPC-EQ": "11630",
	"HAL-EQ": "2303",
	"UBL-EQ": "16713",
	"SRF-EQ": "3273",
	"BRITANNIA-EQ": "547",
	"NESTLEIND-EQ": "17963",
	"TATAMOTORS-EQ": "3456",
	"BAJFINANCE-EQ": "317",
	"OFSS-EQ": "10738",
	"JKCEMENT-EQ": "13270",
	"TORNTPHARM-EQ": "3518",
	"INDIGO-EQ": "11195",
	"PFC-EQ": "14299",
	"PAGEIND-EQ": "14413",
	"CUB-EQ": "5701",
	"MANAPPURAM-EQ": "19061",
	"LTI-EQ": "17818",
	"AUBANK-EQ": "21238",
	"MRF-EQ": "2277",
	"COFORGE-EQ": "11543",
	"METROPOLIS-EQ": "9581",
	"TATACHEM-EQ": "3405",
	"BOSCHLTD-EQ": "2181",
	"IBULHSGFIN-EQ": "30125",
	"RAMCOCEM-EQ": "2043",
	"ZEEL-EQ": "3812",
	"SYNGENE-EQ": "10243",
	"RECLTD-EQ": "15355",
	"TATASTEEL-EQ": "3499",
	"COROMANDEL-EQ": "739",
	"CROMPTON-EQ": "17094",
	"AUROPHARMA-EQ": "275",
	"AXISBANK-EQ": "5900",
	"RBLBANK-EQ": "18391",
	"PETRONET-EQ": "11351",
	"JINDALSTEL-EQ": "6733",
	"GLENMARK-EQ": "7406",
	"KOTAKBANK-EQ": "1922",
	"GSPL-EQ": "13197",
	"ADANIPORTS-EQ": "15083",
	"COALINDIA-EQ": "20374",
	"AMARAJABAT-EQ": "100",
	"TCS-EQ": "11536",
	"ONGC-EQ": "2475",
	"APOLLOTYRE-EQ": "163",
	"BIOCON-EQ": "11373",
	"PERSISTENT-EQ": "18365",
	"DLF-EQ": "14732",
	"SRTRANSFIN-EQ": "4306",
	"MPHASIS-EQ": "4503",
	"NAVINFLUOR-EQ": "14672",
	"INDIAMART-EQ": "10726",
	"MGL-EQ": "17534",
	"IRCTC-EQ": "13611",
	"IGL-EQ": "11262",
	"BSOFT-EQ": "6994",
	"BATAINDIA-EQ": "371",
	"HCLTECH-EQ": "7229",
	"SHREECEM-EQ": "3103",
	"RELIANCE-EQ": "2885",
	"HDFCBANK-EQ": "1333",
	"TECHM-EQ": "13538",
	"ASHOKLEY-EQ": "212"
}

exchange = "NSE"
per_trade_fund = 10000
open_position = {}
close_position = []
ohlc = {}

def closingPosition(script, token, price):
	open_position_type = open_position[script]["order"]
	quantity = open_position[script]["quantity"]
	close_position.append(script)
	if open_position_type == "BUY":
		orderparams = {
			"variety": "NORMAL",
			"tradingsymbol": script,
			"symboltoken": token,
			"transactiontype": "SELL",
			"exchange": exchange,
			"ordertype": "LIMIT",
			"producttype": "INTRADAY",
			"duration": "DAY",
			"price": price,
			"squareoff": "0",
			"stoploss": "0",
			"quantity": quantity
		}
		orderId = obj.placeOrder(orderparams)
		print(f"Position closed for {script}, at Price: {price} for Quantity: {quantity}, with order_id: {orderId} at time: {datetime.datetime.now()}")
	else:
		orderparams = {
			"variety": "NORMAL",
			"tradingsymbol": script,
			"symboltoken": token,
			"transactiontype": "BUY",
			"exchange": exchange,
			"ordertype": "LIMIT",
			"producttype": "INTRADAY",
			"duration": "DAY",
			"price": price,
			"squareoff": "0",
			"stoploss": "0",
			"quantity": quantity
		}
		orderId = obj.placeOrder(orderparams)
		print(f"Position closed for {script}, at Price: {price} for Quantity: {quantity}, with order_id: {orderId} at time: {datetime.datetime.now()}")

def positionManagement(script, token, price):
	open_position_type = open_position[script]["order"]
	target = open_position[script]["target"]
	stoploss = open_position[script]["stoploss"]
	quantity = open_position[script]["quantity"]

	if (ltp == target) | (ltp == stoploss):
		close_position.append(script)
		if open_position_type == "BUY":
			orderparams = {
				"variety": "NORMAL",
				"tradingsymbol": script,
				"symboltoken": token,
				"transactiontype": "SELL",
				"exchange": exchange,
				"ordertype": "LIMIT",
				"producttype": "INTRADAY",
				"duration": "DAY",
				"price": price,
				"squareoff": "0",
				"stoploss": "0",
				"quantity": quantity
			}
			orderId = obj.placeOrder(orderparams)
			print(f"Position closed for {script}, at Price: {price} for Quantity: {quantity}, with order_id: {orderId} at time: {datetime.datetime.now()}")
		else:
			orderparams = {
				"variety": "NORMAL",
				"tradingsymbol": script,
				"symboltoken": token,
				"transactiontype": "BUY",
				"exchange": exchange,
				"ordertype": "LIMIT",
				"producttype": "INTRADAY",
				"duration": "DAY",
				"price": price,
				"squareoff": "0",
				"stoploss": "0",
				"quantity": quantity
			}
			orderId = obj.placeOrder(orderparams)
			print(f"Position closed for {script}, at Price: {price} for Quantity: {quantity}, with order_id: {orderId} at time: {datetime.datetime.now()}")
	else:
		pass

def placeOrder(order, script, token, price):
	quantity = int(per_trade_fund/price)
	buy_order_target = round(price*1.01, 1)
	buy_order_stoploss = round(price*0.99, 1)
	sell_order_target = round(price*0.99, 1)
	sell_order_stoploss = round(price*1.01, 1)

	if order == "BUY":
		open_position[script] = {
		"order" : order,
		"price" : price,
		"quantity" : quantity,
		"target" : buy_order_target,
		"stoploss" : buy_order_stoploss
		}

	else:
		open_position[script] = {
		"order" : order,
		"price" : price,
		"quantity" : quantity,
		"target" : sell_order_target,
		"stoploss" : sell_order_stoploss
		}

	orderparams = {
		"variety": "NORMAL",
		"tradingsymbol": script,
		"symboltoken": token,
		"transactiontype": order,
		"exchange": exchange,
		"ordertype": "LIMIT",
		"producttype": "INTRADAY",
		"duration": "DAY",
		"price": price,
		"squareoff": "0",
		"stoploss": "0",
		"quantity": quantity
	}
	orderId = obj.placeOrder(orderparams)
	print(f"{order} Order Placed for {script}, at Price: {price} for Quantity: {quantity}, with order_id: {orderId} at time: {datetime.datetime.now()}")

def getData(token, ltp):
	for i, j in script_list.items():        
		if (j == token) and (i not in ohlc):
			LTP = obj.ltpData(exchange, i, j)
			high = LTP["data"]["high"]
			low = LTP["data"]["low"]
			openx = LTP["data"]["open"]
			ohlc[i] = {
				"high" : high,
				"low" : low,
				"openx" : openx,
			}
			return i, high, low, openx
		
		if (j == token) and (i in ohlc):
			if float(ltp) >= ohlc[i]["high"]:
				ohlc[i]["high"] = float(ltp)
			if float(ltp) <= ohlc[i]["low"]:
				ohlc[i]["low"] =  float(ltp)
			return i, ohlc[i]["high"], ohlc[i]["low"], ohlc[i]["openx"]

def sendData(message):
	print(message)
	ltp = message[0]["ltp"]
	token = message[0]["tk"]
	script, high, low, openx = getData(token, ltp)
	volume = message[0]["v"]
	ltt = message[0]["ltt"]

	if (ltp == high) and (script not in open_position):
		placeOrder("BUY", script, token, ltp)

	if (ltp == low) and (script not in open_position):
		placeOrder("SELL", script, token, ltp)

	if (script in open_position) and (script not in close_position) and (ltt[-8:] < "13:30:00"):
		positionManagement(script, token, ltp)

	if (script in open_position) and (script not in close_position) and (ltt[-8:] == "13:30:00"):
		closingPosition(script, token, ltp)


def socketOpen(task, token, feedToken, user_id):
	ss = SmartWebSocket(feedToken, user_id)

	def on_message(ws, message):
		# sendData(message)
		print(message)

	def on_open(ws):
		ss.subscribe(task, token)

	def on_error(ws, error):
		print(error)

	def on_close(ws):
		print("Close")

	ss._on_open = on_open
	ss._on_message = on_message
	ss._on_error = on_error
	ss._on_close = on_close

	ss.connect()

def main():
	global obj

	obj = SmartConnect(api_key=api_key)
	token = obj.generateToken(
		obj.generateSession(user_id, password)["data"]["refreshToken"])
	jwtToken = token['data']["jwtToken"]
	refreshToken = token['data']['refreshToken']
	feedToken = token['data']['feedToken']

	empty = []
	for i, j in script_list.items():
		empty.append(f"nse_cm|{j}&")
	newS = "".join([i for i in empty])
	token = newS[:-1]
	task = "mw"

	socketOpen(task, token, feedToken, user_id)

if (__name__ == '__main__'):
	main()