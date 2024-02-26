from project import check_correct_args, select_house, select_grade
import pytest

def test_check_correct_args():
    with pytest.raises(SystemExit):
        check_correct_args()



def test_select_house():
    assert select_house("courage") == "Gryffindor"
    assert select_house("dedication") == "Hufflepuff"
    assert select_house("wisdom") == "Ravenclaw"
    assert select_house("ambition") == "Slytherin"


def test_select_grade():
    assert select_grade(2005) == "Grade 12"
    assert select_grade(2015) == "Grade 2"

