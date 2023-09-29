"""This module contains ListAnalyzer class for analyzing lists."""

class ListAnalyzer:
    """Class to analyze lists and compare their averages."""

    @staticmethod
    def average(lst):
        """Calculate average of a list."""
        return sum(lst) / len(lst)

    def compare_averages(self, list1, list2):
        """Compare averages of two lists and return message."""
        avg1 = self.average(list1)
        avg2 = self.average(list2)

        if avg1 > avg2:
            return "Первый список имеет большее среднее значение"
        if avg2 > avg1:
            return "Второй список имеет большее среднее значение"

        return "Средние значения равны"
