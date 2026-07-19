from abc import ABC, abstractmethod
from typing import List

from src.models.document import Document

class BaseExtractor(ABC):

    @abstractmethod
    def extract(self, file_path: str) -> List[Document]:
        pass