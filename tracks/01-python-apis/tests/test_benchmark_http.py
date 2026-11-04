"""Pure validation tests for the loopback HTTP benchmark utility."""

import pytest

from scripts.benchmark_http import percentile, validate_samples


@pytest.mark.parametrize(
    ("values", "fraction", "expected"),
    [([4.0, 1.0, 3.0, 2.0], 0.5, 2.0), ([1.0, 2.0, 3.0], 0.95, 3.0)],
)
def test_nearest_rank_percentile(
    values: list[float], fraction: float, expected: float
) -> None:
    assert percentile(values, fraction) == expected


@pytest.mark.parametrize("values,fraction", [([], 0.5), ([1.0], 0), ([1.0], 1.1)])
def test_invalid_percentile(values: list[float], fraction: float) -> None:
    with pytest.raises(ValueError):
        percentile(values, fraction)


@pytest.mark.parametrize("iterations,warmup", [(0, 0), (61, 0), (40, 21), (1, -1)])
def test_invalid_sample_counts(iterations: int, warmup: int) -> None:
    with pytest.raises(ValueError):
        validate_samples(iterations, warmup)


def test_valid_sample_count() -> None:
    validate_samples(40, 5)
