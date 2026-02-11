import unittest

from validator import validate_users


class ValidateUsersTests(unittest.TestCase):
    def test_all_valid_users(self):
        users = [{"id": 1, "age": 18}, {"id": 2, "age": 35}]

        result = validate_users(users)

        self.assertEqual(result["total"], 2)
        self.assertEqual(result["invalid_count"], 0)
        self.assertEqual(result["invalid_users"], [])

    def test_missing_age(self):
        users = [{"id": 10}]

        result = validate_users(users)

        self.assertEqual(
            result["invalid_users"],
            [{"id": 10, "reason": "missing_age"}],
        )

    def test_boundary_values(self):
        users = [{"id": 1, "age": 1}, {"id": 2, "age": 120}]

        result = validate_users(users)

        self.assertEqual(result["invalid_count"], 0)

    def test_out_of_range_values(self):
        users = [{"id": 1, "age": 0}, {"id": 2, "age": 121}]

        result = validate_users(users)

        self.assertEqual(
            result["invalid_users"],
            [
                {"id": 1, "reason": "age_out_of_range"},
                {"id": 2, "reason": "age_out_of_range"},
            ],
        )

    def test_invalid_types_including_bool(self):
        users = [
            {"id": 1, "age": "20"},
            {"id": 2, "age": None},
            {"id": 3, "age": True},
            {"id": 4, "age": False},
        ]

        result = validate_users(users)

        self.assertEqual(
            result["invalid_users"],
            [
                {"id": 1, "reason": "age_invalid_type"},
                {"id": 2, "reason": "age_invalid_type"},
                {"id": 3, "reason": "age_invalid_type"},
                {"id": 4, "reason": "age_invalid_type"},
            ],
        )

    def test_missing_id_returns_none(self):
        users = [{"age": "x"}]

        result = validate_users(users)

        self.assertEqual(
            result["invalid_users"],
            [{"id": None, "reason": "age_invalid_type"}],
        )


if __name__ == "__main__":
    unittest.main()
