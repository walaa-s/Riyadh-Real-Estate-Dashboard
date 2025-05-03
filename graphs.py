import pandas as pd
import plotly.express as px
from config import Config

class CreateGraphs:
    @staticmethod
    def overview_table(df: pd.DataFrame) -> pd.DataFrame:
        return df.describe(include="all").T

    @staticmethod
    def distribution(df: pd.DataFrame):
        fig_price = px.histogram(
            df, x="baseRent", nbins=50,
            title="Distribution of Selling Price (SAR)",
            labels={"baseRent": "Price (SAR)", "count": "Count"}
        )
        fig_year = px.histogram(
            df, x="yearConstructed", nbins=df["yearConstructed"].nunique(),
            title="Distribution of Year Built",
            labels={"yearConstructed": "Year Constructed", "count": "Count"}
        )
        return fig_price, fig_year

    @staticmethod
    def trend_over_time(df: pd.DataFrame):
        agg = (
            df.groupby("date")[["baseRent", "totalRent"]]
              .median()
              .reset_index()
              .sort_values("date")
        )
        fig = px.line(
            agg, x="date", y=["baseRent", "totalRent"],
            title="Trend of Median Selling Price Over Time",
            labels={"value": "Price (SAR)", "variable": "Type"}
        )
        return fig, agg

    @staticmethod
    def by_type(df: pd.DataFrame):
        agg = (
            df.groupby("typeOfFlat")["baseRent"]
              .median()
              .reset_index()
              .sort_values("baseRent")
        )
        fig = px.bar(
            agg, x="typeOfFlat", y="baseRent",
            title="Median Selling Price by Property Type",
            labels={"typeOfFlat": "Property Type", "baseRent": "Price (SAR)"}
        )
        return fig, agg

    @staticmethod
    def feature_impact(df: pd.DataFrame):
        rows = []
        for feature in ("elevator", "furnished"):
            yes = df[df[feature]]["baseRent"].median()
            no  = df[~df[feature]]["baseRent"].median()
            rows.append({"Feature": feature, "Condition": "With",    "Price": yes})
            rows.append({"Feature": feature, "Condition": "Without", "Price": no})
        imp = pd.DataFrame(rows)
        fig = px.bar(
            imp, x="Feature", y="Price", color="Condition", barmode="group",
            title="Impact of Elevator & Furnished on Median Price",
            labels={"Price": "Price (SAR)"}
        )
        return fig, imp

    @staticmethod
    def create_map(df: pd.DataFrame):
        cfg = Config()
        agg = (
            df.groupby("region")["baseRent"]
              .median()
              .reset_index(name="MedianRent")
        )
        agg["CountOfProperties"] = df.groupby("region").size().values
        # apply coords
        agg["lat"] = agg["region"].map(lambda r: cfg.region_coords.get(r, (None, None))[0])
        agg["lon"] = agg["region"].map(lambda r: cfg.region_coords.get(r, (None, None))[1])
        fig = px.scatter_mapbox(
            agg, lat="lat", lon="lon",
            size="CountOfProperties", color="MedianRent",
            color_continuous_scale="Viridis", zoom=10,
            mapbox_style="carto-positron",
            hover_name="region",
            hover_data={"MedianRent": True, "CountOfProperties": True}
        )
        return fig, agg
