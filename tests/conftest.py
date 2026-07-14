import pytest
from melon.chart import MelonClient

@pytest.fixture
def melon_client():
    with MelonClient() as client:
        yield client

@pytest.fixture
def sample_chart_response():
    return {
        "httpsDomain": "https://m2.melon.com",
        "response": {
            "STATUS": "0",
            "RECOMMENDLIST": [],
            "CHARTLIST": [
                {
                    "SONGID": "37928381",
                    "SONGNAME": "LOVE ATTACK",
                    "ALBUMNAME": "SCENEDROME",
                    "ARTISTLIST": [{"ARTISTID": "3709231", "ARTISTNAME": "RESCENE (리센느)"}],
                    "CURRANK": "1",
                    "PASTRANK": "1",
                    "RANKGAP": "0",
                    "RANKTYPE": "NONE",
                },
            ],
        },
    }

@pytest.fixture
def sample_report_response():
    return {
        "httpsDomain": "https://m2.melon.com",
        "response": {
            "RESULTCODE": "0",
            "RESPONSE": "chartReport",
            "SONGINFO": {
                "SONGID": "37928381",
                "SONGNAME": "LOVE ATTACK",
                "ALBUMNAME": "SCENEDROME",
                "CURRANK": "1",
                "PASTRANK": "1",
                "RANKGAP": "0",
                "RANKTYPE": "NONE",
            },
            "LISTENERDATA": {"ONEHOUR": "-", "ONEDAY": "-"},
        },
    }
