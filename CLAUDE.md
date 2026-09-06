# Project Structure

* pages: Next.js pages (e.g., /, /about)
* components: Reusable React components
* public: Public assets (e.g., images, fonts)
* data: SQLite database schema and migration files
* utils: Utility functions for the project

# Naming Conventions

* Use PascalCase for file names and directory names
* Use camelCase for variable names and function names
* Use underscores to separate words in constants and enum values

# DB Migration Rules

* Create a new migration by running npx migrate-mysql --create
* Run migrations using migrate-mysql up
* Rollback migrations using migrate-mysql down

# Dev Commands

* Start development environment: npm run dev
* Build production-ready code: npm run build
* Test the project: npm test
* Lint the code: npm run lint

# Patterns to Follow

* Use React Hooks for state management
* Use Next.js API routes for server-side rendering
* Use SQLite transactions for database operations

# Anti-Patterns to Avoid

* Don't mix business logic with UI components
* Don't use global variables or mutable state
* Don't hardcode sensitive information (e.g., API keys)

