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
        raise DeviceNotFound()

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

    def check_reachable(self) -> bool:
        '''Check if the light is reachable'''
        data = self._api_request()["state"]["reachable"]
        return data

    def check_on(self) -> bool:
        '''Check if the light is on'''
        data = self._api_request()["state"]["on"]
        return data

    def set_on(self, on:bool):
        '''Turn the light on/off'''
        assert type(on) == bool
        self._api_request("PUT", "/state", {"on": on})

    def get_brightness(self) -> int:
        '''Get the brightness'''
        data = self._api_request()["state"]["bri"]
        return data

    def set_brightness(self, brightness:int):
        '''Set the brightness (`0` - `254`)'''
        assert type(brightness) == int
        bri_ = min(max(brightness, 0), 254)
        self._api_request("PUT", "/state", {"bri": bri_})

    def get_hue(self) -> int:
        '''Get the hue'''
        data = self._api_request()["state"]["hue"]
        return data

    def set_hue(self, hue:int):
        '''Set the hue (0 - 65535)'''
        assert type(hue) == int
        hue_ = min(max(hue, 0), 65535)
        self._api_request("PUT", "/state", {"hue": hue_})

    def get_saturation(self) -> int:
        '''Get the saturation'''
        data = self._api_request()["state"]["sat"]
        return data

    def set_saturation(self, saturation:int):
        '''Set the saturation (`0` - `254`)'''
        assert type(saturation) == int
        sat_ = min(max(saturation, 0), 254)
        self._api_request("PUT", "/state", {"sat": sat_})

    def get_color_temperature(self) -> int:
        '''Get the white color temperature in Mired'''
        data = self._api_request()["state"]["ct"]
        return data

    def set_color_temperature(self, mired:int):
        '''Set the white color temperature in Mired (`154` - `500`)'''
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

    def check_any_on(self) -> bool:
        '''Check if any light in this group is on'''
        data = self._api_request()["state"]["any_on"]
        return data

    def check_all_on(self) -> bool:
        '''Check if all lights in this group are on'''
        data = self._api_request()["state"]["all_on"]
        return data

    def set_all_on(self, on:bool):
        '''Turn on/off all lights in this group'''
        assert type(on) == bool
        self._api_request("PUT", "/action", {"on": on})

    def get_brightness(self):
        '''Get the last set brightness in this group'''
        data = self._api_request()["action"]["bri"]
        return data

    def set_brightness(self, brightness:int):
        '''Set the brightness (`0` - `254`) of all lights in this group'''
        assert type(brightness) == int
        bri_ = min(max(brightness, 0), 254)
        self._api_request("PUT", "/action", {"bri": bri_})

    def get_hue(self) -> int:
        '''Get the last set hue in this group'''
        data = self._api_request()["action"]["hue"]
        return data

    def set_hue(self, hue:int):
        '''Set the hue (`0` - `65535`) of all lights in this group'''
        assert type(hue) == int
        hue_ = min(max(hue, 0), 65535)
        self._api_request("PUT", "/action", {"hue": hue_})

    def get_saturation(self) -> int:
        '''Get the last set saturation in this group'''
        data = self._api_request()["action"]["sat"]
        return data

    def set_saturation(self, saturation:int):
        '''Set the saturation (`0` - `254`) of all lights in this group'''
        assert type(saturation) == int
        sat_ = min(max(saturation, 0), 254)
        self._api_request("PUT", "/action", {"sat": sat_})

    def get_color_temperature(self) -> int:
        '''Get the last set white color temperature in Mired'''
        data = self._api_request()["action"]["ct"]
        return data

    def set_color_temperature(self, mired:int):
        '''Set the white color temperature in Mired (`154` - `500`) for all lights in this group'''
        assert type(mired) == int
        ct_ = min(max(mired, 154), 500)
        self._api_request("PUT", "/action", {"ct": ct_})

    def alert(self):
        '''Flash all lights in the group once.'''
        self._api_request("PUT", "/action", {"alert": "select"})

    def alert_long(self):
        '''Flash all lights in the group for 10 seconds.'''
        self._api_request("PUT", "/action", {"alert": "lselect"})


class MotionSensor(_BaseController):

    _api_endpoint_all = "https://{bridge_ip_address}/api/{bridge_api_user}/sensors"
    _api_endpoint_specific = "https://{bridge_ip_address}/api/{bridge_api_user}/sensors/{number}"

    def check_on(self) -> bool:
        '''Check if the sensor is on'''
        data = self._api_request()["config"]["on"]
        return data

    def set_on(self, on:bool):
        '''Turn the sensor on/off'''
        assert type(on) == bool
        self._api_request("PUT", "/config", {"on": on})

    def check_reachable(self) -> bool:
        '''Check if the sensor is reachable'''
        data = self._api_request()["config"]["reachable"]
        return data

    def get_battery(self) -> int:
        '''Get the current charge of the battery in percent'''
        data = self._api_request()
        return data["config"]["battery"]

    def get_sensitivity(self) -> int:
        '''Get the sensitivity of the sensor'''
        data = self._api_request()["config"]["sensitivity"]
        return data

    def set_sensitivity(self, sensitivity:int):
        '''Set the sensitivity of the sensor'''
        assert type(sensitivity) == int
        sensitivity_ = min(max(sensitivity, 0), int(self.get_sensitivitymax()))
        self._api_request("PUT", "/config", {"sensitivity": sensitivity_})

    def get_sensitivitymax(self) -> int:
        '''Get the maximum sensititvity of the sensor'''
        data = self._api_request()["config"]["sensitivitymax"]
        return data

    def check_ledindication(self) -> bool:
        '''Check if the LED indication is turned on or off'''
        data = self._api_request()["config"]["ledindication"]
        return data

    def set_ledindication(self, on:bool):
        '''Turn the LED indicator on/off'''
        assert type(on) == bool
        self._api_request("PUT", "/config", {"ledindication": on})

    def get_presence(self) -> bool:
        '''Check if the motion sensor detected the presence of someone in it's reach'''
        data = self._api_request()["state"]["presence"]
        return data
