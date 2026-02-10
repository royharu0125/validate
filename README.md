\# Validator – Data Validation MVP



本專案是一個以 Python 撰寫的資料檢核（Data Validation）模組，

模擬系統在接收使用者資料時，進行基本的欄位完整性與數值合理性驗證。



本專案著重於「系統維運與後端資料處理」常見的核心邏輯，

適合作為內部系統、API 前處理或批次資料檢核的基礎模組。



---



\## 專案背景與目的



在系統維運與後端服務中，資料品質是穩定度的第一道防線。

實務上常會遇到以下問題：



\- 欄位缺失導致系統錯誤

\- 使用者輸入不合理的數值

\- 資料格式不一致，影響後續流程



本專案的目的在於練習：

\- 將實務需求轉換為可重複使用的驗證邏輯

\- 對資料異常進行分類與整理

\- 回傳結構化結果，利於系統或人員後續處理



---



\## 功能說明



目前支援以下驗證規則：



1\. 缺少 age 欄位  

&nbsp;  - 錯誤原因：missing\_age



2\. age 數值不合法  

&nbsp;  - age < 1 或 age > 120  

&nbsp;  - age 非整數型別  

&nbsp;  - 錯誤原因：age\_out\_of\_range



驗證結果會依照資料出現順序回傳，方便除錯與後續處理。



---



\## 專案結構



&nbsp;   validator/ 

&nbsp;├─ validator.py

&nbsp;└─ README.md



---



\## 使用方式



\### 範例資料



users = \[

&nbsp;   {"id": 1, "age": 25},

&nbsp;   {"id": 2},

&nbsp;   {"id": 3, "age": -5},

&nbsp;   {"id": 4, "age": 200},

&nbsp;   {"id": 5, "age": 30}

]



\### 呼叫驗證函式



from validator import validate\_users



result = validate\_users(users)

print(result)



---



\## 回傳格式說明



{

&nbsp; "total": 5,

&nbsp; "invalid\_count": 3,

&nbsp; "invalid\_users": \[

&nbsp;   {"id": 2, "reason": "missing\_age"},

&nbsp;   {"id": 3, "reason": "age\_out\_of\_range"},

&nbsp;   {"id": 4, "reason": "age\_out\_of\_range"}

&nbsp; ]

}



---



\## 回傳欄位說明



\- total  

&nbsp; 輸入資料的總筆數



\- invalid\_count  

&nbsp; 不合法資料的筆數



\- invalid\_users  

&nbsp; 不合法資料清單，每一筆包含：

&nbsp; - id：使用者識別碼

&nbsp; - reason：錯誤原因說明



---



\## 設計重點



\- 使用 list 與 dict 處理結構化資料

\- 明確區分資料缺失與數值異常

\- 使用 continue 控制流程，避免不必要的判斷

\- 回傳結構化結果，方便系統串接與維運除錯



---



\## 適用場景



\- 系統資料前處理（Pre-processing）

\- API 輸入驗證

\- 批次資料檢核

\- 系統維運與資料品質檢查



---



\## 後續可擴充方向



\- 增加更多驗證規則（例如其他欄位檢查）

\- 將驗證邏輯模組化

\- 包裝成 API 服務（例如 FastAPI）

\- 串接資料庫或檔案來源



---



\## 備註



本專案為學習與作品集用途，

著重於系統邏輯與資料處理流程的建立，

可依實際需求進行語言或框架的轉換與擴充。



