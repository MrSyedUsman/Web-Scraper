from bs4 import BeautifulSoup
import requests
import csv

filename = "table_scrape.csv"
csv_writer = csv.writer(open(filename,"w"))

for i in range(1,322):
    source = requests.get("https://www.freiwilligenserver.de/index.cfm?uuid=1C54FF36C3F011D6B42C0080AD795D93&showPage="+str(i)+"&pageRows=100&char=&search=&kreis=&order=vereinA&").text
    soup = BeautifulSoup(source,"lxml")

    # filename = "table_scrape.csv"
    # csv_writer = csv.writer(open(filename,"w"))

    table = soup.find("table", class_="fwsDbView")
    # print(table.text)

    for tr in table.find_all("tr"):
        data = []

        if(i==1):
            for th in tr.find_all("th"):
                data.append(th.text.strip())
            
            if(data):
                print("inserting headers: {}".format(",".join(data)))
                csv_writer.writerow(data)
                continue

        for td in tr.find_all("td"):
            data.append(td.text.strip())

        if(data):
            print("Inserting data table: {}".format(",".join(data)))
            csv_writer.writerow(data)

