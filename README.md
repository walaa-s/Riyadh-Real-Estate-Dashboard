# Riyadh Real Estate Market Insights Dashboard

A Streamlit-based analytics dashboard for exploring and visualizing Riyadh apartment listing data. This project walks through:

1. **Data Collection**  
2. **Data Cleaning & Visualization**  
3. **Project Deployment**

---

## 1. Data Collection

**Requirements**  
- Must include a **date** field for each record.  
- Must include a **location/region** field for each record.  
- Must contain at least **10,000 rows**.

**In this project**  
We use `riyadh_apartments_updated.csv`, which has:
- **`Region`** → normalized into a `region` column  
- **10,000+** listings spanning 2020–2024  

---

## 2. Data Cleaning & Visualization

### 2.1 Cleaning  
- Remove rows with missing **date**, **price**, or **region**.  
- Parse and cast:
  - `Selling Price (SAR)` → `baseRent` (float)  
  - `Area (sqm)` → `livingSpace` (float)  
  - `Bedrooms` → `noRooms` (integer)  
  - `Property Age (years)` → compute `yearConstructed`  
  - `Elevator` & `Furnished` → boolean flags  
- Standardize text columns (`region`, `typeOfFlat`).

### 2.2 Visualization  
We produce the following interactive charts (via Plotly + Streamlit):

| Section                         | Chart                                                                                                          |
|---------------------------------|----------------------------------------------------------------------------------------------------------------|
| **Data Distributions**          | • Histogram of **Selling Price** (SAR)<br>• Histogram of **Year Built**                                       |
| **Price Trend Over Time**       | • Line chart of median **baseRent** & **totalRent** by date                                                     |
| **Median Price by Type**        | • Bar chart of median **Selling Price** grouped by **Property Type**                                           |
| **Elevator & Furnished Impact** | • Grouped bar chart comparing median price “With” vs “Without” each feature                                   |
| **Map by Region**               | • Mapbox scatter showing each **region**’s median price (color) and property count (marker size)              |

Each chart is accompanied by a short, automatically generated **insight**.

---

## 3. Project Deployment

We deliver a **Streamlit** app:

- **Interactive sidebar filters** for:
  - Price range slider (SAR)  
  - Multi-select regions  
- **Expandable summary** table of the cleaned DataFrame  
- **Embedded Plotly charts** with insight text below each  

### 3.1 Prerequisites

- Python 3.8+  
- `pip`  

### 3.2 Installation

1. Clone this repo:
   ```bash
   git clone https://github.com/your-org/riyadh-real-estate-dashboard.git
   cd riyadh-real-estate-dashboard
Create & activate a virtual environment:


python -m venv venv
source venv/bin/activate       # Linux / macOS
venv\Scripts\activate          # Windows PowerShell
Install dependencies:

pip install -r requirements.txt
Note: requirements.txt should list:


streamlit
pandas
plotly
Place your riyadh_apartments_updated.csv in the project root.

### 3.3 Running the App

streamlit run app.py
Visit http://localhost:8501 in your browser to interact with the dashboard.

### File Structure

├── app.py               # Streamlit main script
├── config.py            # Region-to-lat/lon mappings
├── process_data.py      # Data loading & cleaning logic
├── graphs.py            # Plotly chart creation
├── insights.py          # Auto-generated insight text
├── requirements.txt     # Python dependencies
└── riyadh_apartments_updated.csv  # Raw data (10k+ rows)

### How to Extend
Add new filters (e.g. number of bedrooms, living space).

Swap in FastAPI for a RESTful backend + separate frontend.

Enhance insights with statistical tests or NLP on descriptions.

Enjoy exploring Riyadh’s real-estate market!
Please open an issue or pull request for questions or improvements.
