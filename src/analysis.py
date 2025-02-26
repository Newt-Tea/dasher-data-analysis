import pandas as pd

def load_data(file_path):
    """Load the DoorDash data from a CSV file."""
    data = pd.read_csv(file_path)
    return data

def analyze_data(data):
    """Perform analysis on the DoorDash data."""
    # Example analysis: Calculate total earnings per driver
    total_earnings = data.groupby('driver_id')['earnings'].sum()
    return total_earnings

def main():
    """Main function to execute the analysis."""
    file_path = '../data/doordash_data.csv'
    data = load_data(file_path)
    insights = analyze_data(data)
    print(insights)

if __name__ == "__main__":
    main()