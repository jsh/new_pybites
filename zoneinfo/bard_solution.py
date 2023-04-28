def convert_timezone(dt: datetime, tz: str) -> datetime:
  """Converts a datetime object from one timezone to another timezone.

  Args:
    dt: The datetime object to convert.
    tz: The timezone to convert to.

  Returns:
    The converted datetime object.
  """

  # Create a timezone object for the target timezone.
  target_timezone = ZoneInfo(tz)

  # Convert the datetime object to the target timezone.
  converted_dt = dt.astimezone(target_timezone)

  # Return the converted datetime object.
  return converted_dt

"""
>>> from datetime import datetime
>>> from zoneinfo import ZoneInfo
>>> dt = datetime(2022, 5, 1, 12, 0, tzinfo=ZoneInfo('America/Los_Angeles'))
>>> convert_timezone(dt, 'Europe/London')
datetime.datetime(2022, 5, 1, 20, 0, tzinfo=zoneinfo.ZoneInfo(key='Europe/London'))
"""