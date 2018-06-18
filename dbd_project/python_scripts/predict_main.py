from model import ELM
import tensorflow as tf
import preprocessing
import time
import pandas as pd
import gmail_api as gma
import text_generation as textg
import download_file_api as dfa
import csv

def main():
  # Basic tf setting
  tf.set_random_seed(2018)
  sess = tf.Session()

  # Download files
  #詐騙特徵
  dfa.download_csv("1ckDsJdBaGTGwVbtUQAxvUTfjYX190TnNS9fjgtPfbBM", "詐騙特徵蒐集.csv")
  #簡易詐騙檢測
  dfa.download_csv("1Vx98ErRq4W8AgnBMhoElrA33J76_SAGCd4TrY5M0fp8", "簡易詐騙風險檢測.csv")


  # Fetch data
  t1 = time.time()
  preprocessing.feature_preprocessing("詐騙特徵蒐集.csv", "training_feature.csv", 0)
  t2 = time.time()
  fetch_time = t2 - t1
  
  train_data = pd.read_csv('training_feature.csv')
  train_x = train_data[["https", "http", "nether", "Ame", "Jap", "Ger", "Kor", "UK, Fre", "Other", "coun_nether", "10", "20", "30", "40", "50", "cost_other", "cost_nether", "Brands", "NBrands", "facebook", "no2", "no3", "no4", "no5", "count_down", "limited_time", "no_limited_time"]]
  #train_x = train_x.value
  train_x = train_x.as_matrix()
  train_n = len(train_x)
 

  # Construct ELM
  batch_size = train_n
  hidden_num = 10
  print("batch_size : {}".format(batch_size))
  print("hidden_num : {}".format(hidden_num))
  elm = ELM(sess, batch_size, 27, hidden_num, 1)

  # one-step feed-forward training
  t1 = time.time()
  """
  train_data = pd.read_csv('training_feature.csv')
  train_x = train_data[["https", "http", "nether", "Ame", "Jap", "Ger", "Kor", "UK, Fre", "Other", "coun_nether", "10", "20", "30", "40", "50", "cost_other", "cost_nether", "Brands", "NBrands", "facebook", "no2", "no3", "no4", "no5", "count_down", "limited_time", "no_limited_time"]]
  #train_x = train_x.value
  train_x = train_x.as_matrix()
  """
  train_y = train_data["result"]
  #train_y = train_y.value
  train_y = train_y.as_matrix()
  train_y = train_y.reshape(train_n, 1)
  elm.feed(train_x, train_y)

  t2 = time.time()
  feeding_time = t2 -t1

  # testing
  t1 = time.time()
  preprocessing.feature_preprocessing("簡易詐騙風險檢測.csv", "feature.csv", 1)
  test_feature = pd.read_csv('feature.csv')
  test_feature = test_feature[["https", "http", "nether", "Ame", "Jap", "Ger", "Kor", "UK, Fre", "Other", "coun_nether", "10", "20", "30", "40", "50", "cost_other", "cost_nether", "Brands", "NBrands", "facebook", "no2", "no3", "no4", "no5", "count_down", "limited_time", "no_limited_time"]]
  #test_feature = test_feature.value
  test_feature = test_feature.as_matrix()

  elm.test(test_feature)
  t2 = time.time()
  testing_time = t2 - t1

  #convert to csv
  result = (elm._result)
  test_n = len(result)
  result = result.reshape(test_n, )
  result = pd.Series(result)

  temp_file= pd.read_csv('feature.csv')
  date = temp_file['time']
  address = temp_file['email']
  final_result = pd.concat([result, date, address], axis = 1)
  final_result.to_csv('final_result.csv')


  #send mail
  t1 = time.time()
  fr = open('final_result.csv', "r")
  for row in csv.DictReader(fr):
    result2text = float(row['0'])
    time2text = row['time']
    address = row['email']
    textgz = textg.textg(result2text, time2text)
    if address != "":
      gma.main(address, textgz)
    time.sleep(2)
  t2 = time.time()
  sending_mail_time = t2 - t1

  #Time
  print("Fetching data time is %.2f second." % fetch_time)
  print("Feeding time is %.2f second." % feeding_time)
  print("Testing time is %.2f second." % testing_time)
  print("Sending mail time is %.2f second." % sending_mail_time)


if __name__ == '__main__':
  main()