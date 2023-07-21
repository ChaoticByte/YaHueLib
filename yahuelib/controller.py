# Copyright (c) 2023 Julian Müller (ChaoticByte)


from json import dumps as _json_dumps
from json import loads as _json_loads
from urllib import request as _request


from .exceptions import *


# Have to use the following SSL context because the
# TLS certificate of a Hue Bridge is self signed
ssl_context_unverified = _request.ssl._create_unverified_context()


class _BaseController:

    _api_endpoint_all = ""
    _api_endpoint_specific = ""

    def __init__(self, number:int, bridge_ip_address:str, bridge_api_user:str):
        assert type(number) == int
        assert type(bridge_ip_address) == str
        assert type(bridge_api_user) == str
        self.number = number
        self.bridge_ip_address = bridge_ip_address
        self.bridge_api_user = bridge_api_user
    
    @classmethod
    def from_name(cls, name:str, bridge_ip_address:str, bridge_api_user:str):
        assert type(bridge_ip_address) == str
        assert type(bridge_api_user) == str
        assert type(name) == str
        api_request = _request.Request(cls._api_endpoint_all.format(
            bridge_ip_address=bridge_ip_address,
            bridge_api_user=bridge_api_user))
        with _request.urlopen(api_request, context=ssl_context_unverified) as r:
            data = _json_loads(r.read())
        for n in data:
            if data[n]["name"] == name:
                return cls(int(n), bridge_ip_address, bridge_api_user)
        raise LightOrGroupNotFound()

    def _api_request(self, method="GET", path:str="", data:dict={}):
        assert type(method) == str
        assert type(path) == str
        assert type(data) == dict
        api_request = _request.Request(
            self._api_endpoint_specific.format(
                bridge_ip_address=self.bridge_ip_address,
                bridge_api_user=self.bridge_api_user,
                number=self.number
            ) + path,
            method=method,
            data=_json_dumps(data).encode())
        with _request.urlopen(api_request, context=ssl_context_unverified) as r:
            response_data = _json_loads(r.read())
            if type(response_data) == list and len(response_data) > 0:
                if "error" in response_data[0]:
                    raise APIError(response_data)
            return response_data


class LightController(_BaseController):

    _api_endpoint_all = "https://{bridge_ip_address}/api/{bridge_api_user}/lights"
    _api_endpoint_specific = "https://{bridge_ip_address}/api/{bridge_api_user}/lights/{number}"

    @property
    def reachable(self) -> bool:
        data = self._api_request()
        return data["state"]["reachable"]

    @property
    def on(self) -> bool:
        data = self._api_request()
        return data["state"]["on"]

    @on.setter
    def on(self, on:bool):
        assert type(on) == bool
        self._api_request("PUT", "/state", {"on": on})
    
    @property
    def brightness(self):
        data = self._api_request()
        return data["state"]["bri"]
    
    @brightness.setter
    def brightness(self, brightness:float):
        assert type(brightness) == float or type(brightness) == int
        bri_ = min(max(int(brightness * 254), 0), 254)
        self._api_request("PUT", "/state", {"bri": bri_})
    
    @property
    def hue(self):
        data = self._api_request()
        return data["state"]["hue"]
    
    @hue.setter
    def hue(self, hue:float):
        assert type(hue) == float or type(hue) == int
        hue_ = min(max(int(hue * 65535), 0), 65535)
        self._api_request("PUT", "/state", {"hue": hue_})

    @property
    def saturation(self):
        data = self._api_request()
        return data["state"]["sat"]
    
    @saturation.setter
    def saturation(self, saturation:float):
        assert type(saturation) == float or type(saturation) == int
        sat_ = min(max(int(saturation * 254), 0), 254)
        self._api_request("PUT", "/state", {"sat": sat_})
    
    def alert(self):
        self._api_request("PUT", "/state", {"alert": "select"})

    def alert_long(self):
        self._api_request("PUT", "/state", {"alert": "lselect"})


class GroupController(_BaseController):

    _api_endpoint_all = "https://{bridge_ip_address}/api/{bridge_api_user}/groups"
    _api_endpoint_specific = "https://{bridge_ip_address}/api/{bridge_api_user}/groups/{number}"

    @property
    def any_on(self) -> bool:
        data = self._api_request()
        return data["state"]["any_on"]

    @property
    def all_on(self) -> bool:
        data = self._api_request()
        return data["state"]["all_on"]

    @all_on.setter
    def all_on(self, on:bool):
        assert type(on) == bool
        self._api_request("PUT", "/action", {"on": on})

    @property
    def brightness(self):
        data = self._api_request()
        return data["action"]["bri"]
    
    @brightness.setter
    def brightness(self, brightness:float):
        assert type(brightness) == float or type(brightness) == int
        bri_ = min(max(int(brightness * 254), 0), 254)
        self._api_request("PUT", "/action", {"bri": bri_})

    @property
    def hue(self):
        data = self._api_request()
        return data["action"]["hue"]
    
    @hue.setter
    def hue(self, hue:float):
        assert type(hue) == float or type(hue) == int
        hue_ = min(max(int(hue * 65535), 0), 65535)
        self._api_request("PUT", "/action", {"hue": hue_})

    @property
    def saturation(self):
        data = self._api_request()
        return data["action"]["sat"]
    
    @saturation.setter
    def saturation(self, saturation:float):
        assert type(saturation) == float or type(saturation) == int
        sat_ = min(max(int(saturation * 254), 0), 254)
        self._api_request("PUT", "/action", {"sat": sat_})
    
    def alert(self):
        self._api_request("PUT", "/action", {"alert": "select"})

    def alert_long(self):
        self._api_request("PUT", "/action", {"alert": "lselect"})
