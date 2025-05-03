import pandas as pd
from datetime import datetime
from config import Config

class ProcessData:
    def __init__(self, path: str = "riyadh_apartments_updated.csv"):
        self.path = path
        self.config = Config()

    def get_clean_data(self) -> pd.DataFrame:
        df = pd.read_csv(self.path)

        # Prices
        df["baseRent"]  = (df["Selling Price (SAR)"]
                            .astype(str)
                            .str.replace(",", "")
                            .astype(float))
        df["totalRent"] = df["baseRent"]

        # Dates
        df["date"] = pd.to_datetime(df["random_date"], errors="coerce")

        # Numeric features
        df["livingSpace"] = pd.to_numeric(df["Area (sqm)"], errors="coerce")
        df["noRooms"]     = pd.to_numeric(df["Bedrooms"], errors="coerce").astype("Int64")

        # Year constructed
        df["Property Age (years)"] = pd.to_numeric(df["Property Age (years)"], errors="coerce")
        df["yearConstructed"] = datetime.now().year - df["Property Age (years)"]

        # Categoricals
        df["region"]     = df["Region"].astype(str)
        df["typeOfFlat"] = df["Property Type"].astype(str)

        # Boolean flags
        df["elevator"]  = df["Elevator"].astype(str).str.lower().eq("yes")
        df["furnished"] = df["Furnished"].astype(str).str.lower().eq("yes")

        # Drop rows missing core fields
        df = df.dropna(subset=["date", "baseRent", "region"])
        return df
