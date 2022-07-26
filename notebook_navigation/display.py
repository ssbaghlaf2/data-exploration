from IPython.display import display, HTML
import pandas as pd


def html_display(statement):
    return display(
        HTML(
            f"""
        <div dir='rtl'>
        {statement}
        </div>
        """
        )
    )


def display_df(df, max_rows=None, max_cols=None, cols=None, colwidth=-1):
    if isinstance(df, pd.DataFrame):
        if cols is None:
            cols = df.columns

        with pd.option_context(
            "display.max_rows",
            max_rows,
            "display.max_columns",
            max_cols,
            "display.max_colwidth",
            colwidth,
        ):
            display(df[cols])
    else:
        with pd.option_context(
            "display.max_rows",
            max_rows,
            "display.max_columns",
            max_cols,
            "display.max_colwidth",
            colwidth,
        ):
            display(df)
