import csv
import pandas as pd


  #=====================
  # input:
  #   input_file_name: the input data name
  #   output_file_name: name the output data and create it
  #   mode: 0 for "詐騙特徵蒐集"
  #         1 for "簡易詐騙風險檢測"
  #
  # function: 
  #   preprocess the feature
  #=====================

  
def csv_from_excel(xlsxname, csvname):
  data_xlsx = pd.read_excel(xlsxname, index = 0)
  data_xlsx.to_csv(csvname, encoding='utf-8') 
    
 
# runs the csv_from_excel function:
def feature1_processing(row, feature):
  if feature == "https":
    row.append(1)
    row.append(0)
    row.append(0)
  elif feature == "http":
    row.append(0)
    row.append(1)
    row.append(0)
  elif feature == "兩者都沒有":
    row.append(0)
    row.append(0)
    row.append(1)
  else:
    row.append(0)
    row.append(0)
    row.append(0)
  
def feature2_processing(row, feature):
  if feature == "美國":
    row.append(1)
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(0)
  elif feature == "日本":
    row.append(0)
    row.append(1)
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(0)
  elif feature == "德國":
    row.append(0)
    row.append(0)
    row.append(1)
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(0)
  elif feature == "韓國":
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(1)
    row.append(0)
    row.append(0)
    row.append(0)
  elif feature == "英國、法國":
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(1)
    row.append(0)
    row.append(0)
  elif feature == "其他國家":
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(1)
    row.append(0)
  elif feature == "無":
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(1)
  else:
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(0)
  
def feature3_processing(row, feature):
  if feature == "一折":
    row.append(1)
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(0)
  elif feature == "兩折":
    row.append(0)
    row.append(1)
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(0)
  elif feature == "三折":
    row.append(0)
    row.append(0)
    row.append(1)
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(0)
  elif feature == "四折":
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(1)
    row.append(0)
    row.append(0)
    row.append(0)
  elif feature == "五折":
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(1)
    row.append(0)
    row.append(0)
  elif feature == "其他":
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(1)
    row.append(0)
  elif feature == "無":
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(1)
  else:
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(0)
  
def feature4_processing(row, feature):
  if feature == "有":
    row.append(1)
    row.append(0)
  elif feature == "沒有":
    row.append(0)
    row.append(1)
  else:
    row.append(0)
    row.append(0)
  
def feature5_processing(row, feature):
  if feature == "facebook":
    row.append(1)
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(0)
  elif feature == "露天拍賣":
    row.append(0)
    row.append(1)
    row.append(0)
    row.append(0)
    row.append(0)
  elif feature == "yahoo 奇摩購物":
    row.append(0)
    row.append(0)
    row.append(1)
    row.append(0)
    row.append(0)
  elif feature == "vivishop":
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(1)
    row.append(0)
  elif feature == "其他":
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(1)
  else:
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(0)
    row.append(0)
  
def feature6_processing(row, feature):
  if feature == "倒數計時":
    row.append(1)
    row.append(0)
    row.append(0)
  elif feature == "只有提到限時":
    row.append(0)
    row.append(1)
    row.append(0)
  elif feature =="無":
    row.append(0)
    row.append(0)
    row.append(1)
  else:
    row.append(0)
    row.append(0)
    row.append(0)
  
def feature_time_processing(row, feature):
  if feature.find("上午") == -1:
    feature = feature[:feature.find("下午")] + "PM" + feature[feature.find("下午") + 2:]
  elif feature.find("下午") == -1:
    feature = feature[:feature.find("上午")] + "AM" + feature[feature.find("上午") + 2:]
  else:
    print("時區轉換失敗")
  year = feature[0:4]
  first = feature.find("/")
  second_slice = feature[first + 1 :]
  second = second_slice.find("/") + feature.find("/")
  month = feature[feature.find("/") + 1 : second + 1]
  third = feature.find("M") - 2
  day = feature[second + 2 : third + 1]
  time = feature[feature.find("M") - 1 :]
  attribute_ = year + "/" + month + "/" + day + " " + time[0] + "." + time[1] + ". " + time[2:]
  row.append(attribute_)



def feature_preprocessing(input_file_name, output_file_name, mode):
  #=====================
  # input:
  #   input_file_name: the input data name
  #   output_file_name: name the output data and create it
  #   mode: 0 for "詐騙特徵蒐集"
  #         1 for "簡易詐騙風險檢測"
  #
  # function: 
  #   preprocess the feature
  #=====================
    
  # test Mode
  if mode != 0:
    if mode != 1:
      print("Mode Error!!")
  
  #csv_from_excel(input_file_name, output_file_name)
  # open the file
  f = open(input_file_name, "r", encoding = 'utf-8-sig')
  output_f = open(output_file_name, 'w', newline = '')
  #i = 0
  # 詐騙特徵蒐集之前處理
  if mode == 0:
    fieldnames = ["https", "http", "nether", "Ame", "Jap", "Ger", "Kor", "UK, Fre", "Other", "coun_nether", \
                  "10", "20", "30", "40", "50", "cost_other", "cost_nether", "Brands", "NBrands", "facebook", \
                  "no2", "no3", "no4", "no5", "count_down", "limited_time", "no_limited_time", "result"]

    writer = csv.DictWriter(output_f, fieldnames=fieldnames)
    writer.writeheader()  
    for row in csv.DictReader(f):
      #i = i + 1
      
      # read row
      if row['您已確定該網站為詐騙網站？'] == "是，這是詐騙網站。" :
        feature1 = row['請看到網址的部分，它包含以下哪一種網址？']
        feature2 = row['該商品有提到它是外國商品？']
        feature3 = row['下殺折扣']
        feature4 = row['有無使用品牌名稱']
        feature5 = row['該商品販賣網站為？']
        feature6 = row['有無限時優惠？']
      elif row['您已確定該網站為詐騙網站？'] == "否，我確定不是。" :
        feature1 = row['請看到網址的部分，它包含以下哪一種網址？1']
        feature2 = row['該商品有提到它是外國商品？1']
        feature3 = row['下殺折扣1']
        feature4 = row['有無使用品牌名稱1']
        feature5 = row['該商品販賣網站為？1']
        feature6 = row['有無限時優惠？1']
        
      # process row
      new_row = []
      feature1_processing(new_row, feature1)
      feature2_processing(new_row, feature2)
      feature3_processing(new_row, feature3)
      feature4_processing(new_row, feature4)
      feature5_processing(new_row, feature5)
      feature6_processing(new_row, feature6)

      # write csv
      if row['您已確定該網站為詐騙網站？'] == "是，這是詐騙網站。" :
        writer.writerow({'https': new_row[0], 'http': new_row[1], 'nether': new_row[2], 'Ame': new_row[3], \
                         'Jap': new_row[4], 'Ger': new_row[5], 'Kor': new_row[6], 'UK, Fre': new_row[7], \
                         'Other': new_row[8], 'coun_nether': new_row[9], '10': new_row[10],'20': new_row[11], \
                         '30': new_row[12], '40': new_row[13], '50': new_row[14], 'cost_other': new_row[15], \
                         'cost_nether': new_row[16], 'Brands': new_row[17], 'NBrands': new_row[18], \
                         'facebook': new_row[19], 'no2': new_row[20], 'no3': new_row[21], 'no4': new_row[22], \
                         'no5': new_row[23], 'count_down': new_row[24], 'limited_time': new_row[25], \
                         'no_limited_time': new_row[26], 'result': 1})
      elif row['您已確定該網站為詐騙網站？'] == "否，我確定不是。" :
         writer.writerow({'https': new_row[0], 'http': new_row[1], 'nether': new_row[2], 'Ame': new_row[3], \
                         'Jap': new_row[4], 'Ger': new_row[5], 'Kor': new_row[6], 'UK, Fre': new_row[7], \
                         'Other': new_row[8], 'coun_nether': new_row[9], '10': new_row[10],'20': new_row[11], \
                         '30': new_row[12], '40': new_row[13], '50': new_row[14], 'cost_other': new_row[15], \
                         'cost_nether': new_row[16], 'Brands': new_row[17], 'NBrands': new_row[18], \
                         'facebook': new_row[19], 'no2': new_row[20], 'no3': new_row[21], 'no4': new_row[22], \
                         'no5': new_row[23], 'count_down': new_row[24], 'limited_time': new_row[25], \
                         'no_limited_time': new_row[26], 'result': 0})
      else:
         print("append result fail!")
      
  
  # 簡易風險檢測之前處理      
  if mode == 1:
    fieldnames = ["https", "http", "nether", "Ame", "Jap", "Ger", "Kor", "UK, Fre", "Other", "coun_nether", "10", "20", "30", "40", "50", "cost_other", "cost_nether", "Brands", "NBrands", "facebook", "no2", "no3", "no4", "no5", "count_down", "limited_time", "no_limited_time", "email", "time", "done"]
    writer = csv.DictWriter(output_f, fieldnames=fieldnames)
    writer.writeheader()
    for row in csv.DictReader(f):
      #i = i + 1
      
      # read row
      feature1 = row['請看到網址的部分，它包含以下哪一種網址？']
      feature2 = row['該商品有提到它是外國商品？']
      feature3 = row['下殺折扣']
      feature4 = row['有無使用品牌名稱']
      feature5 = row['該商品販賣網站為？']
      feature6 = row['有無限時優惠？']

      
      # process row
      new_row = []
      feature1_processing(new_row, feature1)
      feature2_processing(new_row, feature2)
      feature3_processing(new_row, feature3)
      feature4_processing(new_row, feature4)
      feature5_processing(new_row, feature5)
      feature6_processing(new_row, feature6)
      feature_time_processing(new_row, row['時間戳記'])


      # write csv
      writer.writerow({'https': new_row[0], 'http': new_row[1], 'nether': new_row[2], 'Ame': new_row[3], 'Jap': new_row[4], \
                       'Ger': new_row[5], 'Kor': new_row[6], 'UK, Fre': new_row[7], 'Other': new_row[8], 'coun_nether': new_row[9], \
                       '10': new_row[10],'20': new_row[11], '30': new_row[12], '40': new_row[13], '50': new_row[14], 'cost_other': new_row[15], \
                       'cost_nether': new_row[16], 'Brands': new_row[17], 'NBrands': new_row[18], 'facebook': new_row[19], 'no2': new_row[20], \
                       'no3': new_row[21], 'no4': new_row[22], 'no5': new_row[23], 'count_down': new_row[24], 'limited_time': new_row[25], \
                       'no_limited_time': new_row[26], 'email': row['電子郵件地址'], 'time': new_row[27]})
    
    
  output_f.close()
  f.close()    