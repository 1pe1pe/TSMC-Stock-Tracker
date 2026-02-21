import yfinance as yf
from datetime import datetime

def get_tsmc_data():
    print("--- 晨間台積電 (TSMC) 數據彙整 ---")
    print(f"日期: {datetime.now().strftime('%Y-%m-%d')}\n")

    # 1. 抓取台積電 (2330.TW) 前一日收盤價
    try:
        tsmc_tw = yf.Ticker("2330.TW")
        hist_tw = tsmc_tw.history(period="1d")
        if not hist_tw.empty:
            close_price_tw = hist_tw['Close'].iloc[0]
            print(f"📍 台積電 (2330.TW) 收盤價: {close_price_tw:.2f} 元")
    except Exception as e:
        print("無法取得台積電股價資料")

    # 2. 抓取台積電美股 ADR (TSM) 前一日收盤價
    try:
        tsmc_adr = yf.Ticker("TSM")
        hist_adr = tsmc_adr.history(period="1d")
        if not hist_adr.empty:
            close_price_adr = hist_adr['Close'].iloc[0]
            print(f"📍 台積電 ADR (TSM) 收盤價: {close_price_adr:.2f} 美元")
    except Exception as e:
         print("無法取得 ADR 股價資料")

    # 3. 籌碼面預留區塊 (未來進階擴充)
    print("\n📍 法人與主力籌碼動態:")
    print("- 外資買賣超張數: (等待串接證交所資料...)")
    print("- 散戶融資餘額: (等待串接證交所資料...)")
    print("\n💡 提醒：綜合評估各項數據後，再決定今日是否買進喔！")

if __name__ == "__main__":
    get_tsmc_data()
