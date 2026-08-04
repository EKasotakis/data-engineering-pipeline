from src.extract import fetch_data
from src.transform import transform_weather_data
from src.validate import validate_weather_data
from datetime import datetime
import json
from src.load import load_to_database
from src.logger import get_logger

logger = get_logger(__name__)

def main() -> None:
    logger.info("Pipeline started.")
    
    raw_data = fetch_data()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    raw_output_path = f"data/raw/weather_raw_{timestamp}.json"

    with open(raw_output_path, "w", encoding="utf-8") as file:
        json.dump(raw_data, file, indent=4)

    logger.info("Raw JSON saved to: %s", raw_output_path)


    dataframe = transform_weather_data(raw_data)

    dataframe = validate_weather_data(dataframe)
    logger.info("Validation passed.")

    load_to_database(dataframe)
    
    output_path = f"data/processed/weather_data_{timestamp}.csv"

    dataframe.to_csv(output_path, index=False)
    logger.info("Processed CSV saved to: %s", output_path)
      
    print(dataframe.head())

    logger.info("Pipeline completed successfully.")


if __name__ == "__main__":
    main()