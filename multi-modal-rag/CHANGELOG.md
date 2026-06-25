# Changelog

## v0.2.0 - 2026-06-26

### Added

- BaseEmbedding abstraction
- BaseVectorStore abstraction
- Dependency Injection support in RAGPipeline
- SentenceChunker implementation
- Sentence overlap support
- Retrieval distance filtering

### Improved

- Retrieval relevance significantly improved
- Reduced noisy context sent to LLM
- Cleaner architecture with interchangeable components

### Fixed

- Multi-page chunking bug
- Early return bug in SentenceChunker
- Retrieval quality degradation caused by overly broad chunks

### Testing

- Added unit tests for SentenceChunker
- Added overlap validation tests
- All tests passing

## v0.1.0 - 2026-06-25

- Initial release of the Multi-Modal RAG project.
- Added PDF extraction, chunking, embedding, retrieval, and answer generation.
- Added automated tests for extraction, chunking, and pipeline retrieval.
- Documented the project with a root README.
