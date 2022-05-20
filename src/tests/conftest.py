from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def data() -> Path:
    return Path(__file__).parent / "data"
