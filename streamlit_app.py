import streamlit as st
import pandas as pd
import plotly.express as px
import pydeck as pdk

# Load data
df = pd.read_csv("riyadh_apartments_cleaned.csv")
df['date'] = pd.to_datetime(df['date'])
df['price_per_sqm'] = df['price_sar'] / df['area_sqm']

# Sidebar filters
st.sidebar.header("Filter Listings")
selected_region = st.sidebar.multiselect(
    "Region (Direction)", options=sorted(df['region'].unique()), default=None)
price_range = st.sidebar.slider("Price Range (SAR)", int(df['price_sar'].min()), int(df['price_sar'].max()), (int(df['price_sar'].min()), int(df['price_sar'].max())))
bedroom_filter = st.sidebar.multiselect("Bedrooms", sorted(df['bedrooms'].unique()), default=None)
furnished_filter = st.sidebar.multiselect("Furnished", df['furnished'].unique(), default=None)

# Filtered Data
filtered_df = df[
    (df['price_sar'] >= price_range[0]) &
    (df['price_sar'] <= price_range[1])
]
if selected_region:
    filtered_df = filtered_df[filtered_df['region'].isin(selected_region)]
if bedroom_filter:
    filtered_df = filtered_df[filtered_df['bedrooms'].isin(bedroom_filter)]
if furnished_filter:
    filtered_df = filtered_df[filtered_df['furnished'].isin(furnished_filter)]

# KPIs
avg_price = round(filtered_df['price_sar'].mean(), 2)
avg_price_sqm = round(filtered_df['price_per_sqm'].mean(), 2)
total_listings = filtered_df.shape[0]
most_common_neigh = filtered_df['Neighborhood_clean'].mode()[0] if not filtered_df.empty else "N/A"

st.title("🏡 Riyadh Apartments Market Dashboard")

# KPI Cards
col1, col2, col3, col4 = st.columns(4)
col1.metric("Avg. Price (SAR)", f"{avg_price:,.0f}")
col2.metric("Avg. Price/m²", f"{avg_price_sqm:,.0f}")
col3.metric("Total Listings", total_listings)
col4.metric("Top Neighborhood", most_common_neigh)

# Map Visualization using Plotly (no token needed)
st.subheader("📍 Apartment Locations Map")
st.plotly_chart(
    px.scatter_mapbox(
        filtered_df,
        lat="latitude",
        lon="longitude",
        color="price_sar",
        size="price_sar",
        hover_name="Neighborhood_clean",
        hover_data=["region", "area_sqm", "bedrooms", "price_sar"],
        zoom=10,
        height=500,
        mapbox_style="open-street-map"
    )
)

# Price Distribution
st.subheader("📊 Price Distribution")
st.plotly_chart(px.histogram(filtered_df, x="price_sar", nbins=50, title="Distribution of Apartment Prices"))

# Region and Neighborhood Comparison
st.subheader("🏙️ Avg. Price by Region and Neighborhood")
region_neigh_price = filtered_df.groupby(["region", "Neighborhood_clean"])["price_sar"].mean().reset_index()
st.plotly_chart(
    px.bar(
        region_neigh_price,
        x="Neighborhood_clean",
        y="price_sar",
        color="region",
        title="Average Price by Region and Neighborhood",
        labels={"price_sar": "Avg. Price (SAR)"},
        barmode="group"
    )
)

# Price vs Size
st.subheader("🔹 Price vs Area")
st.plotly_chart(px.scatter(filtered_df, x="area_sqm", y="price_sar", color="bedrooms", title="Price vs Area by Bedrooms", labels={"area_sqm": "Area (m²)", "price_sar": "Price (SAR)"}))

# Apartment Type Breakdown (by bedrooms)
st.subheader("🛏️ Apartment Type Breakdown")
st.plotly_chart(px.pie(filtered_df, names="bedrooms", title="Distribution by Number of Bedrooms"))

# Time Trend
st.subheader("🗓️ Price Trend Over Time")
time_trend = filtered_df.groupby(filtered_df['date'].dt.to_period("M"))["price_sar"].mean().reset_index()
time_trend['date'] = time_trend['date'].astype(str)
st.plotly_chart(px.line(time_trend, x="date", y="price_sar", title="Monthly Average Price Trend", labels={"price_sar": "Avg. Price (SAR)"}))

# Raw Data
st.subheader("📊 Raw Data")
st.dataframe(filtered_df)
st.download_button("Download Filtered Data", filtered_df.to_csv(index=False), file_name="filtered_apartments.csv")
