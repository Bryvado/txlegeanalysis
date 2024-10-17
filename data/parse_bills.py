import os
import pandas as pd
from lxml import etree

def parse_bill_texts(bills_dir):
    """
    Parse bill texts and return a DataFrame of bill metadata.
    
    :param bills_dir: Directory where bill files are stored
    :return: DataFrame of bill metadata (bill number, type, status, etc.)
    """
    bill_data = []

    for subdir, dirs, files in os.walk(bills_dir):
        for file in files:
            if file.endswith(".xml"):  # Assuming XML files for bill history
                file_path = os.path.join(subdir, file)
                try:
                    tree = etree.parse(file_path)
                    root = tree.getroot()

                    # Extract basic metadata (e.g., bill number, chamber, status)
                    bill_number = root.findtext("billNumber")
                    chamber = root.findtext("chamber")
                    status = root.findtext("status")

                    bill_data.append({
                        "bill_number": bill_number,
                        "chamber": chamber,
                        "status": status,
                        "file_path": file_path
                    })
                except Exception as e:
                    print(f"Failed to parse {file_path}: {e}")
    
    return pd.DataFrame(bill_data)

if __name__ == '__main__':
    bills_directory = './data/81r/bills/'
    df_bills = parse_bill_texts(bills_directory)
    print(df_bills.head())
