"""
This function creates future dates with an hour as an additional column.
"""

def futureData(days=365):
    import pandas as pd
    from datetime import datetime,date,timedelta
    today_date=str(date.today())
    future_date=str(date.today()+timedelta(days))
    df = pd.DataFrame(
            {'dy': pd.date_range(today_date, future_date, freq='1H', closed='left')}
         )
    df["hour"]=pd.to_datetime(df.dy).dt.hour
    df["dy"]=pd.to_datetime(df.dy).dt.date
    return df
future=futureData(days=5)
future
