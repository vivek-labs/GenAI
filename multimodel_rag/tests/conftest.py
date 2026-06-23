from pathlib import Path
from unittest.mock import Mock, patch

import pytest


@pytest.fixture(scope="session")
def sample_pdf_path() -> Path:
    return Path(__file__).resolve().parents[1] / "data" / "raw" / "pdf" / "PA - Consolidated lecture notes.pdf"


@pytest.fixture
def mock_openai_embedder():
    """Mock OpenAI embedder so tests don't need real API keys."""
    with patch("src.embeddings.openai_embeddings.OpenAI"):
        embedder = Mock()
        # Each text gets a fake embedding (list of 1536 floats)
        embedder.embed = Mock(side_effect=lambda texts: [[0.0] * 1536 for _ in texts])
        yield embedder


@pytest.fixture
def mock_rag_pipeline(mock_openai_embedder):
    """RAG pipeline with mocked OpenAI embedder."""
    from src.rag.rag_pipeline import RAGPipeline
    with patch.object(RAGPipeline, "__init__", lambda self: None):
        rag = RAGPipeline()
        rag.embedder = mock_openai_embedder
        from src.vectorstore.chroma_store import ChromaStore
        rag.vectorstore = ChromaStore()
        yield rag