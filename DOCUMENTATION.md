# Table of Contents

* [yahuelib](#yahuelib)
* [yahuelib.controller](#yahuelib.controller)
  * [LightController](#yahuelib.controller.LightController)
    * [check\_reachable](#yahuelib.controller.LightController.check_reachable)
    * [check\_on](#yahuelib.controller.LightController.check_on)
    * [set\_on](#yahuelib.controller.LightController.set_on)
    * [get\_brightness](#yahuelib.controller.LightController.get_brightness)
    * [set\_brightness](#yahuelib.controller.LightController.set_brightness)
    * [get\_hue](#yahuelib.controller.LightController.get_hue)
    * [set\_hue](#yahuelib.controller.LightController.set_hue)
    * [get\_saturation](#yahuelib.controller.LightController.get_saturation)
    * [set\_saturation](#yahuelib.controller.LightController.set_saturation)
    * [get\_color\_temperature](#yahuelib.controller.LightController.get_color_temperature)
    * [set\_color\_temperature](#yahuelib.controller.LightController.set_color_temperature)
    * [alert](#yahuelib.controller.LightController.alert)
    * [alert\_long](#yahuelib.controller.LightController.alert_long)
  * [GroupController](#yahuelib.controller.GroupController)
    * [check\_any\_on](#yahuelib.controller.GroupController.check_any_on)
    * [check\_all\_on](#yahuelib.controller.GroupController.check_all_on)
    * [set\_all\_on](#yahuelib.controller.GroupController.set_all_on)
    * [get\_brightness](#yahuelib.controller.GroupController.get_brightness)
    * [set\_brightness](#yahuelib.controller.GroupController.set_brightness)
    * [get\_hue](#yahuelib.controller.GroupController.get_hue)
    * [set\_hue](#yahuelib.controller.GroupController.set_hue)
    * [get\_saturation](#yahuelib.controller.GroupController.get_saturation)
    * [set\_saturation](#yahuelib.controller.GroupController.set_saturation)
    * [get\_color\_temperature](#yahuelib.controller.GroupController.get_color_temperature)
    * [set\_color\_temperature](#yahuelib.controller.GroupController.set_color_temperature)
    * [alert](#yahuelib.controller.GroupController.alert)
    * [alert\_long](#yahuelib.controller.GroupController.alert_long)
  * [MotionSensor](#yahuelib.controller.MotionSensor)
    * [check\_on](#yahuelib.controller.MotionSensor.check_on)
    * [set\_on](#yahuelib.controller.MotionSensor.set_on)
    * [check\_reachable](#yahuelib.controller.MotionSensor.check_reachable)
    * [get\_battery](#yahuelib.controller.MotionSensor.get_battery)
    * [get\_sensitivity](#yahuelib.controller.MotionSensor.get_sensitivity)
    * [set\_sensitivity](#yahuelib.controller.MotionSensor.set_sensitivity)
    * [get\_sensitivitymax](#yahuelib.controller.MotionSensor.get_sensitivitymax)
    * [check\_ledindication](#yahuelib.controller.MotionSensor.check_ledindication)
    * [set\_ledindication](#yahuelib.controller.MotionSensor.set_ledindication)
    * [get\_presence](#yahuelib.controller.MotionSensor.get_presence)
* [yahuelib.utils](#yahuelib.utils)
  * [rgb\_to\_hsv](#yahuelib.utils.rgb_to_hsv)
  * [kelvin\_to\_mired](#yahuelib.utils.kelvin_to_mired)
* [yahuelib.exceptions](#yahuelib.exceptions)
  * [DeviceNotFound](#yahuelib.exceptions.DeviceNotFound)
  * [APIError](#yahuelib.exceptions.APIError)

<a id="yahuelib"></a>

# yahuelib

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

<a id="yahuelib.controller.LightController.check_reachable"></a>

#### check\_reachable

```python
def check_reachable() -> bool
```

Check if the light is reachable

<a id="yahuelib.controller.LightController.check_on"></a>

#### check\_on

```python
def check_on() -> bool
```

Check if the light is on

<a id="yahuelib.controller.LightController.set_on"></a>

#### set\_on

```python
def set_on(on: bool)
```

Turn the light on/off

<a id="yahuelib.controller.LightController.get_brightness"></a>

#### get\_brightness

```python
def get_brightness() -> int
```

Get the brightness

<a id="yahuelib.controller.LightController.set_brightness"></a>

#### set\_brightness

```python
def set_brightness(brightness: int)
```

Set the brightness (`0` - `254`)

<a id="yahuelib.controller.LightController.get_hue"></a>

#### get\_hue

```python
def get_hue() -> int
```

Get the hue

<a id="yahuelib.controller.LightController.set_hue"></a>

#### set\_hue

```python
def set_hue(hue: int)
```

Set the hue (0 - 65535)

<a id="yahuelib.controller.LightController.get_saturation"></a>

#### get\_saturation

```python
def get_saturation() -> int
```

Get the saturation

<a id="yahuelib.controller.LightController.set_saturation"></a>

#### set\_saturation

```python
def set_saturation(saturation: int)
```

Set the saturation (`0` - `254`)

<a id="yahuelib.controller.LightController.get_color_temperature"></a>

#### get\_color\_temperature

```python
def get_color_temperature() -> int
```

Get the white color temperature in Mired

<a id="yahuelib.controller.LightController.set_color_temperature"></a>

#### set\_color\_temperature

```python
def set_color_temperature(mired: int)
```

Set the white color temperature in Mired (`154` - `500`)

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

<a id="yahuelib.controller.GroupController.check_any_on"></a>

#### check\_any\_on

```python
def check_any_on() -> bool
```

Check if any light in this group is on

<a id="yahuelib.controller.GroupController.check_all_on"></a>

#### check\_all\_on

```python
def check_all_on() -> bool
```

Check if all lights in this group are on

<a id="yahuelib.controller.GroupController.set_all_on"></a>

#### set\_all\_on

```python
def set_all_on(on: bool)
```

Turn on/off all lights in this group

<a id="yahuelib.controller.GroupController.get_brightness"></a>

#### get\_brightness

```python
def get_brightness()
```

Get the last set brightness in this group

<a id="yahuelib.controller.GroupController.set_brightness"></a>

#### set\_brightness

```python
def set_brightness(brightness: int)
```

Set the brightness (`0` - `254`) of all lights in this group

<a id="yahuelib.controller.GroupController.get_hue"></a>

#### get\_hue

```python
def get_hue() -> int
```

Get the last set hue in this group

<a id="yahuelib.controller.GroupController.set_hue"></a>

#### set\_hue

```python
def set_hue(hue: int)
```

Set the hue (`0` - `65535`) of all lights in this group

<a id="yahuelib.controller.GroupController.get_saturation"></a>

#### get\_saturation

```python
def get_saturation() -> int
```

Get the last set saturation in this group

<a id="yahuelib.controller.GroupController.set_saturation"></a>

#### set\_saturation

```python
def set_saturation(saturation: int)
```

Set the saturation (`0` - `254`) of all lights in this group

<a id="yahuelib.controller.GroupController.get_color_temperature"></a>

#### get\_color\_temperature

```python
def get_color_temperature() -> int
```

Get the last set white color temperature in Mired

<a id="yahuelib.controller.GroupController.set_color_temperature"></a>

#### set\_color\_temperature

```python
def set_color_temperature(mired: int)
```

Set the white color temperature in Mired (`154` - `500`) for all lights in this group

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

<a id="yahuelib.controller.MotionSensor"></a>

## MotionSensor Objects

```python
class MotionSensor(_BaseController)
```

<a id="yahuelib.controller.MotionSensor.check_on"></a>

#### check\_on

```python
def check_on() -> bool
```

Check if the sensor is on

<a id="yahuelib.controller.MotionSensor.set_on"></a>

#### set\_on

```python
def set_on(on: bool)
```

Turn the sensor on/off

<a id="yahuelib.controller.MotionSensor.check_reachable"></a>

#### check\_reachable

```python
def check_reachable() -> bool
```

Check if the sensor is reachable

<a id="yahuelib.controller.MotionSensor.get_battery"></a>

#### get\_battery

```python
def get_battery() -> int
```

Get the current charge of the battery in percent

<a id="yahuelib.controller.MotionSensor.get_sensitivity"></a>

#### get\_sensitivity

```python
def get_sensitivity() -> int
```

Get the sensitivity of the sensor

<a id="yahuelib.controller.MotionSensor.set_sensitivity"></a>

#### set\_sensitivity

```python
def set_sensitivity(sensitivity: int)
```

Set the sensitivity of the sensor

<a id="yahuelib.controller.MotionSensor.get_sensitivitymax"></a>

#### get\_sensitivitymax

```python
def get_sensitivitymax() -> int
```

Get the maximum sensititvity of the sensor

<a id="yahuelib.controller.MotionSensor.check_ledindication"></a>

#### check\_ledindication

```python
def check_ledindication() -> bool
```

Check if the LED indication is turned on or off

<a id="yahuelib.controller.MotionSensor.set_ledindication"></a>

#### set\_ledindication

```python
def set_ledindication(on: bool)
```

Turn the LED indicator on/off

<a id="yahuelib.controller.MotionSensor.get_presence"></a>

#### get\_presence

```python
def get_presence() -> bool
```

Check if the motion sensor detected the presence of someone in it's reach

<a id="yahuelib.utils"></a>

# yahuelib.utils

<a id="yahuelib.utils.rgb_to_hsv"></a>

#### rgb\_to\_hsv

```python
def rgb_to_hsv(r: int, g: int, b: int) -> tuple
```

Convert RGB colors `(255, 220, 100)` to Philips Hue's hue, saturation and brightness values `(8456, 154, 254)` imprecisely

<a id="yahuelib.utils.kelvin_to_mired"></a>

#### kelvin\_to\_mired

```python
def kelvin_to_mired(kelvin: int)
```

Convert the color temperature from Kelvin to Mired

<a id="yahuelib.exceptions"></a>

# yahuelib.exceptions

<a id="yahuelib.exceptions.DeviceNotFound"></a>

## DeviceNotFound Objects

```python
class DeviceNotFound(Exception)
```

`DeviceNotFound` Exception

<a id="yahuelib.exceptions.APIError"></a>

## APIError Objects

```python
class APIError(Exception)
```

Generic `APIError` Exception

