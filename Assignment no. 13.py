import json
import csv

def json_to_csv(json_file: str, csv_file: str):
    """Convert a JSON array into a CSV file."""
    try:
        # Step 1: Load JSON data
        with open(json_file, "r") as jf:
            data = json.load(jf)

        # Ensure the JSON is a list of dictionaries
        if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
            raise ValueError("JSON must be an array of objects (list of dictionaries).")

        # Step 2: Extract headers from keys of the first dictionary
        headers = data[0].keys()

        # Step 3: Write to CSV
        with open(csv_file, "w", newline="") as cf:
            writer = csv.DictWriter(cf, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)

        print(f"Successfully converted '{json_file}' to '{csv_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{json_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Example usage
    json_file = "data.json"   # Replace with your JSON file
    csv_file = "output.csv"   # Desired CSV output file
    json_to_csv(json_file, csv_file)

if __name__ == "__main__":
    main()
