from typing import Dict, List, Optional, Set
from dataclasses import dataclass, field
from datetime import datetime
from .base import BaseModel

@dataclass(kw_only=True)
class Asset(BaseModel):
    """Represents an asset in the system."""
    name: str
    type: str
    qualified_name: str
    description: Optional[str] = None
    owner: Optional[str] = None
    tags: List[str] = field(default_factory=list)

@dataclass(kw_only=True)
class Term(BaseModel):
    """Represents a business term in the glossary."""
    name: str
    definition: str
    status: str = "DRAFT"  # DRAFT, APPROVED, DEPRECATED
    category_ids: Set[str] = field(default_factory=set)
    asset_ids: Set[str] = field(default_factory=set)
    related_term_ids: Set[str] = field(default_factory=set)

    def to_dict(self) -> Dict:
        """Convert term to dictionary representation."""
        base_dict = super().to_dict()
        base_dict.update({
            "name": self.name,
            "definition": self.definition,
            "category_ids": list(self.category_ids),
            "asset_ids": list(self.asset_ids),
            "related_term_ids": list(self.related_term_ids),
            "status": self.status
        })
        return base_dict

@dataclass(kw_only=True)
class Category(BaseModel):
    """Represents a category in the glossary."""
    name: str
    description: Optional[str] = None
    parent_id: Optional[str] = None
    term_ids: Set[str] = field(default_factory=set)
    child_category_ids: Set[str] = field(default_factory=set)

    def to_dict(self) -> Dict:
        """Convert category to dictionary representation."""
        base_dict = super().to_dict()
        base_dict.update({
            "name": self.name,
            "description": self.description,
            "parent_id": self.parent_id,
            "term_ids": list(self.term_ids),
            "child_category_ids": list(self.child_category_ids)
        })
        return base_dict

@dataclass(kw_only=True)
class Glossary(BaseModel):
    """Represents a glossary in the system."""
    name: str
    description: Optional[str] = None
    owner: Optional[str] = None
    status: str = "ACTIVE"  # ACTIVE, ARCHIVED
    category_ids: Set[str] = field(default_factory=set)

    def to_dict(self) -> Dict:
        """Convert glossary to dictionary representation."""
        base_dict = super().to_dict()
        base_dict.update({
            "name": self.name,
            "description": self.description,
            "category_ids": list(self.category_ids),
            "owner": self.owner,
            "status": self.status
        })
        return base_dict 