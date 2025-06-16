# Contributing to Atlan MCP

Thank you for your interest in contributing to the Atlan MCP project! This document outlines the process for contributing code, documentation, and other improvements.

## Getting Started

1. **Fork the Repository**:  
   Start by forking the [Atlan MCP repository](https://github.com/atlanhq/atlan-mcp) to your GitHub account.

2. **Clone Your Fork**:  
   ```bash
   git clone https://github.com/MandeepCheema/atlan-mcp.git
   cd atlan-mcp
   ```

3. **Set Up Your Development Environment**:  
   - Create a virtual environment:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
     ```
   - Install dependencies:
     ```bash
     pip install -e .
     ```

4. **Create a New Branch**:  
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Making Changes

1. **Write Code**:  
   - Follow the project's coding style and guidelines.
   - Write clear, concise, and well-documented code.

2. **Write Tests**:  
   - Ensure your code is covered by unit tests.
   - Run tests locally:
     ```bash
     python -m unittest discover atlan_mcp/glossary/tests
     ```

3. **Update Documentation**:  
   - Update the README, docstrings, and any relevant documentation.

## Submitting Changes

1. **Commit Your Changes**:  
   ```bash
   git add .
   git commit -m "Add glossary management module with tests and demo"
   ```

2. **Push to Your Fork**:  
   ```bash
   export GITHUB_TOKEN=yourtoken
   git push -u origin feature/glossary-module
   ```

3. **Open a Pull Request**:  
   - Go to the [Atlan MCP repository](https://github.com/atlanhq/atlan-mcp).
   - Click "Compare & pull request".
   - Fill in the PR description, referencing any relevant issues or context.
   - Submit the pull request for review.

## Review Process

- Your PR will be reviewed by the maintainers.
- Address any feedback or requested changes.
- Once approved, your changes will be merged into the main branch.

## Additional Resources

- [Atlan MCP Documentation](https://docs.atlan.com/mcp)
- [Issue Tracker](https://github.com/atlanhq/atlan-mcp/issues)

Thank you for contributing! 