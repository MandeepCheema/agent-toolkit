"""
Atlan MCP Glossary Module

This module provides functionality for managing glossaries, categories, terms,
and their associations with assets in the Atlan Model Context Protocol (MCP).
"""

from .api.glossary_manager import GlossaryManager
from .models.entities import Glossary, Category, Term, Asset
from .models.base import BaseModel

__version__ = "0.1.0"
__all__ = [
    "GlossaryManager",
    "Glossary",
    "Category",
    "Term",
    "Asset",
    "BaseModel"
] 