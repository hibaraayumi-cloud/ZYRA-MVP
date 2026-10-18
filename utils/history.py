import pandas as pd
from datetime import datetime

FILE_PATH = "data/analysis_history.csv"

def save_analysis(
    business_type,
    score
):

    try:

        df = pd.read_csv(FILE_PATH)

    except:

        df = pd.DataFrame(
            columns=[
                "date",
                "business_type",
                "score"
            ]
        )

    new_row = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "business_type": business_type,
        "score": score
    }

    df.loc[len(df)] = new_row

    df.to_csv(
        FILE_PATH,
        index=False
    )


def load_history():

    try:

        return pd.read_csv(FILE_PATH)

    except:

        return pd.DataFrame()
