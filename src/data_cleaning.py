import pandas as pd
import numpy as np


def impute_missing_median(df, column):
    """Replace NaN in column with the column median."""
    median_val = df[column].median()
    df[column] = df[column].fillna(median_val)
    return df, median_val


def cap_outlier(df, column, upper=None, lower=None):
    """Cap values outside bounds to the boundary value."""
    if upper is not None:
        df[column] = df[column].clip(upper=upper)
    if lower is not None:
        df[column] = df[column].clip(lower=lower)
    return df


def flag_and_impute_sensor_fault(df, column, threshold_low):
    """Replace values below threshold with the column median."""
    median_val = df.loc[df[column] >= threshold_low, column].median()
    n_flagged = (df[column] < threshold_low).sum()
    df.loc[df[column] < threshold_low, column] = median_val
    return df, n_flagged


def clean_weather(df):
    """
    Apply all cleaning steps to the weather dataset.
    Returns the cleaned DataFrame and a log of decisions made.
    """
    data = df.copy()
    log = []

    data, med = impute_missing_median(data, 'rainfall_mm')
    log.append(f"rainfall_mm: 1 missing value imputed with median {round(med, 2)} mm (Mar 8)")

    data, med = impute_missing_median(data, 'humidity_pct')
    log.append(f"humidity_pct: 1 missing value imputed with median {round(med, 2)}% (Mar 21)")

    data = cap_outlier(data, 'temperature_c', upper=40.0)
    log.append("temperature_c: outlier 45.8C on Mar 14 capped at 40.0C (not physically realistic for Nairobi in March)")

    return data, log


def clean_soil(df):
    """
    Apply all cleaning steps to the soil sensor dataset.
    Returns the cleaned DataFrame and a log of decisions made.
    """
    data = df.copy()
    log = []

    data, med = impute_missing_median(data, 'soil_moisture_pct')
    log.append(f"soil_moisture_pct: 1 missing value imputed with median {round(med, 2)}% (Zone_B Mar 6)")

    data = cap_outlier(data, 'tank_level_liters', upper=6000)
    log.append("tank_level_liters: value of 9900L on Zone_C Mar 14 capped at 6000L (exceeds physical tank capacity)")

    data, n = flag_and_impute_sensor_fault(data, 'soil_moisture_pct', threshold_low=10.0)
    log.append(f"soil_moisture_pct: {n} value(s) below 10% replaced with median (likely sensor fault, Zone_B Mar 25)")

    return data, log
