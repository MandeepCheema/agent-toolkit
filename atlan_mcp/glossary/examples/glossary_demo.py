from atlan_mcp.glossary.api.glossary_manager import GlossaryManager

def main():
    # Initialize the glossary manager
    manager = GlossaryManager()
    
    print("=== Creating a Glossary ===")
    # Create a new glossary
    glossary = manager.create_glossary(
        name="Data Governance Glossary",
        description="A comprehensive glossary for data governance terms",
        owner="data_team"
    )
    print(f"Created glossary: {glossary.name} (ID: {glossary.id})")
    
    print("\n=== Creating Categories ===")
    # Create categories
    data_quality = manager.create_category(
        name="Data Quality",
        glossary_id=glossary.id,
        description="Terms related to data quality metrics and processes"
    )
    data_security = manager.create_category(
        name="Data Security",
        glossary_id=glossary.id,
        description="Terms related to data security and privacy"
    )
    print(f"Created categories: {data_quality.name}, {data_security.name}")
    
    print("\n=== Creating Terms ===")
    # Create terms
    data_profiling = manager.create_term(
        name="Data Profiling",
        definition="The process of examining data for quality and consistency",
        category_ids=[data_quality.id]
    )
    data_masking = manager.create_term(
        name="Data Masking",
        definition="The process of obscuring sensitive data",
        category_ids=[data_security.id]
    )
    print(f"Created terms: {data_profiling.name}, {data_masking.name}")
    
    print("\n=== Creating and Associating Assets ===")
    # Create assets and associate them with terms
    customer_table = manager.create_asset(
        name="Customer Table",
        type="TABLE",
        qualified_name="database.schema.customers",
        description="Main customer data table"
    )
    
    # Associate asset with term
    manager.associate_term_with_asset(data_profiling.id, customer_table.id)
    print(f"Associated {customer_table.name} with {data_profiling.name}")
    
    print("\n=== Searching Terms ===")
    # Search for terms
    search_results = manager.search_terms("data")
    print("Search results for 'data':")
    for term in search_results:
        print(f"- {term.name}: {term.definition}")
    
    print("\n=== Exporting Glossary ===")
    # Export the entire glossary
    exported = manager.export_glossary(glossary.id)
    print(f"Glossary '{exported['name']}' contains:")
    print(f"- {len(exported['categories'])} categories")
    for category in exported['categories']:
        print(f"  - {category['name']} ({len(category['terms'])} terms)")
    
    print("\n=== Getting Related Assets ===")
    # Get assets associated with a term
    assets = manager.get_assets_for_term(data_profiling.id)
    print(f"Assets associated with {data_profiling.name}:")
    for asset in assets:
        print(f"- {asset.name} ({asset.type})")

if __name__ == "__main__":
    main() 