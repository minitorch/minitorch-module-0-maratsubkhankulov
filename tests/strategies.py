from hypothesis import settings
from hypothesis.strategies import floats, integers

import minitorch

settings.register_profile("ci", deadline=None)
settings.load_profile("ci")


small_ints = integers(min_value=1, max_value=3)
small_floats = floats(min_value=-100, max_value=100, allow_nan=False)
positive_small_floats = floats(min_value=1e2, max_value=100, allow_nan=False)
med_ints = integers(min_value=1, max_value=20)
minus_one_to_one = floats(min_value=-1, max_value=1, allow_nan=False)


def assert_close(a: float, b: float) -> None:
    assert minitorch.operators.is_close(a, b), "Failure x=%f y=%f" % (a, b)
