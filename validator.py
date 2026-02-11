"""Validator module for user age data."""


def validate_users(users, min_age=1, max_age=120):
    """
    驗證 users 資料是否符合規則。

    參數：
      users: list[dict]，例如 [{"id": 1, "age": 25}, {"id": 2}]
      min_age, max_age: 年齡合法範圍（預設 1~120）

    回傳：
      dict:
        {
          "total": <總筆數>,
          "invalid_count": <不合法筆數>,
          "invalid_users": [
              {"id": <id>, "reason": "missing_age"},
              {"id": <id>, "reason": "age_invalid_type"},
              {"id": <id>, "reason": "age_out_of_range"},
          ]
        }
    """
    total = len(users)
    invalid_users = []

    for user in users:
        # 1) id 防呆
        user_id = user.get("id", None)

        # 2) 缺 age
        if "age" not in user:
            invalid_users.append({"id": user_id, "reason": "missing_age"})
            continue

        age = user["age"]

        # 3) age 型別需為 int，且不接受 bool
        if isinstance(age, bool) or not isinstance(age, int):
            invalid_users.append({"id": user_id, "reason": "age_invalid_type"})
            continue

        # 4) age 超出範圍
        if age < min_age or age > max_age:
            invalid_users.append({"id": user_id, "reason": "age_out_of_range"})

    return {
        "total": total,
        "invalid_count": len(invalid_users),
        "invalid_users": invalid_users,
    }


# 下面這段是「本機測試用」
if __name__ == "__main__":
    users = [
        {"id": 1, "age": 25},
        {"id": 2},
        {"id": 3, "age": -5},
        {"id": 4, "age": 200},
        {"id": 5, "age": 30},
        {"id": 6, "age": "20"},  # 故意放字串測試
        {"age": 10},  # 故意缺 id 測試
        {"id": 7, "age": True},  # 故意放 bool 測試
    ]

    result = validate_users(users)
    print(result)
