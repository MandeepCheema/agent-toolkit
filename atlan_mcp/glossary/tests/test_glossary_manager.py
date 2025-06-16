import unittest
from datetime import datetime
from atlan_mcp.glossary.api.glossary_manager import GlossaryManager
from atlan_mcp.glossary.models.entities import Glossary, Category, Term, Asset

class TestGlossaryManager(unittest.TestCase):
    def setUp(self):
        self.manager = GlossaryManager()
        
    def test_create_and_get_glossary(self):
        # Create a glossary
        glossary = self.manager.create_glossary(
            name="Test Glossary",
            description="A test glossary",
            owner="test_user"
        )
        
        self.assertIsInstance(glossary, Glossary)
        self.assertEqual(glossary.name, "Test Glossary")
        
        # Get the glossary
        retrieved = self.manager.get_glossary(glossary.id)
        self.assertEqual(retrieved, glossary)
        
    def test_create_and_get_category(self):
        # Create a glossary first
        glossary = self.manager.create_glossary(name="Test Glossary")
        
        # Create a category
        category = self.manager.create_category(
            name="Test Category",
            glossary_id=glossary.id,
            description="A test category"
        )
        
        self.assertIsInstance(category, Category)
        self.assertEqual(category.name, "Test Category")
        self.assertIn(category.id, glossary.category_ids)
        
        # Get the category
        retrieved = self.manager.get_category(category.id)
        self.assertEqual(retrieved, category)
        
    def test_create_and_get_term(self):
        # Create a term
        term = self.manager.create_term(
            name="Test Term",
            definition="A test term definition"
        )
        
        self.assertIsInstance(term, Term)
        self.assertEqual(term.name, "Test Term")
        self.assertEqual(term.definition, "A test term definition")
        
        # Get the term
        retrieved = self.manager.get_term(term.id)
        self.assertEqual(retrieved, term)
        
    def test_term_category_association(self):
        # Create a glossary and category
        glossary = self.manager.create_glossary(name="Test Glossary")
        category = self.manager.create_category(name="Test Category", glossary_id=glossary.id)
        
        # Create a term in the category
        term = self.manager.create_term(
            name="Test Term",
            definition="A test term",
            category_ids=[category.id]
        )
        
        self.assertIn(term.id, category.term_ids)
        self.assertIn(category.id, term.category_ids)
        
    def test_term_asset_association(self):
        # Create a term and an asset
        term = self.manager.create_term(name="Test Term", definition="A test term")
        asset = self.manager.create_asset(
            name="Test Asset",
            type="TABLE",
            qualified_name="test.asset"
        )
        
        # Associate them
        success = self.manager.associate_term_with_asset(term.id, asset.id)
        self.assertTrue(success)
        
        # Check the association
        assets = self.manager.get_assets_for_term(term.id)
        self.assertEqual(len(assets), 1)
        self.assertEqual(assets[0], asset)
        
        terms = self.manager.get_terms_for_asset(asset.id)
        self.assertEqual(len(terms), 1)
        self.assertEqual(terms[0], term)
        
    def test_search_operations(self):
        # Create test data
        glossary = self.manager.create_glossary(name="Test Glossary")
        category = self.manager.create_category(name="Test Category", glossary_id=glossary.id)
        term = self.manager.create_term(
            name="Test Term",
            definition="A test term definition",
            category_ids=[category.id]
        )
        
        # Test glossary search
        glossaries = self.manager.search_glossaries("Test")
        self.assertEqual(len(glossaries), 1)
        self.assertEqual(glossaries[0], glossary)
        
        # Test category search
        categories = self.manager.search_categories("Test")
        self.assertEqual(len(categories), 1)
        self.assertEqual(categories[0], category)
        
        # Test term search
        terms = self.manager.search_terms("Test")
        self.assertEqual(len(terms), 1)
        self.assertEqual(terms[0], term)
        
    def test_export_glossary(self):
        # Create test data
        glossary = self.manager.create_glossary(name="Test Glossary")
        category = self.manager.create_category(name="Test Category", glossary_id=glossary.id)
        term = self.manager.create_term(
            name="Test Term",
            definition="A test term",
            category_ids=[category.id]
        )
        
        # Export the glossary
        exported = self.manager.export_glossary(glossary.id)
        
        self.assertIsNotNone(exported)
        self.assertEqual(exported["name"], "Test Glossary")
        self.assertEqual(len(exported["categories"]), 1)
        self.assertEqual(exported["categories"][0]["name"], "Test Category")
        self.assertEqual(len(exported["categories"][0]["terms"]), 1)
        self.assertEqual(exported["categories"][0]["terms"][0]["name"], "Test Term")

if __name__ == '__main__':
    unittest.main() 