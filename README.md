# Django-first-try
=============================================================

詐騙資料庫

  簡單的回報方式提高民眾回報的可能、圖片展示讓民眾方便記憶、閱覽，
  並藉由可互動的簡易詐騙檢測、可看到貢獻的詐騙特徵蒐集增加回報資訊的想法，
  使用 Google 應用程式、 Django 套件。
  
=============================================================

功能：
  1. web 展示 Google Fusion Table、表單、特徵數據
  2. 表單蒐集詐騙資訊、詐騙特徵
  3. 以表單蒐集簡易詐騙檢測的答案，藉由極限學習機分析其風險，最後以Gmail API回傳結果
  
=============================================================

Demo：
  01_展示資料庫
  https://drive.google.com/open?id=1SDVWOlbnk_vB1RnE_KrTPCTr_q1b4SMO
  02_簡易特徵檢測
  https://drive.google.com/open?id=1AjuRq_o3VXeszJvYx_eV8QRPAG3dlyQT
  03_特徵資料展示
  https://drive.google.com/open?id=1kXVh3qSSJeo_guKpnZqzUi5hp3aF7HGw

=============================================================
未完成：
  1. import data to google fusion table
  2. extract feature data for updating google fusion table 

=============================================================

套件：

  Django 2.0.6, google-api-pythob-client 1.7.3, google-auth 1.5.0, google-auth-httplib2 0.0.3, httplib 0.11.3, pandas 0.23.1, 
  tensorflow 1.8.0
