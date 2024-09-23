from Auto_Trader import pd, time
import Auto_Trader

def buy_or_sell(df, row, holdings):
    """
    Determine whether to sell based on Stop Loss of -5%
    """
    holdings = pd.DataFrame(holdings)[["tradingsymbol", "instrument_token", "exchange", "average_price", "quantity"]]
    try:
        # Filter holdings for the specific instrument token
        holdings_symbol_data = holdings[holdings["instrument_token"] == row["instrument_token"]]
        # Ensure there's data for the symbol
        if holdings_symbol_data.empty:
            # print(f"No holdings found for {row['instrument_token']}")
            return
        
        # Extract average price from the holdings
        average_price = holdings_symbol_data['average_price'].iloc[-1]
        
        # Extract last closing price from the dataframe
        last_price = df['Close'].iloc[-1]
        
        # Avoid divide-by-zero error
        if average_price == 0:
            print(f"Error: Average price is zero for {holdings_symbol_data['tradingsymbol'].iloc[-1]}")
            return
        
        # Calculate profit percentage
        profit_percent = ((last_price - average_price) / average_price) * 100
        
        if profit_percent <= -5.0:
            return "SELL"
        else:
            return "HOLD"
        
    
    except Exception as e:
        print(f"Error processing {row['instrument_token']}: {str(e)}")
