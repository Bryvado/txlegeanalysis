import ftplib
import os

FTP_SERVER = 'ftp.legis.state.tx.us'
BILLS_DIR = '/bills/'  # Modify this if necessary

def download_files(legislative_session, output_dir):
    """
    Downloads files from the Texas Legislature FTP.
    
    :param legislative_session: The legislative session to download (e.g., 81r for 2009)
    :param output_dir: Local directory to store downloaded files
    """
    with ftplib.FTP(FTP_SERVER) as ftp:
        ftp.login()
        session_dir = os.path.join(BILLS_DIR, legislative_session)
        ftp.cwd(session_dir)
        
        # Recursively download the bill documents
        os.makedirs(output_dir, exist_ok=True)
        download_recursive(ftp, '', output_dir)

def download_recursive(ftp, current_dir, local_dir):
    """
    Helper function to recursively download files from the FTP server.
    
    :param ftp: Active FTP connection
    :param current_dir: Current FTP directory
    :param local_dir: Local directory to save files
    """
    ftp.cwd(current_dir)
    os.makedirs(local_dir, exist_ok=True)
    
    for item in ftp.nlst():
        if '.' in item:  # It's a file
            local_path = os.path.join(local_dir, item)
            if not os.path.exists(local_path):
                with open(local_path, 'wb') as f:
                    ftp.retrbinary(f'RETR {item}', f.write)
                    print(f"Downloaded {item}")
        else:  # It's a directory
            new_local_dir = os.path.join(local_dir, item)
            download_recursive(ftp, item, new_local_dir)

if __name__ == '__main__':
    session = '81r'  # Example: 81st Regular Session (2009)
    output = './data/81r/'
    download_files(session, output)
