import esphome.codegen as cg
from esphome.components import ble_client, sensor
import esphome.config_validation as cv
from esphome.const import (
    CONF_ALTITUDE,
    DEVICE_CLASS_EMPTY,
    DEVICE_CLASS_TEMPERATURE,
    STATE_CLASS_MEASUREMENT,
    UNIT_CELSIUS,
    UNIT_EMPTY,
    UNIT_METER,
    UNIT_SECOND,
)

from . import CONF_DIESEL_HEATER_BLE, DieselHeaterBLE

CODEOWNERS = ["@warehog"]
DEPENDENCIES = ["diesel_heater_ble"]
AUTO_LOAD = ["sensor"]

# Sensor con
