# Atlan MCP Glossary Module

This module provides a comprehensive glossary management system for the Atlan MCP project. It allows users to create, update, and associate terms with assets, as well as search and export glossary data.

## Features

- **Glossary Management**: Create and manage glossaries with categories and terms.
- **Term Association**: Associate terms with assets and other terms.
- **Search Functionality**: Search for terms, categories, and assets.
- **Export Capabilities**: Export glossary data for reporting and analysis.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/atlanhq/atlan-mcp.git
   cd atlan-mcp
   ```

2. **Set Up Your Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -e .
   ```

## Usage

### Example

```python
from atlan_mcp.glossary.api.glossary_manager import GlossaryManager

# Initialize the glossary manager
manager = GlossaryManager()

# Create a new glossary
glossary = manager.create_glossary(
    name="Data Governance Glossary",
    description="A comprehensive glossary for data governance terms",
    owner="data_team"
)

# Create a category
category = manager.create_category(
    name="Data Quality",
    glossary_id=glossary.id,
    description="Terms related to data quality metrics and processes"
)

# Create a term
term = manager.create_term(
    name="Data Profiling",
    definition="The process of examining data for quality and consistency",
    category_ids=[category.id]
)

# Associate a term with an asset
asset = manager.create_asset(
    name="Customer Table",
    type="TABLE",
    qualified_name="database.schema.customers"
)
manager.associate_term_with_asset(term.id, asset.id)

# Search for terms
search_results = manager.search_terms("data")
for term in search_results:
    print(f"- {term.name}: {term.definition}")

# Export the glossary
exported = manager.export_glossary(glossary.id)
print(exported)
```

## Testing

Run the unit tests:
```bash
python -m unittest discover atlan_mcp/glossary/tests
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 