# 🌦️ Data Engineering Pipeline – Luxembourg Weather ETL

## 📌 Overview

This project is an end-to-end data engineering pipeline that extracts weather forecast data from the Open-Meteo API, validates and transforms the data, stores it in PostgreSQL, orchestrates the workflow using Apache Airflow, and visualizes the results through an interactive Streamlit dashboard.

The project demonstrates the complete lifecycle of a production-style ETL pipeline, including data ingestion, validation, storage, scheduling, testing, logging, and visualization.

---

## 🚀 Features

- Extracts weather data from the Open-Meteo API
- Saves raw API responses as JSON
- Transforms JSON into structured pandas DataFrames
- Validates data using Pandera schemas
- Loads data into PostgreSQL
- Performs UPSERT operations to prevent duplicate records
- Stores processed CSV files
- Logs pipeline execution
- Automatic retry mechanism for failed API requests
- Unit tests using Pytest
- Scheduled execution using Apache Airflow
- Interactive dashboard using Streamlit and Plotly

---

## 🏗️ Architecture

```
                 Open-Meteo API
                        │
                        ▼
                 Extract (requests)
                        │
                        ▼
              Transform (pandas)
                        │
                        ▼
             Validate (Pandera)
                        │
                        ▼
          PostgreSQL Database
               ▲            │
               │            ▼
         Airflow DAG    Streamlit Dashboard
```

---

## 🛠️ Technologies Used

| Category | Technologies |
|----------|--------------|
| Language | Python 3.12 |
| Data Processing | pandas |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Validation | Pandera |
| API | Requests |
| Workflow | Apache Airflow |
| Dashboard | Streamlit, Plotly |
| Testing | Pytest |
| Containerization | Docker |
| Environment | python-dotenv |

---

## 📁 Project Structure

```
Data_Engineering_Pipeline/
│
├── airflow/
│   └── dags/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── logs/
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── validate.py
│   ├── load.py
│   ├── logger.py
│   └── utils.py
│
├── tests/
│
├── dashboard.py
├── main.py
├── docker-compose.yml
├── airflow-compose.yaml
├── requirements.txt
└── README.md
```

---

## ⚙️ Pipeline Workflow

1. Request weather data from the Open-Meteo API.
2. Save the raw response as a JSON file.
3. Transform the JSON into a pandas DataFrame.
4. Validate the data using a Pandera schema.
5. Load the validated data into PostgreSQL.
6. Export a processed CSV file.
7. Record execution logs.
8. Schedule automatic execution through Apache Airflow.
9. Visualize the stored data using Streamlit.

---

## 📊 Dashboard

The Streamlit dashboard includes:

- Current weather statistics
- Average temperature
- Average humidity
- Average wind speed
- Interactive Plotly charts
- Adjustable day filter
- Raw data table

---

## 🧪 Testing

Unit tests are written with Pytest and cover:

- Data transformation
- Data validation
- Missing value detection

Run the tests:

```bash
pytest
```

---

## ▶️ Running the Project

### Clone the repository

```bash
git clone https://https://github.com/EKasotakis/data-engineering-pipeline.git
cd data-engineering-pipeline
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the environment

Windows

```bash
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start PostgreSQL

```bash
docker compose -f docker-compose.yml up -d
```

### Execute the pipeline

```bash
python main.py
```

### Start the dashboard

```bash
streamlit run dashboard.py
```

### Start Apache Airflow

```bash
docker compose -p airflow -f airflow-compose.yaml up -d
```

Open:

```
http://localhost:8080
```

---

## 📈 Future Improvements

- CI/CD using GitHub Actions
- Dockerized Streamlit deployment
- Cloud deployment (Azure/AWS)
- Historical weather analytics
- Multiple city support
- Data quality reports

---

## 👤 Author

**Emmanouil Kasotakis**

MSc Artificial Intelligence & Data Science

Luxembourg