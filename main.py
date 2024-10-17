from utils.ftp_download import download_files
from data.parse_bills import parse_bill_texts
from db.db_setup import create_db
import sqlite3

if __name__ == '__main__':
    # Step 1: Download legislative data
    legislative_session = '81r'
    output_dir = './data/81r/'
    download_files(legislative_session, output_dir)
    
    # Step 2: Parse the downloaded bill texts
    bills_directory = './data/81r/bills/'
    df_bills = parse_bill_texts(bills_directory)
    
    # Step 3: Create the SQLite database and insert parsed data
    create_db()
    conn = sqlite3.connect('txlege.db')
    df_bills.to_sql('bills', conn, if_exists='replace', index=False)
    conn.close()
    
    print("Data processing complete!")
