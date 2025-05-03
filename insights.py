import calendar

class CreateInsights:
    @staticmethod
    def overview_text(df) -> str:
        return f"Dataset contains {df.shape[0]} records across {df.shape[1]} columns."

    @staticmethod
    def trend_insights(agg) -> str:
        if agg.empty: return "No data for trend."
        start, end = agg.iloc[0], agg.iloc[-1]
        delta = end["baseRent"] - start["baseRent"]
        pct   = (delta / start["baseRent"] * 100) if start["baseRent"] else 0
        return (
            f"From {start['date'].date()} to {end['date'].date()}, median price changed "
            f"by SAR{delta:.0f} ({pct:.1f}%)."
        )

    @staticmethod
    def type_insights(agg) -> str:
        low, high = agg.iloc[0], agg.iloc[-1]
        return (
            f"Lowest median price: {low['typeOfFlat']} (SAR{low['baseRent']:.0f}); "
            f"Highest: {high['typeOfFlat']} (SAR{high['baseRent']:.0f})."
        )

    @staticmethod
    def feature_insights(imp) -> str:
        texts = []
        for feat in ("elevator", "furnished"):
            sub = imp[imp["Feature"] == feat]
            w, wo = sub[sub.Condition=="With"].Price.values[0], sub[sub.Condition=="Without"].Price.values[0]
            comp = "higher" if w>wo else "lower"
            texts.append(f"Properties with {feat} have {comp} median price (SAR{w:.0f} vs SAR{wo:.0f}).")
        return " ".join(texts)

    @staticmethod
    def map_insights(agg) -> str:
        if agg.empty: return "No data for map."
        hi = agg.loc[agg["MedianRent"].idxmax()]
        lo = agg.loc[agg["MedianRent"].idxmin()]
        return (
            f"Highest median price in {hi.region} (SAR{hi.MedianRent:.0f}); "
            f"lowest in {lo.region} (SAR{lo.MedianRent:.0f})."
        )
