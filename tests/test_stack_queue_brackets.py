import pytest
from stack_queue_brackets.stack_queue_brackets import validate_brackets

def test_validate_brackets():
    test_cases = [
        ("{}", True),
        ("{}(){}", True),
        ("()[[Extra Characters]]", True),
        ("(){}[[]]", True),
        ("{}{Code}[Fellows](())", True),
        ("[({}]", False),
        ("(](", False),
        ("{(})", False)
    ]

    for input_str, expected_output in test_cases:
        assert validate_brackets(input_str) == expected_output

    print("All test cases passed.")

test_validate_brackets()

