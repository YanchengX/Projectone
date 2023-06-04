# 實作需求-手動操作薪水紀錄系統

主要功能較為從公司轉型資訊化從紙本帳轉移到電腦
如果作為一般算帳系統比自動打卡更不實用
main -> app..py

## 開發工具跟技術

* MVC framework 作設計
* python-dodx 產生文件
* Pyqt5作GUI
* sqlite(db browser)
* 資料庫設計與操作CRUD，JOIN

------------------------

過程中的想法可以精進學習 or 以薪資系統為目的延伸學習::
* 其他框架的設計優劣MVVM..
* 原始功能設計方針導致bug
* 可以用matlab相關套件實現數據圖
* 有第三方pyqt的modern gui可以使用
* 可以實現ORM代替直接參雜sql指令
* 佈署到雲端將儲存紀錄來達到app更能實際運用
------------------------

使用畫面

![1685874250669](https://github.com/YanchengX/semi-automatic-salary-system/assets/51571103/d44c556a-a9ab-4ece-bec2-d5a7bdb5ace0)


## 可使用功能

* CRUD操作
    * 員工
    * 薪資
    * 設定
    * 日期
* 列表渲染
* 自動計算
    * 個人總額
    * 單月總額
    * 固定項目(勞健保
* 使用者防呆輸入
