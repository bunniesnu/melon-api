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
                    "ALBUMID": "11575849",
                    "ALBUMNAME": "SCENEDROME",
                    "ARTISTLIST": [{"ARTISTID": "3709231", "ARTISTNAME": "RESCENE (리센느)"}],
                    "PLAYTIME": "182",
                    "GENRELIST": [
                        {"GENRECODE": "GC0011", "GENRENAME": "Dance"},
                        {"GENRECODE": "GC0167", "GENRENAME": "댄스 20'"},
                    ],
                    "CURRANK": "1",
                    "PASTRANK": "1",
                    "RANKGAP": "0",
                    "RANKTYPE": "NONE",
                    "ISMV": True,
                    "ISADULT": False,
                    "ISFREE": False,
                    "ISHITSONG": False,
                    "ISHOLDBACK": False,
                    "ISTITLESONG": True,
                    "ISSERVICE": True,
                    "ISTRACKZERO": False,
                    "ALBUMIMG": "https://cdnimg.melon.co.kr/example.jpg",
                    "ALBUMIMGPATH": "https://cdnimg.melon.co.kr/example.jpg",
                    "ALBUMIMGLARGE": "https://cdnimg.melon.co.kr/example.jpg",
                    "ALBUMIMGSMALL": "https://cdnimg.melon.co.kr/example.jpg",
                    "ISSUEDATE": "2024.08.27",
                    "CTYPE": "1",
                    "CONTSTYPECODE": "N10001",
                },
            ],
            "RANKDAY": "2026.07.14",
            "RANKHOUR": "12:00",
            "HASMORE": True,
            "SIZE": 1,
            "MENUID": "1000000026",
            "SECTION": "멜론차트",
            "PAGE": "멜론차트_실시간",
            "TLOG": {
                "MENUID": "1000000026",
                "SECTION": "멜론차트",
                "PAGE": "멜론차트_실시간",
            },
        },
    }


@pytest.fixture
def sample_report_response():
    return {
        "httpsDomain": "https://m2.melon.com",
        "response": {
            "RESULTCODE": "0",
            "RESPONSE": "chartReport",
            "CPLANCODE": "0",
            "RECENTTIME": "12:50",
            "SONGINFO": {
                "SONGID": "37928381",
                "SONGNAME": "LOVE ATTACK",
                "ALBUMID": "11575849",
                "ALBUMNAME": "SCENEDROME",
                "ARTISTLIST": [
                    {
                        "ARTISTID": "3709231",
                        "ARTISTNAME": "RESCENE (리센느)",
                        "ACTTYPENAME": None,
                        "DEBUTDAY": None,
                        "BIRTHDAY": None,
                        "ARTISTIMG": "https://cdnimg.melon.co.kr/example.jpg",
                        "IMAGETYPE": "S",
                        "CONTSTYPECODE": "N10006",
                    }
                ],
                "ISSUEDATE": "2024.08.27",
                "ALBUMIMG": "https://cdnimg.melon.co.kr/example.jpg",
                "ALBUMIMGLARGE": "https://cdnimg.melon.co.kr/example.jpg",
                "ALBUMIMGSMALL": "https://cdnimg.melon.co.kr/example.jpg",
                "CURRANK": "1",
                "PASTRANK": "1",
                "RANKGAP": "0",
                "RANKTYPE": "NONE",
            },
            "LISTENERCHART": {
                "XLABELS": [],
                "YMINIMUM": 0,
                "YMAXIMUM": 0,
                "DATA": [],
                "TITLE": {
                    "VALUEPLACEHOLDER": "##VALUE##",
                    "TEXT": "이 곡은 지금\n##VALUE##명이 듣고 있어요.",
                    "VALUE": "3,859",
                },
                "INFO": {
                    "TITLE": "최근 감상자수",
                    "DESC": "현재 TOP100에 오른 곡들의 실시간 감상자수를 확인해보세요.",
                    "INFOLIST": [
                        {"TITLE": "현재 감상자수", "TEXT": "10분마다 업데이트"},
                        {"TITLE": "1시간·24시간 감상자수", "TEXT": "매시 정각 업데이트"},
                    ],
                    "FOOT": "※ 이용량이 적은 01시~07시의 1시간과 24시간 감상자수는 제공되지 않습니다.",
                },
            },
            "LISTENERDATA": {"ONEHOUR": "-", "ONEDAY": "-"},
            "RANKCHART": {
                "XLABELS": [
                    {"XLABEL": "06시", "HIGHLIGHTING": False},
                    {"XLABEL": "현재", "HIGHLIGHTING": True},
                    {"XLABEL": "예측", "HIGHLIGHTING": True},
                ],
                "YMINIMUM": 1,
                "YMAXIMUM": 61,
                "DATA": [
                    {"XINDEX": 0, "VALUE": 1, "LABEL": "1", "HIGHLIGHTING": False},
                    {"XINDEX": 6, "VALUE": 1, "LABEL": "1", "HIGHLIGHTING": True},
                ],
                "PREDICTEDDATA": [
                    {"XINDEX": 6, "VALUE": 1, "LABEL": "1", "HIGHLIGHTING": True},
                    {"XINDEX": 7, "VALUE": 1, "LABEL": "1", "HIGHLIGHTING": True},
                ],
                "TITLE": {
                    "VALUEPLACEHOLDER": "##VALUE##",
                    "TEXT": "다음 예측은 ##VALUE##입니다.",
                    "VALUE": "1위",
                },
                "INFO": {
                    "TITLE": "차트 순위 변화",
                    "DESC": "현재 TOP100에 오른 곡들의 최근 순위 변화와 다음 순위 예측을 확인해보세요.",
                    "INFOLIST": [
                        {"TITLE": "최근 순위 변화", "TEXT": "매시 정각 업데이트"},
                        {"TITLE": "다음 순위 예측", "TEXT": "매시 30분부터 10분마다 업데이트"},
                    ],
                },
            },
            "YESTERCHARTINFO": {
                "TITLE": {
                    "VALUEPLACEHOLDER": "##VALUE##",
                    "TEXT": "이 곡의 어제 차트 순위는\n##VALUE##입니다.",
                    "VALUE": "2위",
                },
                "FIRSTINFOLABEL": "최고 순위",
                "FIRSTINFOVALUE": "2위",
                "SECONDINFOLABEL": "최고 순위 기록일",
                "SECONDINFOVALUE": "2026.07.09",
                "RECORDLIST": [],
                "INFO": {
                    "TITLE": "이 곡의 데일리 기록",
                    "DESC": "현재 TOP100에 오른 곡들의 일간 차트 기록을 확인해보세요.",
                    "INFOLIST": [
                        {"TITLE": "데이터 생성 기준", "TEXT": "오늘 낮 12시까지의 데이터"},
                        {"TITLE": "업데이트 시간", "TEXT": "매일 오후 5시"},
                        {"TITLE": "일간 차트 연속 진입일", "TEXT": "14.01.01 이후 기록"},
                    ],
                },
            },
            "FOOTBUTTON": {"NEXTBUTTON": {"SONGID": "602024048", "LABEL": "다음 곡"}},
            "MENUID": "1000002722",
            "SECTION": "멜론차트",
            "PAGE": "멜론차트_TOP100차트리포트",
            "TLOG": {
                "MENUID": "1000002722",
                "SECTION": "멜론차트",
                "PAGE": "멜론차트_TOP100차트리포트",
                "CONTSTYPECODE": "N10001",
                "CONTSTYPENAME": "곡",
                "CONTSID": "37928381",
                "CONTSNAME": "",
            },
        },
    }


@pytest.fixture
def sample_top100_response():
    return {
        "httpsDomain": "https://m2.melon.com",
        "response": {
            "RANKDAY": "2026.07.14",
            "RANKHOUR": "13:00",
            "STATUS": "0",
            "SONGLIST": [
                {
                    "SONGID": "37928381",
                    "SONGNAME": "LOVE ATTACK",
                    "ALBUMID": "11575849",
                    "ALBUMNAME": "SCENEDROME",
                    "ARTISTLIST": [{"ARTISTID": "3709231", "ARTISTNAME": "RESCENE (리센느)"}],
                    "PLAYTIME": "182",
                    "GENRELIST": [{"GENRECODE": "GN0200", "GENRENAME": "댄스"}],
                    "CURRANK": "1",
                    "PASTRANK": "1",
                    "RANKGAP": "0",
                    "RANKTYPE": "NONE",
                    "ISMV": True,
                    "ISADULT": False,
                    "ISFREE": False,
                    "ISHITSONG": False,
                    "ISHOLDBACK": False,
                    "ISTITLESONG": True,
                    "ISSERVICE": True,
                    "ISTRACKZERO": False,
                    "ALBUMIMG": "https://cdnimg.melon.co.kr/example.jpg",
                    "ALBUMIMGPATH": "https://cdnimg.melon.co.kr/example.jpg",
                    "ALBUMIMGLARGE": "https://cdnimg.melon.co.kr/example.jpg",
                    "ALBUMIMGSMALL": "https://cdnimg.melon.co.kr/example.jpg",
                    "ISSUEDATE": "2024.08.27",
                    "CTYPE": "1",
                    "CONTSTYPECODE": "N10001",
                },
            ],
            "CHARTINFO": {
                "LINKURL": "https://m2.melon.com/m6/chart/chartEntInfo.htm?cpId=IS40&appVer=6.22.1",
                "LINKTYPE": "ZA",
            },
            "STATSELEMENTS": {"IMPRESSIONID": "", "RANGECODE": "1000002737"},
            "MENUID": "1000002721",
            "SECTION": "멜론차트",
            "PAGE": "멜론차트_TOP100NOW",
            "TLOG": {
                "MENUID": "1000002721",
                "SECTION": "멜론차트",
                "PAGE": "멜론차트_TOP100NOW",
            },
        },
    }
