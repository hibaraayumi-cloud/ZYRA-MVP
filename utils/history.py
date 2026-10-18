import pandas as pd
from datetime import datetime

CSV_FILE = "data/analysis_history.csv"


def save_analysis(
    business_type,
    revenue,
    cost,
    cash,
    growth,
    score
):

    try:

        df = pd.read_csv(CSV_FILE)

    except:

        df = pd.DataFrame(
            columns=[
                "date",
                "business_type",
                "revenue",
                "cost",
                "cash",
                "growth",
                "score"
            ]
        )

    new_row = {
        "date":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M"
            ),

        "business_type":
            business_type,

        "revenue":
            revenue,

        "cost":
            cost,

        "cash":
            cash,

        "growth":
            growth,

        "score":
            score
    }

    df.loc[len(df)] = new_row

    df.to_csv(
        CSV_FILE,
        index=False
    )


def load_history():

    try:

        return pd.read_csv(
            CSV_FILE
        )

    except:

        return pd.DataFrame()
