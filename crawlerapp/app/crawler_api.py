from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
import requests
from bs4 import BeautifulSoup
import uuid
import os

app = FastAPI()


@app.post("/crawl")
def crawl(url: str = Form(...), format: str = Form(...)):
    response = requests.get(url)
    dataTemp = []
    if response.status_code == 200:
        if format == "html":
            soup = BeautifulSoup(response.content, 'html.parser')
            table = soup.find('table', class_='table')

            # Extract the rows of the table
            rows = table.find_all('tr')
            current_city = None

            for row in rows:

                th = row.find("th")
                if th:
                    current_city = th.text.strip()

                columns = row.find_all("td")

                if len(columns) >= 3:
                    brand = columns[0].get_text(strip=True)
                    buy_price = columns[1].get_text(strip=True)
                    sell_price = columns[2].get_text(strip=True)
                    dataTemp.append(f"""
                        Khu vực: {current_city}
                        Hệ thống: {brand}
                        Mua vào: {buy_price}
                        Bán ra: {sell_price}
                        """)
        else:
            soup = BeautifulSoup(response.content, 'xml')
            table = soup.find('table', class_='table')

            # Extract the rows of the table
            rows = table.find_all('tr')
            current_city = None

            for row in rows:

                th = row.find("th")
                if th:
                    current_city = th.text.strip()

                columns = row.find_all("td")

                if len(columns) >= 3:
                    brand = columns[0].get_text(strip=True)
                    buy_price = columns[1].get_text(strip=True)
                    sell_price = columns[2].get_text(strip=True)
                    dataTemp.append(f"""
                            Khu vực: {current_city}
                            Hệ thống: {brand}
                            Mua vào: {buy_price}
                            Bán ra: {sell_price}
                            """)

    urlName = url.split("/")
    fileName = urlName[2].split(".")

    OUTPUT_DIR = "output/txt"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filename = f"{fileName[0]}_{uuid.uuid4().hex}.txt"
    filepath = os.path.join(OUTPUT_DIR, filename)

    data = ' '.join(dataTemp)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(data)

    return FileResponse(
        filepath,
        media_type="text/plain",
        filename=filename
    )