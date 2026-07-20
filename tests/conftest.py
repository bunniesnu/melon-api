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


@pytest.fixture
def sample_daily_response():
    return {
        "httpsDomain": "https://m2.melon.com",
        "response": {
            "CHARTINFO": {
                "LINKURL": "https://m2.melon.com/m5/chart/chartDayInfo.htm",
                "LINKTYPE": "ZA"
            },
            "STATUS": "0",
            "RECOMMENDLIST": [],
            "CHARTLIST": [
                {
                    "SONGID": "37928381",
                    "SONGNAME": "LOVE ATTACK",
                    "ALBUMID": "11575849",
                    "ALBUMNAME": "SCENEDROME",
                    "ARTISTLIST": [
                    {
                        "ARTISTID": "3709231",
                        "ARTISTNAME": "RESCENE (리센느)"
                    }
                    ],
                    "PLAYTIME": "182",
                    "GENRELIST": [
                    {
                        "GENRECODE": "GN0200",
                        "GENRENAME": "댄스"
                    }
                    ],
                    "CURRANK": "1",
                    "PASTRANK": "2",
                    "RANKGAP": "1",
                    "RANKTYPE": "UP",
                    "ISMV": True,
                    "ISADULT": False,
                    "ISFREE": False,
                    "ISHITSONG": False,
                    "ISHOLDBACK": False,
                    "ISTITLESONG": True,
                    "ISSERVICE": True,
                    "ISTRACKZERO": False,
                    "ALBUMIMG": "https://cdnimg.melon.co.kr/cm2/album/images/115/75/849/11575849_20240826152240_500.jpg?da43be78cb2cc67e9ee423c739bc09b6/melon/resize/144/optimize/90",
                    "ALBUMIMGPATH": "https://cdnimg.melon.co.kr/cm2/album/images/115/75/849/11575849_20240826152240_500.jpg?da43be78cb2cc67e9ee423c739bc09b6/melon/resize/144/optimize/90",
                    "ALBUMIMGLARGE": "https://cdnimg.melon.co.kr/cm2/album/images/115/75/849/11575849_20240826152240_500.jpg?da43be78cb2cc67e9ee423c739bc09b6/melon/optimize/90",
                    "ALBUMIMGSMALL": "https://cdnimg.melon.co.kr/cm2/album/images/115/75/849/11575849_20240826152240_500.jpg?da43be78cb2cc67e9ee423c739bc09b6/melon/resize/50/optimize/90",
                    "ISSUEDATE": "2024.08.27",
                    "CTYPE": "1",
                    "CONTSTYPECODE": "N10001"
                }
            ],
            "RANKDAY": None,
            "HASMORE": False,
            "SIZE": 100,
            "MENUID": "1000002322",
            "SECTION": "멜론차트",
            "PAGE": "멜론차트_TOP100일간",
            "TLOG": {
            "MENUID": "1000002322",
            "SECTION": "멜론차트",
            "PAGE": "멜론차트_TOP100일간"
            }
        },
        "httpDomain": "http://m2.melon.com"
    }


@pytest.fixture
def sample_weekly_response():
    return {
        "httpsDomain": "https://m2.melon.com",
        "response": {
            "MUSICAWARD": {
                "TITLE": "주간 인기상 투표",
                "AWARDMONTH": 7,
                "AWARDWEEK": 2,
                "AWARDYEAR": 2026,
                "AWARDDAYOFMONTH": 10,
                "SUBTITLE": "7월 3주차",
                "WEEKSTATUS": "P",
                "WEEKRANKLIST": [
                    {
                        "CURRANK": "1",
                        "SONGNAME": "Pretty Girl",
                        "ARTISTID": "3709231",
                        "ARTISTNAME": "RESCENE (리센느)",
                        "ARTISTIMG": "https://cdnimg.melon.co.kr/cm2/artistcrop/images/037/09/231/3709231_20260701101738_500.jpg/melon/resize/144/optimize/90",
                        "ARTISTIMGLARGE": "https://cdnimg.melon.co.kr/cm2/artistcrop/images/037/09/231/3709231_20260701101738_500.jpg/melon/resize/500/optimize/90",
                        "ARTISTIMGSMALL": "https://cdnimg.melon.co.kr/cm2/artistcrop/images/037/09/231/3709231_20260701101738_500.jpg/melon/resize/50/optimize/90",
                        "VOTEPER": "39",
                        "STARTMONTH": "7",
                        "STARTWEEK": "3"
                    },
                    {
                        "CURRANK": "2",
                        "SONGNAME": "Do your dance",
                        "ARTISTID": "3478478",
                        "ARTISTNAME": "RIIZE",
                        "ARTISTIMG": "https://cdnimg.melon.co.kr/cm2/artistcrop/images/034/78/478/3478478_20260612155006_500.jpg/melon/resize/144/optimize/90",
                        "ARTISTIMGLARGE": "https://cdnimg.melon.co.kr/cm2/artistcrop/images/034/78/478/3478478_20260612155006_500.jpg/melon/resize/500/optimize/90",
                        "ARTISTIMGSMALL": "https://cdnimg.melon.co.kr/cm2/artistcrop/images/034/78/478/3478478_20260612155006_500.jpg/melon/resize/50/optimize/90",
                        "VOTEPER": "26",
                        "STARTMONTH": "7",
                        "STARTWEEK": "3"
                    },
                    {
                        "CURRANK": "3",
                        "SONGNAME": "singasong",
                        "ARTISTID": "5004360",
                        "ARTISTNAME": "V8,디에잇,Vernon",
                        "ARTISTIMG": "https://cdnimg.melon.co.kr/cm2/artistcrop/images/050/04/360/5004360_20260615172151_500.jpg/melon/resize/144/optimize/90",
                        "ARTISTIMGLARGE": "https://cdnimg.melon.co.kr/cm2/artistcrop/images/050/04/360/5004360_20260615172151_500.jpg/melon/resize/500/optimize/90",
                        "ARTISTIMGSMALL": "https://cdnimg.melon.co.kr/cm2/artistcrop/images/050/04/360/5004360_20260615172151_500.jpg/melon/resize/50/optimize/90",
                        "VOTEPER": "14",
                        "STARTMONTH": "7",
                        "STARTWEEK": "3"
                    }
                ]
            },
            "STATUS": "0",
            "REVIEW": None,
            "RECOMMENDLIST": [],
            "CHARTLIST": [
                {
                    "SONGID": "602024048",
                    "SONGNAME": "갑자기",
                    "ALBUMID": "13399673",
                    "ALBUMNAME": "I.O.I 3rd MINI ALBUM [I.O.I : LOOP]",
                    "ARTISTLIST": [
                    {
                        "ARTISTID": "960251",
                        "ARTISTNAME": "아이오아이 (I.O.I)"
                    }
                    ],
                    "PLAYTIME": "195",
                    "GENRELIST": [
                    {
                        "GENRECODE": "GN0200",
                        "GENRENAME": "댄스"
                    },
                    {
                        "GENRECODE": "GN2500",
                        "GENRENAME": "아이돌"
                    }
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
                    "ALBUMIMG": "https://cdnimg.melon.co.kr/cm2/album/images/133/99/673/13399673_20260518151131_500.jpg?87de97fb7105b703fcaf0b07a9190ed0/melon/resize/144/optimize/90",
                    "ALBUMIMGPATH": "https://cdnimg.melon.co.kr/cm2/album/images/133/99/673/13399673_20260518151131_500.jpg?87de97fb7105b703fcaf0b07a9190ed0/melon/resize/144/optimize/90",
                    "ALBUMIMGLARGE": "https://cdnimg.melon.co.kr/cm2/album/images/133/99/673/13399673_20260518151131_500.jpg?87de97fb7105b703fcaf0b07a9190ed0/melon/optimize/90",
                    "ALBUMIMGSMALL": "https://cdnimg.melon.co.kr/cm2/album/images/133/99/673/13399673_20260518151131_500.jpg?87de97fb7105b703fcaf0b07a9190ed0/melon/resize/50/optimize/90",
                    "ISSUEDATE": "2026.05.19",
                    "CTYPE": "1",
                    "CONTSTYPECODE": "N10001"
                },
                {
                    "SONGID": "601807965",
                    "SONGNAME": "REDRED",
                    "ALBUMID": "13338387",
                    "ALBUMNAME": "GREENGREEN",
                    "ARTISTLIST": [
                    {
                        "ARTISTID": "4491260",
                        "ARTISTNAME": "CORTIS (코르티스)"
                    }
                    ],
                    "PLAYTIME": "164",
                    "GENRELIST": [
                    {
                        "GENRECODE": "GN0200",
                        "GENRENAME": "댄스"
                    },
                    {
                        "GENRECODE": "GN2500",
                        "GENRENAME": "아이돌"
                    }
                    ],
                    "CURRANK": "2",
                    "PASTRANK": "2",
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
                    "ALBUMIMG": "https://cdnimg.melon.co.kr/cm2/album/images/133/38/387/13338387_20260504133459_500.jpg?6c945aff0ea5b1384bd88ff103dd8d82/melon/resize/144/optimize/90",
                    "ALBUMIMGPATH": "https://cdnimg.melon.co.kr/cm2/album/images/133/38/387/13338387_20260504133459_500.jpg?6c945aff0ea5b1384bd88ff103dd8d82/melon/resize/144/optimize/90",
                    "ALBUMIMGLARGE": "https://cdnimg.melon.co.kr/cm2/album/images/133/38/387/13338387_20260504133459_500.jpg?6c945aff0ea5b1384bd88ff103dd8d82/melon/optimize/90",
                    "ALBUMIMGSMALL": "https://cdnimg.melon.co.kr/cm2/album/images/133/38/387/13338387_20260504133459_500.jpg?6c945aff0ea5b1384bd88ff103dd8d82/melon/resize/50/optimize/90",
                    "ISSUEDATE": "2026.04.20",
                    "CTYPE": "1",
                    "CONTSTYPECODE": "N10001"
                },
                {
                    "SONGID": "37928381",
                    "SONGNAME": "LOVE ATTACK",
                    "ALBUMID": "11575849",
                    "ALBUMNAME": "SCENEDROME",
                    "ARTISTLIST": [
                    {
                        "ARTISTID": "3709231",
                        "ARTISTNAME": "RESCENE (리센느)"
                    }
                    ],
                    "PLAYTIME": "182",
                    "GENRELIST": [
                    {
                        "GENRECODE": "GN0200",
                        "GENRENAME": "댄스"
                    }
                    ],
                    "CURRANK": "3",
                    "PASTRANK": "5",
                    "RANKGAP": "2",
                    "RANKTYPE": "UP",
                    "ISMV": True,
                    "ISADULT": False,
                    "ISFREE": False,
                    "ISHITSONG": False,
                    "ISHOLDBACK": False,
                    "ISTITLESONG": True,
                    "ISSERVICE": True,
                    "ISTRACKZERO": False,
                    "ALBUMIMG": "https://cdnimg.melon.co.kr/cm2/album/images/115/75/849/11575849_20240826152240_500.jpg?da43be78cb2cc67e9ee423c739bc09b6/melon/resize/144/optimize/90",
                    "ALBUMIMGPATH": "https://cdnimg.melon.co.kr/cm2/album/images/115/75/849/11575849_20240826152240_500.jpg?da43be78cb2cc67e9ee423c739bc09b6/melon/resize/144/optimize/90",
                    "ALBUMIMGLARGE": "https://cdnimg.melon.co.kr/cm2/album/images/115/75/849/11575849_20240826152240_500.jpg?da43be78cb2cc67e9ee423c739bc09b6/melon/optimize/90",
                    "ALBUMIMGSMALL": "https://cdnimg.melon.co.kr/cm2/album/images/115/75/849/11575849_20240826152240_500.jpg?da43be78cb2cc67e9ee423c739bc09b6/melon/resize/50/optimize/90",
                    "ISSUEDATE": "2024.08.27",
                    "CTYPE": "1",
                    "CONTSTYPECODE": "N10001"
                }
            ],
            "STARTDAY": "20260706",
            "ENDDAY": "20260712",
            "HASMORE": False,
            "SIZE": 100,
            "CHARTINFO": {
                "LINKURL": "https://m2.melon.com/m5/chart/chartWeekInfo.htm",
                "LINKTYPE": "ZA"
            },
            "MENUID": "1000002323",
            "SECTION": "멜론차트",
            "PAGE": "멜론차트_TOP100주간",
            "TLOG": {
                "MENUID": "1000002323",
                "SECTION": "멜론차트",
                "PAGE": "멜론차트_TOP100주간"
            }
        },
        "httpDomain": "http://m2.melon.com"
    }


@pytest.fixture
def sample_hot100_response():
    return {
        "httpsDomain": "https://m2.melon.com",
        "response": {
            "RANKDAY": "2026.07.14",
            "RANKHOUR": "14:00",
            "STATUS": "0",
            "SONGLIST": [
                {
                    "SONGID": "602024048",
                    "SONGNAME": "갑자기",
                    "ALBUMID": "13399673",
                    "ALBUMNAME": "I.O.I 3rd MINI ALBUM [I.O.I : LOOP]",
                    "ARTISTLIST": [
                    {
                        "ARTISTID": "960251",
                        "ARTISTNAME": "아이오아이 (I.O.I)"
                    }
                    ],
                    "PLAYTIME": "195",
                    "GENRELIST": [
                    {
                        "GENRECODE": "GN0200",
                        "GENRENAME": "댄스"
                    },
                    {
                        "GENRECODE": "GN2500",
                        "GENRENAME": "아이돌"
                    }
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
                    "ALBUMIMG": "https://cdnimg.melon.co.kr/cm2/album/images/133/99/673/13399673_20260518151131_500.jpg?87de97fb7105b703fcaf0b07a9190ed0/melon/resize/144/optimize/90",
                    "ALBUMIMGPATH": "https://cdnimg.melon.co.kr/cm2/album/images/133/99/673/13399673_20260518151131_500.jpg?87de97fb7105b703fcaf0b07a9190ed0/melon/resize/144/optimize/90",
                    "ALBUMIMGLARGE": "https://cdnimg.melon.co.kr/cm2/album/images/133/99/673/13399673_20260518151131_500.jpg?87de97fb7105b703fcaf0b07a9190ed0/melon/optimize/90",
                    "ALBUMIMGSMALL": "https://cdnimg.melon.co.kr/cm2/album/images/133/99/673/13399673_20260518151131_500.jpg?87de97fb7105b703fcaf0b07a9190ed0/melon/resize/50/optimize/90",
                    "ISSUEDATE": "2026.05.19",
                    "CTYPE": "1",
                    "CONTSTYPECODE": "N10001"
                }
            ],
            "CHARTINFO": {
                "LINKURL": "https://m2.melon.com/m6/chart/hot100ChartInfo.htm",
                "LINKTYPE": "ZA"
            },
            "MENUID": "1000003084",
            "SECTION": "멜론차트",
            "PAGE": "멜론차트_HOT100",
            "TLOG": {
                "MENUID": "1000003084",
                "SECTION": "멜론차트",
                "PAGE": "멜론차트_HOT100"
            }
        },
        "httpDomain": "http://m2.melon.com"
    }


@pytest.fixture
def sample_hot100_graph_hour_response():
    return {
        "httpsDomain": "https://m2.melon.com",
        "httpDomain": "http://m2.melon.com",
        "response": {
            "STATUS": "0",
            "RANKDAY": "2026.07.14",
            "RANKHOUR": "17:15",
            "STANDARD": "6.0",
            "XCATE": ["15시", "16시", "17시"],
            "ENTCHARTXCATE": ["15시", "16시", "17시"],
            "FIVECHARTFLAG": "Y",
            "ALLRANK": "N",
            "COMPRANK": "N",
            "GRAPHDATALIST": [
                {
                    "GRAPHRANK": 1,
                    "SONGID": "602450078",
                    "PEEKTIME": "14일 08시",
                    "FIRSTRANKSERIALCOUNT": "2",
                    "FIRSTRANKCOUNT": "0",
                    "GRAPHTOP7": 0,
                    "GRAPHTOPRANK": 1,
                    "GRAPHENTCHART": "6",
                    "GRAPHNEWRANK": "N",
                    "SHAREVALUE": "17",
                    "GRAPHDATA": [
                        {
                            "X": "0",
                            "VAL": "4.607",
                            "TOPCNTTIC": 0,
                            "TOPCNTYN": "N",
                            "IMMTOPTIC": False,
                            "FSTTOPTIC": False,
                            "NEWRANKTIC": False,
                        },
                        {
                            "X": "1",
                            "VAL": "4.515",
                            "TOPCNTTIC": 0,
                            "TOPCNTYN": "N",
                            "IMMTOPTIC": False,
                            "FSTTOPTIC": False,
                            "NEWRANKTIC": False,
                        },
                        {
                            "X": "2",
                            "VAL": "4.681",
                            "TOPCNTTIC": 0,
                            "TOPCNTYN": "N",
                            "IMMTOPTIC": False,
                            "FSTTOPTIC": False,
                            "NEWRANKTIC": False,
                        },
                    ],
                    "ENTGRAPHDATA": [
                        {"X": "0", "RANK": "6"},
                        {"X": "1", "RANK": "6"},
                        {"X": "2", "RANK": "6"},
                    ],
                    "GRAPHCHARTINFO": {
                        "SONGID": "602450078",
                        "SONGNAME": "Pretty Girl",
                        "ALBUMID": "13788545",
                        "ALBUMNAME": "Pretty Girl - Special Single",
                        "ARTISTLIST": [
                            {
                                "ARTISTID": "3709231",
                                "ARTISTNAME": "RESCENE (리센느)",
                            }
                        ],
                        "PLAYTIME": "210",
                        "GENRELIST": [
                            {
                                "GENRECODE": "GN0200",
                                "GENRENAME": "댄스",
                            }
                        ],
                        "CURRANK": "5",
                        "PASTRANK": "5",
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
                        "ALBUMIMG": "https://example.com/album.jpg",
                        "ALBUMIMGPATH": "https://example.com/album.jpg",
                        "ALBUMIMGLARGE": "https://example.com/album_large.jpg",
                        "ALBUMIMGSMALL": "https://example.com/album_small.jpg",
                        "ISSUEDATE": "2026.07.08",
                        "CTYPE": "1",
                        "CONTSTYPECODE": "N10001",
                    },
                }
            ],
            "CHARTINFO": {
                "LINKURL": "https://m2.melon.com/m6/chart/chartGraphInfo.htm",
                "LINKTYPE": "ZA",
            },
            "MENUID": "1000003037",
            "SECTION": "멜론차트",
            "PAGE": "멜론차트_HOT100그래프시간",
            "TLOG": {
                "MENUID": "1000003037",
                "SECTION": "멜론차트",
                "PAGE": "멜론차트_HOT100그래프시간",
            },
        },
    }

@pytest.fixture
def sample_artist_chart_response():
    return {
        "httpsDomain": "https://m2.melon.com",
        "response": {
            "STATUS": "0",
            "SEARCHTYPELIST": [
                {
                    "TYPECODE": "DP0000",
                    "TYPECODENAME": "전체"
                },
                {
                    "TYPECODE": "MG0000",
                    "TYPECODENAME": "남자그룹"
                },
                {
                    "TYPECODE": "FG0000",
                    "TYPECODENAME": "여자그룹"
                },
                {
                    "TYPECODE": "MS0000",
                    "TYPECODENAME": "남자솔로"
                },
                {
                    "TYPECODE": "FS0000",
                    "TYPECODENAME": "여자솔로"
                },
                {
                    "TYPECODE": "AB0000",
                    "TYPECODENAME": "해외"
                },
                {
                    "TYPECODE": "DP1800",
                    "TYPECODENAME": "인디"
                }
            ],
            "CHARTLIST": [
                {
                    "ARTISTID": "3709231",
                    "ARTISTNAME": "RESCENE (리센느)",
                    "ACTTYPENAME": "그룹",
                    "DEBUTDAY": None,
                    "BIRTHDAY": None,
                    "ARTISTIMG": "https://cdnimg.melon.co.kr/cm2/artistcrop/images/037/09/231/3709231_20260701101738.jpg?78297ceffb4a156b74f31cc249aa2b51/melon/optimize/90",
                    "CURRANK": "1",
                    "PASTRANK": "1",
                    "RANKGAP": "0",
                    "RANKTYPE": "NONE",
                    "AREATYPE": "FG0000",
                    "TOTFANCNT": 31226,
                    "INCREMFANCNT": 541,
                    "INCREMTYPE": "UP",
                    "SONGIDX": "10",
                    "MVIDX": "10",
                    "PHOTOIDX": "10",
                    "FANIDX": "10",
                    "LIKEIDX": "10",
                    "TOCIDX": "10",
                    "CHNLSEQ": "0",
                    "TOPRANK": "1",
                    "PASTWEEKRANK": "1",
                    "IMAGETYPE": "S",
                    "CONTSTYPECODE": "N10006"
                }
            ],
            "RANKDAY": "2026.07.18",
            "HASMORE": False,
            "SIZE": 1,
            "CHARTINFO": {
                "OPENLINK": "https://m2.melon.com/chart/chartInfo.htm",
                "OPENTYPE": "ZA"
            },
            "MENUID": "1000000034",
            "SECTION": "멜론차트",
            "PAGE": "멜론차트_아티스트",
            "TLOG": {
                "MENUID": "1000000034",
                "SECTION": "멜론차트",
                "PAGE": "멜론차트_아티스트"
            }
        },
        "httpDomain": "http://m2.melon.com"
    }

@pytest.fixture
def sample_album_info():
    return {
        "httpsDomain": "https://m2.melon.com",
        "response": {
            "RESULTCODE": "0",
            "RESPONSE": "albumInfo",
            "CPLANCODE": "0",
            "MENUID": "1000000461",
            "ALBUMINFO": {
                "ISSERVICE": True,
                "ALBUMID": "13788545",
                "ALBUMNAME": "Pretty Girl - Special Single",
                "ISSUEDATE": "2026.07.08",
                "ISTRACKZERO": False,
                "ALBUMIMG": "https://cdnimg.melon.co.kr/cm2/album/images/137/88/545/13788545_20260707111659_500.jpg?3ef0f9e6af1ea09e3f919c7cb69065ed",
                "ALBUMIMGLARGE": "https://cdnimg.melon.co.kr/cm2/album/images/137/88/545/13788545_20260707111659_1000.jpg?3ef0f9e6af1ea09e3f919c7cb69065ed",
                "SONGCNT": "1",
                "CTYPE": "2",
                "CONTSTYPECODE": "N10002",
                "ARTISTLIST": [
                    {
                        "ARTISTID": "3709231",
                        "ARTISTNAME": "RESCENE (리센느)",
                        "ACTTYPENAME": None,
                        "DEBUTDAY": None,
                        "BIRTHDAY": None,
                        "ARTISTIMG": "https://cdnimg.melon.co.kr/cm2/artistcrop/images/037/09/231/3709231_20260701101738_500.jpg?78297ceffb4a156b74f31cc249aa2b51/melon/resize/220/optimize/90",
                        "IMAGETYPE": "S",
                        "CONTSTYPECODE": "N10006"
                    }
                ]
            },
            "TOTAVRGSCOREINFO": {
                "TITLE": "평점 부여 권한",
                "TEXT": "클린한 평점 환경을 위해\r\n24시간 이내에\r\n다운로드 받은 파일 재생,\r\n스트리밍으로 감상한 경우에만\r\n평점 부여가 가능합니다.\r\n참고하여 서비스 이용 바랍니다.\r\n\r\n* 접속자가 많은 경우\r\n평점주기가 지연 될 수 있습니다.",
                "TOTAVRGSCORE": "4.9",
                "PTCPNMPRCO": "1946"
            },
            "LIKECNT": "13207",
            "ISDOLBYATMOS": True,
            "ISMASTERPIECE": False,
            "BOOKLETIMGLIST": None,
            "ALBUMPRICE": "",
            "ALBUMPRICEFLAC16": "",
            "ALBUMPRICEFLAC24": "",
            "ALBUMFLACINFO": "FLAC",
            "ALBUMMESSAGE": "",
            "BBSCHANNELSEQ": "102",
            "BBSCONTSREFVALUE": "13788545",
            "POSTIMG": "https://cdnimg.melon.co.kr/cm2/album/images/137/88/545/13788545_20260707111659_500.jpg/melon/optimize/90",
            "POSTEDITIMG": "https://cdnimg.melon.co.kr/cm2/album/images/137/88/545/13788545_20260707111659_500.jpg/melon/resize/144/optimize/90",
            "TITLESONGINFO": {
                "SONGID": "602450078",
                "SONGNAME":"Pretty Girl"
            },
            "ARTISTNOTEINFO": {
                "ALBUMID": "13788545",
                "ARTISTID": "3709887",
                "ARTISTNOTE": "안녕~ 리마인 원이입니다! 이번 앨범은 프리티 원이로 돌아왔어요. 이 곡을 듣는 모든 분들의 발걸음이 어디서든 당당해졌으면 좋겠습니다! 첫 리메이크 곡인 만큼 많이 사랑해주세요! 리마인 사랑해\U0001F497\U0001F61D","ARTISTNAME":"원이 (WONI)",
                "ARTISTIMG": "https://cdnimg.melon.co.kr/cm2/artistcrop/images/037/09/887/3709887_20260701101801.jpg?b18a48740a42a972a398c8d6e8584217",
                "ISSUEDATE": "2026.07.08"
            },
            "ARTISTNOTEALLBUTTONFLAG": True,
            "GENRELIST": [
                {
                    "GENRECODE": "GN0200",
                    "GENRENAME": "댄스"
                }
            ],
            "ISSUEDATE": "2026.07.08",
            "REPORT": "RESCENE [Pretty Girl - Special Single] \n \n5세대 대세 걸그룹 '리센느(RESCENE)' \n자몽향을 가득 담아 리센느만의 청량함으로 재해석한 2세대 레전드 명곡, ‘Pretty Girl’ \n \n2세대 대표 아이돌 카라(KARA)의 메가 히트곡 ‘Pretty Girl’이 독보적인 콘셉트로 매 앨범마다 특별한 향기를 선사하는 걸그룹 리센느(RESCENE)의 목소리를 통해 재탄생했다. \n \n원곡 특유의 깜찍 발랄함과 당당한 매력으로 큰 사랑을 받았던 대표적인 틴팝(Teen Pop) 장르의 느낌을 유지하면서도, 입안 가득 톡 터지는 '자몽향'처럼 상큼하고 청량감 넘치는 편곡으로 선명하고 싱그러운 이미지를 더했다. \n \n이번 리메이크는 원곡의 중독성 있는 멜로디 라인을 살리면서도 트랙 전반의 사운드 아키텍처를 다듬어 음악적 완성도를 높였다. 기존의 기타 사운드에 강렬한 디스토션(Distortion) 사운드를 가미하여 곡의 전체적인 윤곽을 한층 더 선명하게 잡아주었으며, 여기에 리센느만의 세련된 감성을 느낄 수 있도록 감각적인 신스(Synth) 소스들을 추가해 세련된 공간감을 연출했다. 특히 묵직한 타격감이 돋보이는 드럼의 활용으로 트랙의 무게중심을 아래로 낮추어, 리센느만의 깊이 있고 탄탄한 베이스 라인을 강조하는 스타일을 완성해 냈다. \n \n이렇듯 견고해진 트랙의 무게감 위로 원곡의 탑라인에 리센느의 맑고 부드러운 보컬을 더해, 전반적인 에너지가 한층 더 입체적으로 업그레이드되었다. 청각을 넘어 시각과 후각까지 자극하는 리센느만의 선명하고 청량한 '자몽향' 가득한 ‘Pretty Girl’은 올여름 대중들의 귀를 완벽하게 사로잡을 것이다. \n \nTRACKLIST CREDIT \n01. Pretty Girl \nLyrics by 송수윤, 한재호, 김승수 \nComposed by 한재호, 김승수 \nArranged by 한재호, 김승수, 이주헌 (The Muze), 더풀킴 (The Muze), 황세영 \n \nVocal Directed by 이주헌, 더풀킴, 김보아 \nBackground Vocals by 김보아, 미나미 \n \nRecorded by 장우영 @DOOBDOOB STUDIO \nMixed by Simon Bergseth @Stadion Studio \nMastered by 권남우 @821 SOUND \n","ALBUMTYPE":"싱글","SELLCNPY":"지니뮤직, STONE MUSIC","PLANCNPY":"더뮤즈엔터테인먼트",
            "CREDITLIST": None,
            "REPORTPREVIEW": "RESCENE [Pretty Girl - Special Single]  5세대 대세 걸그룹 '리센느(RESCENE)' 자몽향을 가득 담아 리센느만의 청량함으로 재해석한 2세대 레전드 명곡, ‘Pretty Girl’  2세대 대표 아이돌 카라(KARA)의 메가 히트곡 ‘Pretty Girl’이 독보적인 콘셉트로 매 앨범마다 특별한 향기를 선사하는 걸그룹 리센느(RESCENE)의 목소리를 통해 재탄생했다.  원곡 특유의 깜찍 발랄함과 당당한 매력으로 큰 사랑을 받았던 대표적인 틴팝(Teen Pop) 장르의 느낌을 유지하면서도, 입안 가득 톡 터지는 '자몽향'처럼 상큼하고 청량감 넘치는 편곡으로 선명하고 싱그러운 이미지를 더했다.  이번 리메이크는 원곡의 중독성 있는 멜로디 라인을 살리면서도 트랙 전반의 사운드 아키텍처를 다듬어 음악적 완성도를 높였다. 기존의 기타 사운드에 강렬한 디스토션(Distortion) 사운드를 가미하여 곡의 전체적인 윤곽을 한층 더 선명하게 잡아주었으며, 여기에 리센느만의 세련된 감성을 느낄 수 있도록 감각적인 신스(Synth) 소스들을 추가해 세련된 공간감을 연출했다. 특히 묵직한 타격감이 돋보이는 드럼의 활용으로 트랙의 무게중심을 아래로 낮추어, 리센느만의 깊이 있고 탄탄한 베이스 라인을 강조하는 스타일을 완성해 냈다.  이렇듯 견고해진 트랙의 무게감 위로 원곡의 탑라인에 리센느의 맑고 부드러운 보컬을 더해, 전반적인 에너지가 한층 더 입체적으로 업그레이드되었다. 청각을 넘어 시각과 후각까지 자극하는 리센느만의 선명하고 청량한 '자몽향' 가득한 ‘Pretty Girl’은 올여름 대중들의 귀를 완벽하게 사로잡을 것이다.  TRACKLIST CREDIT 01. Pretty Girl Lyrics by 송수윤, 한재호, 김승수 Composed by 한재호, 김승수 Arranged by 한재호, 김승수, 이주헌 (The Muze), 더풀킴 (The Muze), 황세영  Vocal Directed by 이주헌, 더풀킴, 김보아 Background Vocals by 김보아, 미나미  Recorded by 장우영 @DOOBDOOB STUDIO Mixed by Simon Bergseth @Stadion Studio Mastered by 권남우 @821 SOUND",
            "SPOTLIGHTBUTTONFLAG": "N",
            "HIRISINGBUTTONFLAG": "N",
            "MILLIONSINFO": {
                "HISTDATA": 580502,
                "ISSUEDATE": "202607081800",
                "HISTINFO": "ST",
                "ISNOW": "N",
                "ISCOUNTING": "N",
                "REACHINGINFO": "",
                "ACCUMDATA":"580502",
                "LINK": {
                    "LINKTYPE":"ZA",
                    "LINKURL":""
                }
            },
            "DUMMYTEXT": "22#_h8Si9Rj0Qk!Pl@OmN#nM$oL%pK^qJ&r*IsH(tG)uF-v:Ew;Dx=Cy{Bz}A<>a1Zb2Yc_l@OmN#nM$oL%pK^qJ&r*IsH(tG)uF-v:Ew;Dx=Cy{Bz}A<>a",
            "SECTION": "앨범상세",
            "PAGE": "앨범상세_앨범홈",
            "TLOG": {
                "MENUID": "1000000461",
                "SECTION": "앨범상세",
                "PAGE": "앨범상세_앨범홈",
                "CONTSTYPECODE": "N10002",
                "CONTSTYPENAME": "앨범",
                "CONTSID": "13788545",
                "CONTSNAME": "Pretty Girl - Special Single"
            }
        },
        "httpDomain":"http://m2.melon.com"
    }