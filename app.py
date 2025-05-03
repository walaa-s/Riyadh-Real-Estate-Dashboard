import streamlit as st
from process_data import ProcessData
from graphs import CreateGraphs
from insights import CreateInsights

st.set_page_config(page_title="Riyadh Real Estate Dashboard", layout="wide")
st.title("Riyadh Real Estate Market Insights")

# --- load & clean ---
processor = ProcessData("riyadh_apartments_updated.csv")
df = processor.get_clean_data()

# --- sidebar filters ---
st.sidebar.header("Filter Data")
min_price, max_price = st.sidebar.slider(
    "Price Range (SAR)",
    int(df.baseRent.min()), int(df.baseRent.max()),
    (int(df.baseRent.min()), int(df.baseRent.max()))
)
regions = st.sidebar.multiselect(
    "Regions", sorted(df.region.unique()), default=sorted(df.region.unique())
)
filtered = df.query("baseRent >= @min_price and baseRent <= @max_price and region in @regions")

# --- overview ---
st.header("Data Overview")
with st.expander("Show full summary table"):
    overview_df = CreateGraphs.overview_table(filtered)
    st.table(overview_df)       # ← use st.table to avoid Arrow errors
st.markdown(CreateInsights.overview_text(filtered))

st.markdown("---")

# --- distributions ---
st.header("Data Distributions")
fig_price, fig_year = CreateGraphs.distribution(filtered)
c1, c2 = st.columns(2)
with c1: st.plotly_chart(fig_price, use_container_width=True)
with c2: st.plotly_chart(fig_year,  use_container_width=True)

st.markdown("---")

# --- trend ---
st.header("Price Trend Over Time")
fig_trend, trend_df = CreateGraphs.trend_over_time(filtered)
st.plotly_chart(fig_trend, use_container_width=True)
st.markdown(CreateInsights.trend_insights(trend_df))

st.markdown("---")

# --- by type ---
st.header("Median Price by Property Type")
fig_type, type_df = CreateGraphs.by_type(filtered)
st.plotly_chart(fig_type, use_container_width=True)
st.markdown(CreateInsights.type_insights(type_df))

st.markdown("---")

# --- feature impact ---
st.header("Elevator & Furnished Impact")
fig_imp, imp_df = CreateGraphs.feature_impact(filtered)
st.plotly_chart(fig_imp, use_container_width=True)
st.markdown(CreateInsights.feature_insights(imp_df))

st.markdown("---")

# --- map ---
st.header("Median Price by Region")
fig_map, map_df = CreateGraphs.create_map(filtered)
st.plotly_chart(fig_map, use_container_width=True)
st.markdown(CreateInsights.map_insights(map_df))
