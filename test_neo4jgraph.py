# test_neo4jgraph.py
"""
Tests for Neo4jGraph module.
"""

import unittest
from neo4jgraph import Neo4jGraph

class TestNeo4jGraph(unittest.TestCase):
    """Test cases for Neo4jGraph class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = Neo4jGraph()
        self.assertIsInstance(instance, Neo4jGraph)
        
    def test_run_method(self):
        """Test the run method."""
        instance = Neo4jGraph()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
