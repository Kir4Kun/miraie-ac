from enum import Enum


class DisplayMode(Enum):
    """Enum for Display mode."""

    ON = "on"
    OFF = "off"


class FanMode(Enum):
    """Enum for fan mode."""

    AUTO = "auto"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    QUIET = "quiet"


class HVACMode(Enum):
    """Enum for HVAC mode."""

    COOL = "cool"
    AUTO = "auto"
    DRY = "dry"
    FAN = "fan"


class PowerMode(Enum):
    """Enum for power mode."""

    ON = "on"
    OFF = "off"


class PresetMode(Enum):
    """Enum for Preset mode."""

    NONE = "none"
    ECO = "eco"
    BOOST = "boost"


class SwingMode(Enum):
    """Enum for Swing mode."""

    AUTO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
