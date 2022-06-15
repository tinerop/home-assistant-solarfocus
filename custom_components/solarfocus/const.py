"""Constants for the Solarfocus integration."""

from typing import Final
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.const import (
    ENERGY_KILO_WATT_HOUR,
    PERCENTAGE,
    POWER_WATT,
    TEMP_CELSIUS,
)

DOMAIN = "solarfocus"

"""Default values for configuration"""
DEFAULT_HOST = "solarfocus.local"
DEFAULT_PORT = 502
DEFAULT_NAME = "Solarfocus"
DEFAULT_SCAN_INTERVAL = 10

"""Configuration and options"""
CONF_HEATING_CIRCUIT = "heating_circuit"
CONF_BUFFER = "buffer"
CONF_BOILER = "boiler"
CONF_HEATPUMP = "heatpump"
CONF_PHOTOVOLTAIC = "photovoltaic"

"""Custom Measurement Units"""
VOLUME_FLOW_RATE_LITER_PER_HOUR: Final = "l/h"
REVOLUTIONS_PER_MIN: Final = "rpm"


"""Supported sensor types."""
HEATING_CIRCUIT_SENSOR_TYPES = [
    SensorEntityDescription(
        key="hc1_supply_temp",
        name="Heating Supply Temperatur",
        native_unit_of_measurement=TEMP_CELSIUS,
        icon="mdi:thermometer",
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="hc1_room_temp",
        name="Heating Room Temperatur",
        native_unit_of_measurement=TEMP_CELSIUS,
        icon="mdi:thermometer",
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="hc1_humidity",
        name="Heating Humidity",
        native_unit_of_measurement=PERCENTAGE,
        icon="mdi:water-percent",
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="hc1_limit_thermostat",
        name="Heating Limit Thermostat",
        icon="mdi:thermostat",
        device_class="solarfocus__limit",
    ),
    SensorEntityDescription(
        key="hc1_mixer_valve",
        name="Heating Mixer Valve",
        native_unit_of_measurement=PERCENTAGE,
        icon="mdi:valve",
    ),
    SensorEntityDescription(
        key="hc1_state",
        name="Heating State",
        icon="mdi:radiator",
        device_class="solarfocus__hcstate",
    ),
]


BUFFER_SENSOR_TYPES = [
    SensorEntityDescription(
        key="bu1_top_temp",
        name="Buffer Top Temperatur",
        native_unit_of_measurement=TEMP_CELSIUS,
        icon="mdi:thermometer",
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="bu1_bottom_temp",
        name="Buffer Bottom Temperatur",
        native_unit_of_measurement=TEMP_CELSIUS,
        icon="mdi:thermometer",
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="bu1_pump",
        name="Buffer Pump",
        icon="mdi:pump",
        device_class="solarfocus__pump",
    ),
    SensorEntityDescription(
        key="bu1_state",
        name="Buffer State",
        icon="mdi:database",
        device_class="solarfocus__bustate",
    ),
    SensorEntityDescription(
        key="bu1_mode",
        name="Buffer Mode",
        icon="mdi:format-list-bulleted",
        device_class="solarfocus__bumode",
    ),
]

BOILER_SENSOR_TYPES = [
    SensorEntityDescription(
        key="bo1_temp",
        name="Boiler Temperatur",
        native_unit_of_measurement=TEMP_CELSIUS,
        icon="mdi:thermometer",
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="bo1_state",
        name="Boiler State",
        icon="mdi:water-boiler",
        device_class="solarfocus__bostate",
    ),
    SensorEntityDescription(
        key="bo1_mode",
        name="Boiler Mode",
        icon="mdi:format-list-bulleted",
        device_class="solarfocus__bomode",
    ),
]

HEATPUMP_SENSOR_TYPES = [
    SensorEntityDescription(
        key="hp_supply_temp",
        name="Heatpump Supply Temperature",
        native_unit_of_measurement=TEMP_CELSIUS,
        icon="mdi:thermometer",
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="hp_return_temp",
        name="Heatpump Return Temperature",
        native_unit_of_measurement=TEMP_CELSIUS,
        icon="mdi:thermometer",
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="hp_flow_rate",
        name="Heatpump Supply Temperature",
        native_unit_of_measurement=VOLUME_FLOW_RATE_LITER_PER_HOUR,
        icon="mdi:thermometer",
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="hp_compressor_speed",
        name="Heatpump Compressor Speed",
        native_unit_of_measurement=REVOLUTIONS_PER_MIN,
        icon="mdi:gauge",
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="hp_evu_lock_active",
        name="Heatpump EVU lock",
        icon="mdi:lock",
        device_class="solarfocus__evu",
    ),
    SensorEntityDescription(
        key="hp_defrost_active",
        name="Heatpump Defrost",
        icon="mdi:snowflake-melt",
        device_class="solarfocus__defrost",
    ),
    SensorEntityDescription(
        key="hp_boiler_charge",
        name="Heatpump Boiler Charge",
        icon="mdi:water-boiler",
        device_class="solarfocus__boiler",
    ),
    SensorEntityDescription(
        key="hp_thermal_energy_total",
        name="Heatpump Total Thermal Energy",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        icon="mdi:meter-gas-outline",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
    ),
    SensorEntityDescription(
        key="hp_thermal_energy_drinking_water",
        name="Heatpump Drinking Water Thermal Energy",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        icon="mdi:meter-gas-outline",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
    ),
    SensorEntityDescription(
        key="hp_thermal_energy_heating",
        name="Heatpump Heating Thermal Energy",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        icon="mdi:meter-gas-outline",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
    ),
    SensorEntityDescription(
        key="hp_electrical_energy_total",
        name="Heatpump Total Electrical Energy",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        icon="mdi:meter-electric-outline",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
    ),
    SensorEntityDescription(
        key="hp_electrical_energy_drinking_water",
        name="Heatpump Drinking Water Electrical Energy",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        icon="mdi:meter-electric-outline",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
    ),
    SensorEntityDescription(
        key="hp_eletrical_energy_heating",
        name="Heatpump Heating Electrical Energy",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        icon="mdi:meter-electric-outline",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
    ),
    SensorEntityDescription(
        key="hp_electrical_power",
        name="Heatpump Electrical Power",
        native_unit_of_measurement=POWER_WATT,
        icon="mdi:lightning-bolt",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="hp_thermal_power_cooling",
        name="Heatpump Cooling Thermal Power",
        native_unit_of_measurement=POWER_WATT,
        icon="mdi:snowflake",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="hp_thermal_power_heating",
        name="Heatpump Heating Thermal Power",
        native_unit_of_measurement=POWER_WATT,
        icon="mdi:fire",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="hp_thermal_energy_cooling",
        name="Heatpump Cooling Thermal Energy",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        icon="mdi:meter-gas-outline",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
    ),
    SensorEntityDescription(
        key="hp_electrical_energy_cooling",
        name="Heatpump Cooling Electrical Energy",
        native_unit_of_measurement=POWER_WATT,
        icon="mdi:meter-gas-outline",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="hp_vampair_state",
        name="Heatpump State",
        icon="mdi:heat-pump-outline",
        device_class="solarfocus__hpstate",
    ),
]

PV_SENSOR_TYPES = [
    SensorEntityDescription(
        key="pv_power",
        name="Photovolatic Power",
        native_unit_of_measurement=POWER_WATT,
        icon="mdi:solar-power",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="pv_house_consumption",
        name="Photovolatic House Consumption",
        native_unit_of_measurement=POWER_WATT,
        icon="mdi:home-lightning-bolt-outline",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="pv_heatpump_consumption",
        name="Photovolatic Heatpump Consumption",
        native_unit_of_measurement=POWER_WATT,
        icon="mdi:heat-pump-outline",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="pv_grid_import",
        name="Photovolatic Grid Import",
        native_unit_of_measurement=POWER_WATT,
        icon="mdi:home-import-outline",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="pv_grid_export",
        name="Photovolatic Grid Export",
        native_unit_of_measurement=POWER_WATT,
        icon="mdi:home-export-outline",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
]