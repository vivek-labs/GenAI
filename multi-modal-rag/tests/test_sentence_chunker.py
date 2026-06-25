from src.chunking.sentence_chunker import SentenceChunker
from src.models.document import Document
from src.models.metadata import DocumentMetadata


def test_sentence_chunker_creates_chunks_without_cutting_sentences():
    document = Document(
        document_id="doc1",
        text=(
            "This is sentence one. "
            "This is sentence two. "
            "This is sentence three. "
            "This is sentence four."
        ),
        metadata=DocumentMetadata(
            source_file="test.pdf",
            file_type="pdf",
            page_number=1
        )
    )

    chunker = SentenceChunker(chunk_size=30)

    chunks = chunker.chunk([document])

    assert len(chunks) > 1
    assert all(chunk.text.strip().endswith(".") for chunk in chunks)
    assert all(len(chunk.text) <= 80 for chunk in chunks)

#multi-document test
def test_sentence_chunker_processes_all_documents():
    documents = [
        Document(
            document_id="doc1",
            text="Page one sentence one. Page one sentence two.",
            metadata=DocumentMetadata(
                source_file="test.pdf",
                file_type="pdf",
                page_number=1
            )
        ),
        Document(
            document_id="doc2",
            text="Page two sentence one. Page two sentence two.",
            metadata=DocumentMetadata(
                source_file="test.pdf",
                file_type="pdf",
                page_number=2
            )
        ),
    ]

    chunker = SentenceChunker(chunk_size=40)

    chunks = chunker.chunk(documents)

    pages = {chunk.metadata.page_number for chunk in chunks}

    assert pages == {1, 2}