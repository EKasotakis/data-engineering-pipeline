from src.extract import fetch_data
from src.transform import transform_weather_data
from src.validate import validate_weather_data
from datetime import datetime
import json
from src.load import load_to_database


def main() -> None:
    raw_data = fetch_data()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    raw_output_path = f"data/raw/weather_raw_{timestamp}.json"

    with open(raw_output_path, "w", encoding="utf-8") as file:
        json.dump(raw_data, file, indent=4)

    print(f"Raw JSON saved to: {raw_output_path}")

    dataframe = transform_weather_data(raw_data)

    validate_weather_data(dataframe)

    load_to_database(dataframe)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f"data/processed/weather_data_{timestamp}.csv"

    dataframe.to_csv(output_path, index=False)

    print(f"CSV file saved to: {output_path}")

    print("Validation passed.")
    print(dataframe.head())


if __name__ == "__main__":
    main()