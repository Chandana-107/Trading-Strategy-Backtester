import yfinance as yf
import time

def download_data(ticker, start_date, end_date, retries=5):
    """
    Downloads stock data with automatic retry and timeout handling.
    """

    for attempt in range(1, retries + 1):
        try:
            print(f"Downloading data for {ticker} (Attempt {attempt}/{retries})...")

            data = yf.download(
                ticker,
                start=start_date,
                end=end_date,
                timeout=30,         # <-- prevents curl timeout
                progress=False
            )

            # Check if data returned properly
            if not data.empty:
                print("✔ Data successfully downloaded.\n")
                return data.reset_index()

            print("⚠ Empty response, retrying...")

        except Exception as e:
            print(f"⚠ Error occurred: {e}")
        
        time.sleep(3)  # wait before retry

    print("❌ Failed to download data after multiple attempts.\n")
    return None
