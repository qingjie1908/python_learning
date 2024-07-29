import pytest
from survey import AnonymousSurvey

@pytest.fixture
# We apply the @pytest.fixture decorator to the new function language_survey()
# When a parameter in a test function matches the name of a function with the @pytest.fixture decorator,
# the fixture will be run automatically and the return value will be passed to the test function
def language_survey():
    """A survey that will be available to all test functions."""
    question = "What language did you first learn to speak?"
    language_survey_arg = AnonymousSurvey(question)
    return language_survey_arg

def test_store_single_response(language_survey): #run fixture language_survey func, and now parameter language_survey = language_survey_arg
    """Test that a single response is stored properly."""
    # question = "What nguage did you first learn to speak?"
    # language_survey = AnonymousSurvey(question)
    language_survey.store_reponse('English')
    assert 'English' in language_survey.responses

# pytest test_survey.py
# ========================= test session starts =========================
# platform darwin -- Python 3.12.4, pytest-8.3.2, pluggy-1.5.0
# rootdir: /Users/qingjie/github/python_learning/python_crash_course/C11
# collected 1 item                                                      

# test_survey.py .                                                [100%]

# ========================== 1 passed in 0.00s ==========================

def test_store_three_responses(language_survey):
    """Test that three individual responses are stored properly."""
    # question = "What language did you first learn to speak?"
    # language_survey =  AnonymousSurvey(question)
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_reponse(response)

    for response in responses:
        assert response in language_survey.responses