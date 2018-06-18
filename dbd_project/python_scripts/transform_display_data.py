import download_file_api as dfa
import csv
import os 


def main():
    
  # 檔案名稱
  fo = open("詐騙資訊蒐集(完整).csv", "r", encoding = 'utf-8-sig')
  origin_old_version_len = sum(1 for line in fo)
  fo.close()
  origin_csv =  "詐騙資訊蒐集.csv"
  final_csv = "詐騙資訊(上傳).csv"
  
  # Download files
  # 詐騙資訊
  dfa.download_csv("19IcNQepzCRqT-1Jqn1l9OV68RX0hKZGu3W6LpnHs24I", origin_csv)
  #origin_xlsx = origin_xlsx + ".xlsx"
  #csv_from_excel(origin_xlsx, origin_csv)
  f = open(origin_csv, "r", encoding = 'utf-8-sig')
  output_f = open(final_csv, 'w', newline = '')
  fieldnames = ["時間戳記", "標題內容(如：商品名稱或網站名稱)", "網站網址", "說明此網站或商品的特徵", "上傳你的畫面"]
  writer = csv.DictWriter(output_f, fieldnames=fieldnames)
  writer.writeheader()  
  i = 1

  for row in csv.DictReader(f):
    if i >= origin_old_version_len:
      if row["上傳你的畫面"] != "":
        line = row["上傳你的畫面"]
        front = line[0:line.find("open?")]
        line_id = line[line.find("open?") + 5:]
        final_line = front + "uc?export=download&" + line_id
        writer.writerow({"時間戳記": row["時間戳記"], "標題內容(如：商品名稱或網站名稱)": row["標題內容(如：商品名稱或網站名稱)"], "網站網址": row["網站網址"], "說明此網站或商品的特徵": row["說明此網站或商品的特徵"], "上傳你的畫面": final_line})
    i = i + 1
    
  output_f.close()  
  f.close()
  
  os.remove("詐騙資訊蒐集(完整).csv")
  os.rename("詐騙資訊蒐集.csv", "詐騙資訊蒐集(完整).csv")
  
    
if __name__ == '__main__':
  main()