import pandas as pd


def get_data_excel() -> pd.DataFrame:
    """
    Obtem os dados.
    ATENÇÃO: O caminho dos arquivos devem ser alterados de uma máquina para outra.

    Returns
    -------
    pd.DataFrame
        DataFrame com os dados.
    """
    return pd.concat(
        [
            pd.read_excel(
                "D:/workspace_python/holoviz_get_start/data/GERACAO_USINA_2019.xlsx"
            ),
            pd.read_excel(
                "D:/workspace_python/holoviz_get_start/data/GERACAO_USINA_2020.xlsx"
            ),
            pd.read_excel(
                "D:/workspace_python/holoviz_get_start/data/GERACAO_USINA_2021.xlsx"
            ),
        ]
    )


def get_data_parquet() -> pd.DataFrame:
    """
    Obtem os dados.
    ATENÇÃO: O caminho dos arquivos devem ser alterados de uma máquina para outra.

    Returns
    -------
    pd.DataFrame
        DataFrame com os dados.
    """
    return pd.read_parquet(
        "D:/workspace_python/exemplo_holoviz/data/GERACAO_USINA_2019_2020_2021.parquet"
    ).sort_values("din_instante")
