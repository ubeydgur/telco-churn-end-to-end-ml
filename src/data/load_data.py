"""Veri yükleme modülü.

Ham ve işlenmiş verileri yüklemek için fonksiyonlar içerir.
"""

import pandas as pd
import yaml


def load_config(config_path: str = "configs/config.yaml") -> dict:
    """Konfigürasyon dosyasını yükler.

    Args:
        config_path: config.yaml dosyasının yolu.

    Returns:
        Konfigürasyon değerlerini içeren sözlük.
    """
    with open(config_path) as f:
        config = yaml.safe_load(f)
    return config


def load_raw_data(config_path: str = "configs/config.yaml") -> pd.DataFrame:
    """Ham veriyi yükler ve temel tip dönüşümlerini yapar.

    Args:
        config_path: config.yaml dosyasının yolu.

    Returns:
        Ham veriyi içeren DataFrame.
    """
    config = load_config(config_path)
    raw_path = config["data"]["raw_path"]

    df = pd.read_csv(raw_path)

    # TotalCharges sütunu string olarak geliyor, sayıya çeviriyoruz
    # Boşluk olan değerler NaN olacak
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    return df
