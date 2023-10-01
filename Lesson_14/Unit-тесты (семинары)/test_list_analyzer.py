"""This module contains unit tests for ListAnalyzer class."""

from list_analyzer import ListAnalyzer

class TestListAnalyzer:
    """Test cases for ListAnalyzer."""

    def test_average(self):
        """Test average calculation."""
        analyzer = ListAnalyzer()
        assert analyzer.average([1, 2, 3, 4, 5]) == 3.0

    def test_compare_averages(self):
        """Test comparison of averages."""
        analyzer = ListAnalyzer()
        message = "Второй список имеет большее среднее значение"
        assert analyzer.compare_averages([1, 2, 3], [4, 5, 6]) == message
