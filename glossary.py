from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime

@dataclass
class GlossaryTerm:
    """Represents a term in the glossary."""
    term: str
    definition: str
    created_at: datetime
    updated_at: datetime
    metadata: Dict[str, str]
    related_terms: List[str]

class Glossary:
    """Manages glossary terms and their relationships."""
    
    def __init__(self):
        self.terms: Dict[str, GlossaryTerm] = {}
    
    def add_term(self, term: str, definition: str, metadata: Optional[Dict[str, str]] = None) -> GlossaryTerm:
        """Add a new term to the glossary."""
        if term in self.terms:
            raise ValueError(f"Term '{term}' already exists in the glossary")
        
        now = datetime.utcnow()
        glossary_term = GlossaryTerm(
            term=term,
            definition=definition,
            created_at=now,
            updated_at=now,
            metadata=metadata or {},
            related_terms=[]
        )
        self.terms[term] = glossary_term
        return glossary_term
    
    def get_term(self, term: str) -> Optional[GlossaryTerm]:
        """Retrieve a term from the glossary."""
        return self.terms.get(term)
    
    def update_term(self, term: str, definition: Optional[str] = None, 
                   metadata: Optional[Dict[str, str]] = None) -> GlossaryTerm:
        """Update an existing term in the glossary."""
        if term not in self.terms:
            raise ValueError(f"Term '{term}' does not exist in the glossary")
        
        glossary_term = self.terms[term]
        if definition:
            glossary_term.definition = definition
        if metadata:
            glossary_term.metadata.update(metadata)
        
        glossary_term.updated_at = datetime.utcnow()
        return glossary_term
    
    def add_related_term(self, term: str, related_term: str) -> None:
        """Add a related term relationship."""
        if term not in self.terms:
            raise ValueError(f"Term '{term}' does not exist in the glossary")
        if related_term not in self.terms:
            raise ValueError(f"Related term '{related_term}' does not exist in the glossary")
        
        if related_term not in self.terms[term].related_terms:
            self.terms[term].related_terms.append(related_term)
            self.terms[term].updated_at = datetime.utcnow()
    
    def search_terms(self, query: str) -> List[GlossaryTerm]:
        """Search for terms in the glossary."""
        query = query.lower()
        return [
            term for term in self.terms.values()
            if query in term.term.lower() or query in term.definition.lower()
        ]
    
    def export_glossary(self) -> Dict[str, Dict]:
        """Export the glossary as a dictionary."""
        return {
            term: {
                "definition": term_obj.definition,
                "created_at": term_obj.created_at.isoformat(),
                "updated_at": term_obj.updated_at.isoformat(),
                "metadata": term_obj.metadata,
                "related_terms": term_obj.related_terms
            }
            for term, term_obj in self.terms.items()
        } 