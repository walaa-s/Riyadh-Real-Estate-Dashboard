# Riyadh Real Estate Market Insights Dashboard

A Streamlit-based analytics dashboard for exploring and visualizing apartment listings in Riyadh (10,000+ rows from 2020–2024).

This project covers:

1. **Data Collection**
2. **Data Cleaning & Visualization**
3. **Streamlit Deployment**

---

## 1. Data Collection

**Requirements:**

* Each record must include a **date** field and a **region** field.
* Dataset must have at least **10,000 rows**.

**Implementation:**

* Source file: `riyadh_apartments_updated.csv` (10,000+ listings).
* Key columns:

  * `date_listed` → listing date
  * `region` → e.g., East, West, Central
  * `typeOfFlat`, `Bedrooms`, `Area (sqm)`, `Selling Price (SAR)`

---

## 2. Data Cleaning & Visualization

### 2.1 Cleaning Steps

1. **Drop** rows missing **date**, **price**, or **region**.
2. **Parse & cast**:

   * `Selling Price (SAR)` → `baseRent` (float)
   * `Area (sqm)` → `livingSpace` (float)
   * `Bedrooms` → `noRooms` (integer)
   * `Property Age (years)` → derive `yearBuilt`
   * `Elevator`, `Furnished` → boolean flags
3. **Standardize** text columns: trim whitespace, lowercase.

### 2.2 Visualization Components

| Section                     | Plot Type & Details                                                                 |
| --------------------------- | ----------------------------------------------------------------------------------- |
| **Price Distribution**      | Histogram of `baseRent` (SAR)                                                       |
| **Year Built Distribution** | Histogram of `yearBuilt`                                                            |
| **Price Over Time**         | Line chart of median `baseRent` by `date_listed`                                    |
| **Price by Property Type**  | Bar chart of median `baseRent` grouped by `typeOfFlat`                              |
| **Feature Impact**          | Grouped bar charts: median price **with** vs **without** `Elevator` and `Furnished` |
| **Regional Heatmap**        | Mapbox scatter: median price (color) + listing count (size) per `region`            |

*All charts include dynamic filters via the sidebar (date range, regions, price slider).*

---

## 3. Deployment with Streamlit

**Entry point:** `app.py`

### 3.1 Prerequisites

* **Python:** 3.8+
* **Streamlit** & other dependencies in `requirements.txt`

### 3.2 Installation

```bash
# 1. Clone the repo
git clone https://github.com/your-org/riyadh-real-estate-dashboard.git
cd riyadh-real-estate-dashboard

# 2. (Optional) Create a virtual environment
python3 -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate       # Windows PowerShell

# 3. Install dependencies
pip install -r requirements.txt
```

> **requirements.txt** should list:
>
> ```txt
> streamlit
> pandas
> plotly
> geopandas        # if using shapefiles for regions
> ```

Place **`riyadh_apartments_updated.csv`** in the project root.

### 3.3 Running the App

```bash
streamlit run app.py
```

Then open `http://localhost:8501` in your browser.

---

### Project Structure

```
riyadh-real-estate-dashboard/
├─ app.py               # Streamlit app entry
├─ config.py            # Region-to-coordinates mappings
├─ process_data.py      # Data loading & cleaning
├─ graphs.py            # Plotly chart functions
├─ insights.py          # Auto-generated insights text
├─ requirements.txt     # Python dependencies
└─ riyadh_apartments_updated.csv  # Raw dataset (10k+ rows)
```

---

## How to Extend

* Add **additional filters**: number of bedrooms, living space range.
* Swap in **FastAPI** to serve cleaned data via REST.
* Embed **statistical tests** or **NLP** insights (e.g., text analysis on neighborhood descriptions).

*Questions or improvements? Open an issue or pull request!*
