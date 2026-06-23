from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def sample_pdf_path() -> Path:
    return Path(__file__).resolve().parents[1] / "data" / "raw" / "pdf" / "PA - Consolidated lecture notes.pdf"