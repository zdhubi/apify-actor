import os
import sys
from selenium_fetcher import fetch_products
from xml_generator import build_xml
from log_writer import write_log
from email_notifier import send_error_email
from ftplib import FTP

def upload_to_ftp(host, user, pwd, filename):
    with FTP(host) as ftp:
        ftp.login(user, pwd)
        with open(filename, 'rb') as f:
            ftp.storbinary(f'STOR {filename}', f)

def main():
    try:
        products = fetch_products()
        xml_file = build_xml(products)
        write_log(len(products))
        upload_to_ftp(
            os.environ['FTP_HOST'],
            os.environ['FTP_USER'],
            os.environ['FTP_PASSWORD'],
            xml_file
        )
    except Exception as e:
        send_error_email(str(e))
        sys.exit(1)

if __name__ == "__main__":
    main()
