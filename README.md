
This project was developed as a team effort by:
- Raneem Althqafi
- Jana Almalki
- Walaa Almajnuni
- Waleed Algrafe 
- Osamah Alrdadi 

Original repository: [RaneemQasim5251/Riyadh-Real-Estate-Dashboard](https://github.com/RaneemQasim5251/Riyadh-Real-Estate-Dashboard)







# Riyadh Real Estate Market Insights Dashboard
![image](https://github.com/user-attachments/assets/794ea08d-7797-4943-af94-2dc6ca6972f9)

link:
https://weekendproject.streamlit.app/

![image](https://github.com/user-attachments/assets/a5e32ebc-46d7-4c13-8608-5383462153cd)
![image](https://github.com/user-attachments/assets/8404fe30-208d-4dc3-80e6-0a839d48d8e3)
![image](https://github.com/user-attachments/assets/8f804048-88f3-4982-b798-fc7dcdbd37fc)
![image](https://github.com/user-attachments/assets/8c8f479b-63f0-454e-8cf6-8ea702be777e)
![image](https://github.com/user-attachments/assets/a41e6d19-5ba0-4978-a73b-e667a0f8c125)
![image](https://github.com/user-attachments/assets/f83e499d-de2e-4585-ae3f-a86a5813b681)
![image](https://github.com/user-attachments/assets/8e2b948c-b82e-4443-b24b-440180a59119)

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
├─ insights.py          # insights
├─ requirements.txt     # Python dependencies
└─ riyadh_apartments_updated.csv  # Raw dataset (10k+ rows)
```

---

## How to Extend

* Add **additional filters**: number of bedrooms, living space range.
* Swap in **FastAPI** to serve cleaned data via REST.
* Embed **statistical tests** or **NLP** insights (e.g., text analysis on neighborhood descriptions).

*Questions or improvements? Open an issue or pull request!*
