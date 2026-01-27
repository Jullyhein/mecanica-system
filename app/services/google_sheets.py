import requests
import csv
from io import StringIO

def ler_google_sheets(url:str):
    response = requests.get(url)
    response.raise_for_status()

    csv_data = StringIO(response.txt)
    reader = csv.DictReader(csv_data)

    return(list(reader))
