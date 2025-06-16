from typing import Dict, List, Optional, Set, Union
from datetime import datetime
from ..models.entities import Glossary, Category, Term, Asset
from ..models.base import BaseModel

class GlossaryManager:
    """Manages glossaries, categories, terms, and their associations with assets."""

    def __init__(self):
        self.glossaries: Dict[str, Glossary] = {}
        self.categories: Dict[str, Category] = {}
        self.terms: Dict[str, Term] = {}
        self.assets: Dict[str, Asset] = {}

    # Glossary Operations
    def create_glossary(self, name: str, description: Optional[str] = None, 
                       owner: Optional[str] = None) -> Glossary:
        """Create a new glossary."""
        glossary = Glossary(name=name, description=description, owner=owner)
        self.glossaries[glossary.id] = glossary
        return glossary

    def get_glossary(self, glossary_id: str) -> Optional[Glossary]:
        """Retrieve a glossary by ID."""
        return self.glossaries.get(glossary_id)

    def update_glossary(self, glossary_id: str, **kwargs) -> Optional[Glossary]:
        """Update a glossary."""
        glossary = self.glossaries.get(glossary_id)
        if not glossary:
            return None
        
        for key, value in kwargs.items():
            if hasattr(glossary, key):
                setattr(glossary, key, value)
        
        glossary.updated_at = datetime.utcnow()
        return glossary

    # Category Operations
    def create_category(self, name: str, glossary_id: str, 
                       description: Optional[str] = None,
                       parent_id: Optional[str] = None) -> Optional[Category]:
        """Create a new category in a glossary."""
        if glossary_id not in self.glossaries:
            raise ValueError(f"Glossary with ID {glossary_id} does not exist")
        
        category = Category(name=name, description=description, parent_id=parent_id)
        self.categories[category.id] = category
        self.glossaries[glossary_id].category_ids.add(category.id)
        
        if parent_id and parent_id in self.categories:
            self.categories[parent_id].child_category_ids.add(category.id)
        
        return category

    def get_category(self, category_id: str) -> Optional[Category]:
        """Retrieve a category by ID."""
        return self.categories.get(category_id)

    # Term Operations
    def create_term(self, name: str, definition: str, 
                   category_ids: Optional[List[str]] = None) -> Term:
        """Create a new term."""
        term = Term(name=name, definition=definition)
        if category_ids:
            term.category_ids.update(category_ids)
            for category_id in category_ids:
                if category_id in self.categories:
                    self.categories[category_id].term_ids.add(term.id)
        
        self.terms[term.id] = term
        return term

    def get_term(self, term_id: str) -> Optional[Term]:
        """Retrieve a term by ID."""
        return self.terms.get(term_id)

    def update_term(self, term_id: str, **kwargs) -> Optional[Term]:
        """Update a term."""
        term = self.terms.get(term_id)
        if not term:
            return None
        
        for key, value in kwargs.items():
            if hasattr(term, key):
                setattr(term, key, value)
        
        term.updated_at = datetime.utcnow()
        return term

    # Asset Operations
    def create_asset(self, name: str, type: str, qualified_name: str,
                    description: Optional[str] = None,
                    owner: Optional[str] = None) -> Asset:
        """Create a new asset."""
        asset = Asset(name=name, type=type, qualified_name=qualified_name,
                     description=description, owner=owner)
        self.assets[asset.id] = asset
        return asset

    def associate_term_with_asset(self, term_id: str, asset_id: str) -> bool:
        """Associate a term with an asset."""
        if term_id not in self.terms or asset_id not in self.assets:
            return False
        
        self.terms[term_id].asset_ids.add(asset_id)
        return True

    # Search Operations
    def search_terms(self, query: str) -> List[Term]:
        """Search for terms by name or definition."""
        query = query.lower()
        return [
            term for term in self.terms.values()
            if query in term.name.lower() or query in term.definition.lower()
        ]

    def search_categories(self, query: str) -> List[Category]:
        """Search for categories by name or description."""
        query = query.lower()
        return [
            category for category in self.categories.values()
            if query in category.name.lower() or 
               (category.description and query in category.description.lower())
        ]

    def search_glossaries(self, query: str) -> List[Glossary]:
        """Search for glossaries by name or description."""
        query = query.lower()
        return [
            glossary for glossary in self.glossaries.values()
            if query in glossary.name.lower() or 
               (glossary.description and query in glossary.description.lower())
        ]

    def get_assets_for_term(self, term_id: str) -> List[Asset]:
        """Get all assets associated with a term."""
        if term_id not in self.terms:
            return []
        return [self.assets[aid] for aid in self.terms[term_id].asset_ids if aid in self.assets]

    def get_terms_for_asset(self, asset_id: str) -> List[Term]:
        """Get all terms associated with an asset."""
        return [
            term for term in self.terms.values()
            if asset_id in term.asset_ids
        ]

    # Export Operations
    def export_glossary(self, glossary_id: str) -> Dict:
        """Export a glossary as a dictionary."""
        glossary = self.get_glossary(glossary_id)
        if not glossary:
            return {}
        return {
            "name": glossary.name,
            "description": glossary.description,
            "owner": glossary.owner,
            "categories": [
                {
                    "name": self.categories[cat_id].name,
                    "description": self.categories[cat_id].description,
                    "terms": [
                        {
                            "name": self.terms[term_id].name,
                            "definition": self.terms[term_id].definition,
                            "status": self.terms[term_id].status
                        }
                        for term_id in self.categories[cat_id].term_ids
                        if term_id in self.terms
                    ]
                }
                for cat_id in glossary.category_ids
                if cat_id in self.categories
            ]
        } 