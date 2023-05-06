import requests
from bs4 import BeautifulSoup
import xlsxwriter


workbook = xlsxwriter.Workbook('data.xlsx')
worksheet = workbook.add_worksheet()
row = 0
col = 0

# Number of Pages
pages = 12

for i in range(1, pages+1):
    response = requests.get(f"https://damatajhiz.com/en/mag/page/{i}")
    soup = BeautifulSoup(response.text, "html.parser")
    sub_pages = soup.find_all("h2")
    for sub_page in sub_pages:
        sub_page = sub_page.find("a").attrs
        title = sub_page["title"].replace("Permalink to ", "")
        url = sub_page["href"]
        worksheet.write(row, col,     title)
        worksheet.write(row, col + 1, url)
        print(f"row is: {row}")
        row += 1
print("Done")
workbook.close()