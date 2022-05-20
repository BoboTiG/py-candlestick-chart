import pytest

from candlestick_chart import utils


@pytest.mark.parametrize(
    "value, expected",
    [
        (0, "0"),
        (0.0, "0.00"),
        (123456789, "123,456,789"),
        (1.23456789, "1.23"),
        (1.23456789, "1.23"),
        (1234.56789, "1,234.57"),
        (0.1, "0.1000"),
        (0.01, "0.0100"),
        (0.001, "0.0010"),
        (0.0001, "0.0001"),
        (0.00001, "0.⦗0×4⦘1000"),
        (0.000001, "0.⦗0×5⦘1000"),
        (0.0000001, "0.⦗0×6⦘1000"),
        (0.000000000012340000, "0.⦗0×10⦘1234"),
        (0.000000000012345678, "0.⦗0×10⦘1234"),
        (0.123456789, "0.1235"),
    ],
)
def test_fnum(value, expected):
    assert utils.fnum(value) == expected
    assert utils.fnum(str(value)) == expected
    if value != 0.0:
        assert utils.fnum(value * -1) == f"-{expected}"
