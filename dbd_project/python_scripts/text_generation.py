def textg(result, date):
  #f = open('text_generation.txt','w')
  outcome = ''
  if result < 1 and result >= 0.65:
    outcome = "高風險"
  elif result >= 0.61 and result < 0.65: 
    outcome = "中風險"
  elif result < 0.61 and result >= 0:
    outcome = "低風險"
  else:
    print("風險偵測出現錯誤")
    
  msg = '您好：<br><br>您於 %s 填寫的簡易特徵檢測結果出來了！<br>您檢測的結果為： %s<br><br>歡迎您的下次使用！' % (date, outcome)
  #f.write('您好：\n\n您於 %s 填寫的簡易特徵檢測結果出來了！\n您檢測的結果為： %s\n歡迎您的下次使用！' % (date, outcome))
  #f.write('hi\n%s\nthank' % outcome)
  return msg
  
  #f.close()
if __name__ == '__textg__':
  textg()