import re
class IgnoreFilter:
    """
    Ignore string that does not match the patterns:
        1. ignore version start with 0.
        2. ignore version name not all digits (e,g, 1.2.3b / 1.2.3.dev123))
        3. ignore version name with no '.' mark in it.
        4. ignore version with first number having more than 4 digit (12313245.1232.4)
        5. ignore version start with v
    """

    def __init__(self, regex: str):
        self._pattern = re.compile(regex)

    def connect(self, input_generator):
        return filter(self._pattern.match, input_generator)


ignore_filter = IgnoreFilter(r"^[1-9]\d{0,3}(\.\d+)+$")
