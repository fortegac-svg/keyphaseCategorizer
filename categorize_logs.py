import pandas as pd
import sys

def load_keywords(file_path):
    """Load keywords from the CSV file and return as a dictionary."""
    keywords_df = pd.read_csv(file_path)
    keywords_dict = {}
    for _, row in keywords_df.iterrows():
        # Join keywords into a single string, each keyword separated by ', '
        keywords = ', '.join([k.strip().lower() for k in row['Keywords'].split(',')])
        category_info = (row['CategoryType'], row['CategoryValue'])
        keywords_dict[keywords] = category_info
    return keywords_dict


def categorize_log_entry(entry, keywords_dict):
    """Categorize a single log entry based on keywords."""
    description = entry['Description'].lower()
    # Initialize categories with 'NEEDS KEYWORD', which will be updated if matches are found
    entry_categories = {'Object': 'NEEDS KEYWORD', 'Behaviour': 'NEEDS KEYWORD', 'Technique': 'NEEDS KEYWORD'}

    # Iterate through all keywords and their associated categories
    for keyword, category_info in keywords_dict.items():
        # Check if any keyword is in the log entry's description
        if any(kw in description for kw in keyword.split(', ')):
            category_type, category_value = category_info
            # Update the entry's category if a keyword is found
            entry_categories[category_type] = category_value

    return entry_categories



def categorize_logs(log_df, keywords_dict):
    """Categorize all log entries in the DataFrame."""
    for index, row in log_df.iterrows():
        categories = categorize_log_entry(row, keywords_dict)
        for category_type, category_value in categories.items():
            log_df.at[index, category_type] = category_value
    return log_df

def main(log_file_path, keywords_file_path, output_file_path):
    log_df = pd.read_csv(log_file_path)
    keywords_dict = load_keywords(keywords_file_path)
    print(f"Starting categorization of logs...")
    categorized_df = categorize_logs(log_df, keywords_dict)
    print(f"Categorization complete. Saving to {output_file_path}")
    categorized_df.to_csv(output_file_path, index=False)
    print(f"File saved successfully.")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python categorize_logs.py <log_file.csv> <keywords.csv> <output.csv>")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2], sys.argv[3])
