"""Dataset loaders and reproducible offline fallbacks for the exercise notebooks."""

from __future__ import annotations

from io import BytesIO
from urllib.request import Request, urlopen

import numpy as np
import pandas as pd


CCPP_URL = "https://risk-engineering.org/static/data/CCPP.csv"
AI4I_URLS = [
    "https://archive.ics.uci.edu/ml/machine-learning-databases/00601/ai4i2020.csv",
    (
        "https://raw.githubusercontent.com/SamyamoyRakshit/"
        "AI4I-2020-Predictive-Maintenance-Dataset__Linear-Regression/"
        "main/ai4i2020.csv"
    ),
]


def _download(url: str, timeout: int = 8) -> bytes:
    request = Request(url, headers={"User-Agent": "AI-Summer-School/1.0"})
    with urlopen(request, timeout=timeout) as response:
        return response.read()


def _with_source(df: pd.DataFrame, source: str) -> pd.DataFrame:
    df.attrs["source"] = source
    print(f"Loaded {source}: {df.shape[0]} rows × {df.shape[1]} columns")
    return df


def make_synthetic_ccpp(n: int = 9568, seed: int = 42) -> pd.DataFrame:
    """Physics-shaped fallback matching the CCPP schema and published statistics."""
    rng = np.random.default_rng(seed)
    at = np.clip(rng.normal(19.65, 7.45, n), 1.81, 37.11)
    vacuum = np.clip(28.0 + 1.34 * at + rng.normal(0, 6.0, n), 25.36, 81.56)
    pressure = np.clip(1016.2 - 0.15 * at + rng.normal(0, 5.5, n), 992.89, 1033.30)
    humidity = np.clip(88.0 - 0.75 * at + rng.normal(0, 12.0, n), 25.56, 100.16)
    power = (
        454.61
        - 1.98 * at
        - 0.234 * vacuum
        + 0.062 * (pressure - 1013.0)
        - 0.158 * (humidity - 73.3)
        - 0.028 * (at - 20.0) ** 2
        + 0.010 * (at - 20.0) * (humidity - 73.3)
        + rng.normal(0, 3.0, n)
    )
    power = power - power.mean() + 454.37
    return pd.DataFrame(
        {"AT": at, "V": vacuum, "AP": pressure, "RH": humidity, "PE": power}
    ).round(2)


def load_ccpp(prefer_real: bool = True) -> pd.DataFrame:
    """Load the real CCPP data, or a seeded fallback when unavailable."""
    if prefer_real:
        try:
            df = pd.read_csv(BytesIO(_download(CCPP_URL)))
            df = df[["AT", "V", "AP", "RH", "PE"]]
            return _with_source(df, "REAL CCPP data")
        except Exception as error:
            print(f"Real CCPP download unavailable ({type(error).__name__}); using fallback.")
    return _with_source(make_synthetic_ccpp(), "SEEDED CCPP fallback")


def make_synthetic_ai4i(n: int = 10000, seed: int = 42) -> pd.DataFrame:
    """Physics-based fallback matching the AI4I predictive-maintenance schema."""
    rng = np.random.default_rng(seed)
    innovation = rng.normal(0, 1, n)
    air = np.zeros(n)
    for k in range(1, n):
        air[k] = 0.999 * air[k - 1] + innovation[k]
    air = 300 + 2.0 * (air - air.mean()) / air.std()
    process = air + 10 + rng.normal(0, 1.0, n)

    z1, z2 = rng.normal(0, 1, n), rng.normal(0, 1, n)
    rho = -0.85
    torque = np.clip(40 + 10 * z1, 4, 77)
    speed = np.clip(
        1540 + 180 * (rho * z1 + np.sqrt(1 - rho**2) * z2), 1160, 2900
    )
    machine_type = rng.choice(["L", "M", "H"], size=n, p=[0.6, 0.3, 0.1])
    tool_wear = rng.uniform(0, 240, n).astype(int)

    power = torque * speed * 2 * np.pi / 60
    temperature_gap = process - air
    twf = (tool_wear >= 200) & (rng.random(n) < 0.09)
    hdf = (temperature_gap < 8.6) & (speed < 1380)
    pwf = (power < 3500) | (power > 9000)
    limit = np.where(machine_type == "L", 11000, np.where(machine_type == "M", 12000, 13000))
    osf = tool_wear * torque > limit
    rnf = rng.random(n) < 0.001
    fail = twf | hdf | pwf | osf | rnf

    return pd.DataFrame(
        {
            "type": machine_type,
            "air_temp": air.round(1),
            "proc_temp": process.round(1),
            "speed": speed.round(0),
            "torque": torque.round(1),
            "tool_wear": tool_wear,
            "TWF": twf.astype(int),
            "HDF": hdf.astype(int),
            "PWF": pwf.astype(int),
            "OSF": osf.astype(int),
            "RNF": rnf.astype(int),
            "fail": fail.astype(int),
        }
    )


def load_ai4i(prefer_published: bool = True) -> pd.DataFrame:
    """Load the published synthetic AI4I dataset, or the seeded fallback."""
    rename = {
        "Type": "type",
        "Air temperature [K]": "air_temp",
        "Process temperature [K]": "proc_temp",
        "Rotational speed [rpm]": "speed",
        "Torque [Nm]": "torque",
        "Tool wear [min]": "tool_wear",
        "Machine failure": "fail",
    }
    columns = [
        "type",
        "air_temp",
        "proc_temp",
        "speed",
        "torque",
        "tool_wear",
        "TWF",
        "HDF",
        "PWF",
        "OSF",
        "RNF",
        "fail",
    ]
    if prefer_published:
        for url in AI4I_URLS:
            try:
                df = pd.read_csv(BytesIO(_download(url)), encoding="utf-8-sig")
                df = df.rename(columns=rename)[columns]
                return _with_source(df, "PUBLISHED AI4I dataset (synthetic)")
            except Exception:
                continue
        print("Published AI4I downloads unavailable; using fallback.")
    return _with_source(make_synthetic_ai4i(), "SEEDED AI4I fallback (synthetic)")
