# from abc import ABC, abstractmethod
# from typing import List

# class BaseLoader(ABC):
#     @abstractmethod
#     def load(self) -> List[str]:
#         """Return raw text documents"""
#         pass


from abc import ABC, abstractmethod
from typing import List, Dict


class BaseLoader(ABC):
    @abstractmethod
    def load(self) -> List[Dict]:
        """
        Return documents in standardized format:
        {
            "text": str,
            "source": str,
            "type": str
        }
        """
        pass
