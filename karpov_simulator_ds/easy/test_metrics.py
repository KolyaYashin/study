import metrics


def test_profit() -> None:
    """
    For testing profit function
    :return:
    """
    assert metrics.profit([1, 2, 3], [1, 1, 1]) == 3


def test_margin() -> None:
    """
    For testing margin function
    :return:
    """
    assert metrics.margin([1, 2], [1, 2]) == 0
    assert metrics.margin([1, 2, 3], [1, 1, 1]) == 0.5
    # assert metrics.margin([0, 0, 0], [0, 0, 0]) == 0


def test_markup() -> None:
    """
    For testing markup function
    :return:
    """
    assert metrics.markup([0, 0, 3], [0, 0, 2]) == 0.5
    assert metrics.markup([1, 2, 3], [1, 1, 1]) == 1
    # assert metrics.markup([0, 0, 0], [0, 0, 0]) == 0
