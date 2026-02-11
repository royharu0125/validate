# Validator – Data Validation MVP

本專案是一個以 Python 撰寫的資料檢核（Data Validation）模組，
模擬系統在接收使用者資料時，進行基本的欄位完整性與數值合理性驗證。

## 功能說明

目前支援以下驗證規則：

1. 缺少 `age` 欄位
   - 錯誤代碼：`missing_age`
2. `age` 型別錯誤（非整數，或布林值）
   - 錯誤代碼：`age_invalid_type`
3. `age` 數值超出範圍
   - 小於 `min_age` 或大於 `max_age`
   - 錯誤代碼：`age_out_of_range`

## 專案結構

```text
.
├─ validator.py
├─ tests/
│  └─ test_validator.py
└─ README.md
```

## 使用方式

```python
from validator import validate_users

users = [
    {"id": 1, "age": 25},
    {"id": 2},
    {"id": 3, "age": -5},
    {"id": 4, "age": 200},
    {"id": 5, "age": 30},
]

result = validate_users(users)
print(result)
```

## 回傳格式

```python
{
  "total": 5,
  "invalid_count": 3,
  "invalid_users": [
    {"id": 2, "reason": "missing_age"},
    {"id": 3, "reason": "age_out_of_range"},
    {"id": 4, "reason": "age_out_of_range"}
  ]
}
```

## 測試

本專案已提供自動化測試，請執行：

```bash
python -m unittest discover -s tests -p 'test_*.py'
```
