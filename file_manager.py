import os
import pickle
from typing import Any


class FileManager:
    @staticmethod
    def exists(f_path: str) -> bool:
        return os.path.exists(f_path)

    @staticmethod
    def dump(f_path: str, obj: Any) -> None:
        with open(f_path, "wb") as f:
            pickle.dump(obj, f)

    @staticmethod
    def load(f_path: str) -> Any:
        with open(f_path, "rb") as f:
            return pickle.load(f)

    @staticmethod
    def remove(f_path: str) -> None:
        os.remove(f_path)
