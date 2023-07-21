# Table of Contents

* [yahuelib](#yahuelib)
* [yahuelib.utils](#yahuelib.utils)
  * [rgb\_to\_hsv](#yahuelib.utils.rgb_to_hsv)
* [yahuelib.controller](#yahuelib.controller)
  * [LightController](#yahuelib.controller.LightController)
    * [reachable](#yahuelib.controller.LightController.reachable)
    * [on](#yahuelib.controller.LightController.on)
    * [on](#yahuelib.controller.LightController.on)
    * [brightness](#yahuelib.controller.LightController.brightness)
    * [brightness](#yahuelib.controller.LightController.brightness)
    * [hue](#yahuelib.controller.LightController.hue)
    * [hue](#yahuelib.controller.LightController.hue)
    * [saturation](#yahuelib.controller.LightController.saturation)
    * [saturation](#yahuelib.controller.LightController.saturation)
    * [alert](#yahuelib.controller.LightController.alert)
    * [alert\_long](#yahuelib.controller.LightController.alert_long)
  * [GroupController](#yahuelib.controller.GroupController)
    * [any\_on](#yahuelib.controller.GroupController.any_on)
    * [all\_on](#yahuelib.controller.GroupController.all_on)
    * [all\_on](#yahuelib.controller.GroupController.all_on)
    * [brightness](#yahuelib.controller.GroupController.brightness)
    * [brightness](#yahuelib.controller.GroupController.brightness)
    * [hue](#yahuelib.controller.GroupController.hue)
    * [hue](#yahuelib.controller.GroupController.hue)
    * [saturation](#yahuelib.controller.GroupController.saturation)
    * [saturation](#yahuelib.controller.GroupController.saturation)
    * [alert](#yahuelib.controller.GroupController.alert)
    * [alert\_long](#yahuelib.controller.GroupController.alert_long)
* [yahuelib.exceptions](#yahuelib.exceptions)
  * [LightOrGroupNotFound](#yahuelib.exceptions.LightOrGroupNotFound)
  * [APIError](#yahuelib.exceptions.APIError)

<a id="yahuelib"></a>

# yahuelib

<a id="yahuelib.utils"></a>

# yahuelib.utils

<a id="yahuelib.utils.rgb_to_hsv"></a>

#### rgb\_to\_hsv

```python
def rgb_to_hsv(r: int, g: int, b: int) -> tuple
```

Convert RGB colors `(255, 220, 100)` to HSV `(0.129, 0.608, 1.0)`

<a id="yahuelib.controller"></a>

# yahuelib.controller

<a id="yahuelib.controller.LightController"></a>

## LightController Objects

```python
class LightController(_BaseController)
```

Control a Philips Hue Light using the API of your Hue Bridge.

**Arguments**:

  - `number: int` - The number of your light
  - `bridge_ip_address: str` - The IP address of your Hue Bridge
  - `bridge_api_user: str` - The user used to authenticate to the API
  
  Use the class method `.from_name(name:str, ...)` to use the name of a light instead of the number.

<a id="yahuelib.controller.LightController.reachable"></a>

#### reachable

```python
@property
def reachable() -> bool
```

Check if the light is reachable using `LightController.reachable`

<a id="yahuelib.controller.LightController.on"></a>

#### on

```python
@property
def on() -> bool
```

Check if the light is on using `LightController.on`

<a id="yahuelib.controller.LightController.on"></a>

#### on

```python
@on.setter
def on(on: bool)
```

Turn the light on/off using `LightController.on = ...`

<a id="yahuelib.controller.LightController.brightness"></a>

#### brightness

```python
@property
def brightness() -> int
```

Get the brightness using `LightController.brightness`

<a id="yahuelib.controller.LightController.brightness"></a>

#### brightness

```python
@brightness.setter
def brightness(brightness: float)
```

Set the brightness using `LightController.brightness = ...`

<a id="yahuelib.controller.LightController.hue"></a>

#### hue

```python
@property
def hue() -> int
```

Get the hue using `LightController.hue`

<a id="yahuelib.controller.LightController.hue"></a>

#### hue

```python
@hue.setter
def hue(hue: float)
```

Set the hue using `LightController.hue = ...`

<a id="yahuelib.controller.LightController.saturation"></a>

#### saturation

```python
@property
def saturation() -> int
```

Get the saturation using `LightController.saturation`

<a id="yahuelib.controller.LightController.saturation"></a>

#### saturation

```python
@saturation.setter
def saturation(saturation: float)
```

Set the saturation using `LightController.saturation = ...`

<a id="yahuelib.controller.LightController.alert"></a>

#### alert

```python
def alert()
```

Flash the light once.

<a id="yahuelib.controller.LightController.alert_long"></a>

#### alert\_long

```python
def alert_long()
```

Flash the light for 10 seconds.

<a id="yahuelib.controller.GroupController"></a>

## GroupController Objects

```python
class GroupController(_BaseController)
```

Control a Philips Hue Light Group (Room/Zone) using the API of your Hue Bridge.

**Arguments**:

  - `number: int` - The number of your light group
  - `bridge_ip_address: str` - The IP address of your Hue Bridge
  - `bridge_api_user: str` - The user used to authenticate to the API
  
  Use the class method `.from_name(name:str, ...)` to use the name of a group instead of the number.

<a id="yahuelib.controller.GroupController.any_on"></a>

#### any\_on

```python
@property
def any_on() -> bool
```

Check if any light in this group is on using `GroupController.any_on`

<a id="yahuelib.controller.GroupController.all_on"></a>

#### all\_on

```python
@property
def all_on() -> bool
```

Check if all lights in this group are on using `GroupController.all_on`

<a id="yahuelib.controller.GroupController.all_on"></a>

#### all\_on

```python
@all_on.setter
def all_on(on: bool)
```

Turn on/off all lights in this group using `GroupController.all_on = ...`

<a id="yahuelib.controller.GroupController.brightness"></a>

#### brightness

```python
@property
def brightness() -> int
```

Get the last set brightness in this group using `GroupController.brightness`

<a id="yahuelib.controller.GroupController.brightness"></a>

#### brightness

```python
@brightness.setter
def brightness(brightness: float)
```

Set the brightness of all lights in this group using `GroupController.brightness = ...`

<a id="yahuelib.controller.GroupController.hue"></a>

#### hue

```python
@property
def hue() -> int
```

Get the last set hue in this group using `GroupController.hue`

<a id="yahuelib.controller.GroupController.hue"></a>

#### hue

```python
@hue.setter
def hue(hue: float)
```

Set the hue of all lights in this group using `GroupController.hue = ...`

<a id="yahuelib.controller.GroupController.saturation"></a>

#### saturation

```python
@property
def saturation() -> int
```

Get the last set saturation in this group using `GroupController.saturation`

<a id="yahuelib.controller.GroupController.saturation"></a>

#### saturation

```python
@saturation.setter
def saturation(saturation: float)
```

Set the saturation of all lights in this group using `GroupController.saturation = ...`

<a id="yahuelib.controller.GroupController.alert"></a>

#### alert

```python
def alert()
```

Flash all lights in the group once.

<a id="yahuelib.controller.GroupController.alert_long"></a>

#### alert\_long

```python
def alert_long()
```

Flash all lights in the group for 10 seconds.

<a id="yahuelib.exceptions"></a>

# yahuelib.exceptions

<a id="yahuelib.exceptions.LightOrGroupNotFound"></a>

## LightOrGroupNotFound Objects

```python
class LightOrGroupNotFound(Exception)
```

`LightOrGroupNotFound` Exception

<a id="yahuelib.exceptions.APIError"></a>

## APIError Objects

```python
class APIError(Exception)
```

Generic `APIError` Exception

