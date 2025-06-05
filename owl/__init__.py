"""
OWL: Optimized Workforce Learning for General Multi-Agent Assistance in Real-World Task Automation

This package provides a framework for multi-agent collaboration that pushes the boundaries of task automation.
"""

__version__ = "0.0.1"

# Import key components for easier access
from owl.utils import (
    run_society,
    arun_society,
    OwlRolePlaying,
    OwlGAIARolePlaying,
    DocumentProcessingToolkit,
    extract_pattern,
)

__all__ = [
    "run_society",
    "arun_society",
    "OwlRolePlaying",
    "OwlGAIARolePlaying",
    "DocumentProcessingToolkit",
    "extract_pattern",
] 