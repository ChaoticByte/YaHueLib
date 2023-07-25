# YaHue Lib

Yet Another Philips Hue API Library for Python. This project only implements home subset of the API.

## Getting Started

Before you can use the API of your Hue Bridge, you have to create an API user for it.  
See https://developers.meethue.com/develop/get-started-2/

## Supported Features

- 💡 Lights
    - reachable
    - on
    - brightness
    - hue
    - saturation
    - white color temperature
    - alert
    - alert_long
- 🏠 Groups (Zones and Rooms)
    - any_on
    - all_on
    - brightness
    - hue
    - saturation
    - white color temperature
    - alert
    - alert_long

## Documentation

see [DOCUMENTATION.md](DOCUMENTATION.md)

## Example

```python
#!/usr/bin/env python3

# from yahuelib.controller import LightController
from yahuelib.controller import GroupController
from yahuelib.utils import rgb_to_hsv

if __name__ == "__main__":
    home = GroupController.from_name("Home", "192.168.0.120", "XXXXXXXXXXXXXXXXXXX-XXXXXXXXXXXXXXXXXXXX")
    if not home.check_all_on():
        home.set_all_on(True)
    color = rgb_to_hsv(255, 220, 100)
    home.set_hue(color[0])
    home.set_saturation(color[1])
    home.set_brightness(1.0)
    home.alert()
```
