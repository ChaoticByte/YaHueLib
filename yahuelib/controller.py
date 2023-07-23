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
    '''Control a Philips Hue Light using the API of your Hue Bridge.

    Args:
    - `number: int` - The number of your light
    - `bridge_ip_address: str` - The IP address of your Hue Bridge
    - `bridge_api_user: str` - The user used to authenticate to the API

    Use the class method `.from_name(name:str, ...)` to use the name of a light instead of the number.
    '''

    _api_endpoint_all = "https://{bridge_ip_address}/api/{bridge_api_user}/lights"
    _api_endpoint_specific = "https://{bridge_ip_address}/api/{bridge_api_user}/lights/{number}"

    @property
    def reachable(self) -> bool:
        '''Check if the light is reachable using `LightController.reachable`'''
        data = self._api_request()
        return data["state"]["reachable"]

    @property
    def on(self) -> bool:
        '''Check if the light is on using `LightController.on`'''
        data = self._api_request()
        return data["state"]["on"]

    @on.setter
    def on(self, on:bool):
        '''Turn the light on/off using `LightController.on = ...`'''
        assert type(on) == bool
        self._api_request("PUT", "/state", {"on": on})

    @property
    def brightness(self) -> int:
        '''Get the brightness using `LightController.brightness`'''
        data = self._api_request()
        return data["state"]["bri"]

    @brightness.setter
    def brightness(self, brightness:float):
        '''Set the brightness using `LightController.brightness = ...`'''
        assert type(brightness) == float or type(brightness) == int
        bri_ = min(max(int(brightness * 254), 0), 254)
        self._api_request("PUT", "/state", {"bri": bri_})

    @property
    def hue(self) -> int:
        '''Get the hue using `LightController.hue`'''
        data = self._api_request()
        return data["state"]["hue"]

    @hue.setter
    def hue(self, hue:float):
        '''Set the hue using `LightController.hue = ...`'''
        assert type(hue) == float or type(hue) == int
        hue_ = min(max(int(hue * 65535), 0), 65535)
        self._api_request("PUT", "/state", {"hue": hue_})

    @property
    def saturation(self) -> int:
        '''Get the saturation using `LightController.saturation`'''
        data = self._api_request()
        return data["state"]["sat"]

    @saturation.setter
    def saturation(self, saturation:float):
        '''Set the saturation using `LightController.saturation = ...`'''
        assert type(saturation) == float or type(saturation) == int
        sat_ = min(max(int(saturation * 254), 0), 254)
        self._api_request("PUT", "/state", {"sat": sat_})

    @property
    def color_temperature(self):
        '''Get the white color temperature in Mired using `LightController.color_temperature`'''
        data = self._api_request()
        return data["state"]["ct"]

    @color_temperature.setter
    def color_temperature(self, mired:int):
        '''Set the white color temperature in Mired (`154` - `500`) using `LightController.color_temperature = ...`'''
        assert type(mired) == int
        ct_ = min(max(mired, 154), 500)
        self._api_request("PUT", "/state", {"ct": ct_})

    def alert(self):
        '''Flash the light once.'''
        self._api_request("PUT", "/state", {"alert": "select"})

    def alert_long(self):
        '''Flash the light for 10 seconds.'''
        self._api_request("PUT", "/state", {"alert": "lselect"})


class GroupController(_BaseController):
    '''Control a Philips Hue Light Group (Room/Zone) using the API of your Hue Bridge.

    Args:
    - `number: int` - The number of your light group
    - `bridge_ip_address: str` - The IP address of your Hue Bridge
    - `bridge_api_user: str` - The user used to authenticate to the API

    Use the class method `.from_name(name:str, ...)` to use the name of a group instead of the number.
    '''

    _api_endpoint_all = "https://{bridge_ip_address}/api/{bridge_api_user}/groups"
    _api_endpoint_specific = "https://{bridge_ip_address}/api/{bridge_api_user}/groups/{number}"

    @property
    def any_on(self) -> bool:
        '''Check if any light in this group is on using `GroupController.any_on`'''
        data = self._api_request()
        return data["state"]["any_on"]

    @property
    def all_on(self) -> bool:
        '''Check if all lights in this group are on using `GroupController.all_on`'''
        data = self._api_request()
        return data["state"]["all_on"]

    @all_on.setter
    def all_on(self, on:bool):
        '''Turn on/off all lights in this group using `GroupController.all_on = ...`'''
        assert type(on) == bool
        self._api_request("PUT", "/action", {"on": on})

    @property
    def brightness(self) -> int:
        '''Get the last set brightness in this group using `GroupController.brightness`'''
        data = self._api_request()
        return data["action"]["bri"]

    @brightness.setter
    def brightness(self, brightness:float):
        '''Set the brightness of all lights in this group using `GroupController.brightness = ...`'''
        assert type(brightness) == float or type(brightness) == int
        bri_ = min(max(int(brightness * 254), 0), 254)
        self._api_request("PUT", "/action", {"bri": bri_})

    @property
    def hue(self) -> int:
        '''Get the last set hue in this group using `GroupController.hue`'''
        data = self._api_request()
        return data["action"]["hue"]

    @hue.setter
    def hue(self, hue:float):
        '''Set the hue of all lights in this group using `GroupController.hue = ...`'''
        assert type(hue) == float or type(hue) == int
        hue_ = min(max(int(hue * 65535), 0), 65535)
        self._api_request("PUT", "/action", {"hue": hue_})

    @property
    def saturation(self) -> int:
        '''Get the last set saturation in this group using `GroupController.saturation`'''
        data = self._api_request()
        return data["action"]["sat"]

    @saturation.setter
    def saturation(self, saturation:float):
        '''Set the saturation of all lights in this group using `GroupController.saturation = ...`'''
        assert type(saturation) == float or type(saturation) == int
        sat_ = min(max(int(saturation * 254), 0), 254)
        self._api_request("PUT", "/action", {"sat": sat_})

    @property
    def color_temperature(self):
        '''Get the last set white color temperature in Mired using `GroupController.color_temperature`'''
        data = self._api_request()
        return data["action"]["ct"]

    @color_temperature.setter
    def color_temperature(self, mired:int):
        '''Set the white color temperature in Mired (`154` - `500`) for all lights in this group using `GroupController.color_temperature = ...`'''
        assert type(mired) == int
        ct_ = min(max(mired, 154), 500)
        self._api_request("PUT", "/action", {"ct": ct_})

    def alert(self):
        '''Flash all lights in the group once.'''
        self._api_request("PUT", "/action", {"alert": "select"})

    def alert_long(self):
        '''Flash all lights in the group for 10 seconds.'''
        self._api_request("PUT", "/action", {"alert": "lselect"})
