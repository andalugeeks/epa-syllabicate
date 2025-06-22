# Makefile for the epa-syllabicate project

.PHONY: help install install-dev test test-verbose test-coverage clean format lint all

# Variables
PYTHON := python3
PIP := pip3
PYTEST := pytest

# Colors for output
GREEN := \033[0;32m
YELLOW := \033[1;33m
NC := \033[0m # No Color

# Default command
help: ## Show this help
	@echo "$(GREEN)Available commands:$(NC)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(YELLOW)%-20s$(NC) %s\n", $$1, $$2}'

install: ## Install basic project dependencies
	@echo "$(GREEN)Installing basic dependencies...$(NC)"
	$(PIP) install -e .

install-dev: ## Install development dependencies
	@echo "$(GREEN)Installing development dependencies...$(NC)"
	$(PIP) install -e ".[dev]"

test: ## Run all tests
	@echo "$(GREEN)Running tests...$(NC)"
	$(PYTEST) tests/

test-verbose: ## Run tests with detailed output
	@echo "$(GREEN)Running tests with detailed output...$(NC)"
	$(PYTEST) -v tests/

test-coverage: ## Run tests with code coverage
	@echo "$(GREEN)Running tests with coverage...$(NC)"
	$(PYTEST) --cov=epa_syllabicate --cov-report=html --cov-report=term tests/

test-watch: ## Run tests in watch mode (requires pytest-watch)
	@echo "$(GREEN)Running tests in watch mode...$(NC)"
	$(PYTEST) --watch tests/

format: ## Format code with black
	@echo "$(GREEN)Formatting code...$(NC)"
	black epa_syllabicate/ tests/

lint: ## Check code format
	@echo "$(GREEN)Checking code format...$(NC)"
	black --check epa_syllabicate/ tests/

clean: ## Clean temporary files
	@echo "$(GREEN)Cleaning temporary files...$(NC)"
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf build/
	rm -rf dist/
	rm -rf .pytest_cache/
	rm -rf htmlcov/
	rm -rf .coverage

build: ## Build the package
	@echo "$(GREEN)Building package...$(NC)"
	$(PYTHON) -m build

all: clean install-dev test ## Run cleanup, installation and tests

# Quick development commands
dev-setup: install-dev ## Quick setup for development
	@echo "$(GREEN)Development setup completed$(NC)"

quick-test: ## Quick test without detailed output
	@$(PYTEST) tests/ -q

# Command to run a specific test
# Usage: make test-file FILE=test_syllabicate.py
test-file: ## Run a specific test file (use FILE=filename)
	@echo "$(GREEN)Running $(FILE)...$(NC)"
	$(PYTEST) tests/$(FILE) -v 