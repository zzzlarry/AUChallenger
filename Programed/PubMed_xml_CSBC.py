import xml.etree.ElementTree as ET
import csv

#以文件方讀取XML，解析XML
tree = ET.parse('xml.xml')
root = tree.getroot()
#開啟一個新檔案裝東西用
Resident_data = open('d:/XML/xml.csv', 'w',newline='')
#設定一變數用來裝等一下要存的東西
csvwriter = csv.writer(Resident_data)
#將CSV標題寫入檔案
csvwriter.writerow(["Affiliation", "Year", "ArticleTitle","journal","Abstract","Country","PMID"])

#開始抓資料
for a in root.findall('PubmedArticle'):
    #這一欄位因為有空值會報錯，所以加一個異常判斷
    try:
        # 抓資料
        Affiliation = a.find('MedlineCitation/Article/AuthorList/Author/AffiliationInfo/Affiliation').text
    except:
        #如果出現異常在變入內寫入'NONE'字串
        Affiliation = 'NONE'
        pass
    # 抓資料
    Year = a.find('MedlineCitation/DateCompleted/Year').text
    # 抓資料
    ArticleTitle = a.find('MedlineCitation/Article/ArticleTitle').text
    # 抓資料
    journal = a.find('MedlineCitation/Article/Journal/Title').text
    # 抓資料
    Abstract = a.find('MedlineCitation/Article/Abstract/AbstractText').text
    # 抓資料
    Country = a.find('MedlineCitation/MedlineJournalInfo/Country').text
    # 抓資料
    PMID = a.find('MedlineCitation/PMID').text
    #將抓到的資料寫入，變數名稱後面那一大串用來轉換編碼cp950無法被寫入檔案
    csvwriter.writerow([Affiliation.encode("utf8").decode("cp950", "ignore"), Year.encode("utf8").decode("cp950", "ignore"),
                        ArticleTitle.encode("utf8").decode("cp950", "ignore"), journal.encode("utf8").decode("cp950", "ignore"),
                        Abstract.encode("utf8").decode("cp950", "ignore"), Country.encode("utf8").decode("cp950", "ignore"),
                        PMID.encode("utf8").decode("cp950", "ignore")])







