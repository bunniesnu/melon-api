import httpx

BASE_URL = "https://m.app.melon.com"
HOURLY_CHART_ENDPOINT = "/chart/hourly/hourlyChartList.json"


class MelonClient:
    def __init__(self, timeout: float = 10.0):
        self.client = httpx.Client(base_url=BASE_URL, timeout=timeout)

    def get_hourly_chart(
        self,
        cp_id: str = "AS40",
        cp_key: str = "14LNM3",
        version: str = "4.0",
        resolution: int = 2,
        app_ver: str = "4.1.0.1",
        os_version: str = "11",
        is_recom: str = "N",
        page_size: int = 100,
    ) -> dict:
        params = {
            "cpId": cp_id,
            "cpKey": cp_key,
            "v": version,
            "resolution": resolution,
            "appVer": app_ver,
            "osVersion": os_version,
            "isRecom": is_recom,
            "pageSize": page_size,
        }
        response = self.client.get(HOURLY_CHART_ENDPOINT, params=params)
        response.raise_for_status()
        return response.json()

    def close(self):
        self.client.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()
