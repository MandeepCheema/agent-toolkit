import unittest
from datetime import datetime
from glossary import Glossary, GlossaryTerm

class TestGlossary(unittest.TestCase):
    def setUp(self):
        self.glossary = Glossary()
        
    def test_add_term(self):
        term = self.glossary.add_term(
            "API",
            "Application Programming Interface - A set of rules that allows programs to talk to each other",
            {"category": "Technology", "source": "Wikipedia"}
        )
        
        self.assertIsInstance(term, GlossaryTerm)
        self.assertEqual(term.term, "API")
        self.assertIn("Technology", term.metadata["category"])
        self.assertEqual(len(term.related_terms), 0)
        
    def test_duplicate_term(self):
        self.glossary.add_term("API", "Initial definition")
        with self.assertRaises(ValueError):
            self.glossary.add_term("API", "Another definition")
            
    def test_update_term(self):
        self.glossary.add_term("API", "Initial definition")
        updated_term = self.glossary.update_term(
            "API",
            definition="Updated definition",
            metadata={"new_field": "value"}
        )
        
        self.assertEqual(updated_term.definition, "Updated definition")
        self.assertEqual(updated_term.metadata["new_field"], "value")
        
    def test_add_related_term(self):
        self.glossary.add_term("API", "API definition")
        self.glossary.add_term("REST", "REST definition")
        
        self.glossary.add_related_term("API", "REST")
        term = self.glossary.get_term("API")
        
        self.assertIn("REST", term.related_terms)
        
    def test_search_terms(self):
        self.glossary.add_term("API", "Application Programming Interface")
        self.glossary.add_term("REST API", "Representational State Transfer API")
        
        results = self.glossary.search_terms("api")
        self.assertEqual(len(results), 2)
        
        results = self.glossary.search_terms("rest")
        self.assertEqual(len(results), 1)
        
    def test_export_glossary(self):
        self.glossary.add_term("API", "API definition")
        exported = self.glossary.export_glossary()
        
        self.assertIn("API", exported)
        self.assertEqual(exported["API"]["definition"], "API definition")
        self.assertIsInstance(exported["API"]["created_at"], str)
        self.assertIsInstance(exported["API"]["updated_at"], str)

if __name__ == '__main__':
    unittest.main() 