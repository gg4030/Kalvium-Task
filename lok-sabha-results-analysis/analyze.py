import pandas as pd

def analyze_data(filename):
    df = pd.read_csv(filename)

    # Display the column names to verify
    print(f"Columns in {filename}: {df.columns}")

    # Example analysis: counting seats won by each party
    if 'Party' in df.columns:
        party_counts = df['Party'].value_counts()
        print(f"Seats won by each party in {filename}:\n{party_counts}\n")

    # Example analysis: voter turnout
    if 'Total Votes' in df.columns and 'Total Electors' in df.columns:
        voter_turnout = (df['Total Votes'].astype(float).sum() / df['Total Electors'].astype(float).sum()) * 100
        print(f"Overall voter turnout in {filename}: {voter_turnout:.2f}%\n")

    # Example analysis: close races (assuming 'Votes Secured' and 'Runner Up Votes' are the correct column names)
    if 'Votes Secured' in df.columns and 'Runner Up Votes' in df.columns:
        df['Margin'] = df['Votes Secured'].astype(float) - df['Runner Up Votes'].astype(float)
        close_races = df[df['Margin'] < 1000]
        print(f"Close races in {filename} (margin < 1000 votes):\n{close_races}\n")

# Filenames to analyze
filenames = [
    'PcResultGenJune2024.csv',
    'AcResultGenJune2024.csv',
    'AcResultByeJune2024.csv',
    'AcResultGen2ndJune2024.csv'
]

for filename in filenames:
    analyze_data(filename)
