# a way overboard bowling score tester:
import pytest
from python_bowler import bowling_score

def test_scores():
    games = [['XXXXXXXXXXXX', 300],
             ['9-9-9-9-9-9-9-9-9-9-', 90],
             ['5/5/5/5/5/5/5/5/5/5/5', 150],
             ['X7/9-X-88/-6XXX81', 167]]

    for i in games:
        assert bowling_score(i[0]) == i[1]
