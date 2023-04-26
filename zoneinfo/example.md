# The Zoneinfo Module

Sure, here's an exercise that illustrates and teaches Python's new `zoneinfo` module:

## Bite: Timezone Converter

In this Bite, you will write a function that converts a datetime object from one timezone to another timezone using Python's new `zoneinfo` module.

The function should work with any datetime object and any valid timezone string:

```python
>>> from datetime import datetime
>>> from zoneinfo import ZoneInfo
>>> dt = datetime(2022, 5, 1, 12, 0, tzinfo=ZoneInfo('America/Los_Angeles'))
>>> convert_timezone(dt, 'Europe/London')
datetime.datetime(2022, 5, 1, 20, 0, tzinfo=zoneinfo.ZoneInfo(key='Europe/London'))
```

### Signature

```python
def convert_timezone(dt: datetime, tz: str) -> datetime:
    pass
```


### Tips

- Use the `zoneinfo.ZoneInfo` class to create timezone objects.
- Use the `datetime.astimezone()` method to convert a datetime object from one timezone to another timezone.
- You can pass a string representing a timezone to the `ZoneInfo` constructor or use one of the predefined timezones from the `zoneinfo.available_timezones()` list.