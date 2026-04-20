import csv

def count_rows(filename: str) -> int:
    """Count the total number of rows in a CSV file."""
    try:
        with open(filename, mode="r", newline="") as file:
            reader = csv.reader(file)
            row_count = sum(1 for _ in reader)
        return row_count
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

def main():
    filename = "sample.csv"  # Replace with your CSV file name
    total_rows = count_rows(filename)
    print(f"Total number of rows in '{filename}': {total_rows}")

if __name__ == "__main__":
    main()
