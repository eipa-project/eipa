# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 11:10:03 2020

@author: Reuel D'silva (@reuelrds)
"""

from pathlib import Path


def printLines(file_path, n=10):
    """Print first n lines from the file.

    Args:
        file_path - A string with Absolute Path to the file.
        n         - Number of lines to be printed.
    """

    with open(file_path, "rb") as datafile:
        for _ in range(n):
            print(datafile.readline())


if __name__ == "__main__":
    path = Path.cwd()
    fp = path / "data" / "cornell movie-dialogs corpus" / "movie_line.txt"
    print(fp)
    printLines(fp)
