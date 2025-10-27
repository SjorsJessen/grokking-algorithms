"""JSON Reader."""

from typing import Any
from pathlib import Path
import json

class JSONReader:
    """Read JSON file contents."""
    
    def read_json(path: Path) -> Any | None:
        """Read JSON."""
        with open(path) as f:
            data: Any = json.load(f)
            return data
        return None