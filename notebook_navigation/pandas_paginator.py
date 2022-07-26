from IPython.display import display, clear_output
from ipywidgets import widgets
import math


class Paginator:
    def __init__(self, df, pagesize=10, start_page=0):
        self.df = df
        self.pagesize = pagesize
        self.page = start_page
        self.max_pages = math.ceil(df.shape[0] / self.pagesize)
        self.btn_next = widgets.Button(description="Next")
        self.btn_next.on_click(self.next_page)
        self.btn_prev = widgets.Button(description="Prev")
        self.btn_prev.on_click(self.prev_page)
        self.select_page = widgets.IntSlider(
            value=1,
            min=1,
            max=self.max_pages,
            step=1,
            description="Page number:",
            disabled=False,
            continuous_update=False,
            orientation="horizontal",
            readout=True,
            readout_format="d",
        )

        self.select_page.observe(self.slide_page, names="value")
        self.output = widgets.Output()

    def get_page(self):
        return self.df.iloc[self.page * self.pagesize : (self.page + 1) * self.pagesize]

    def show(self):
        with self.output:
            clear_output()
            self.control = widgets.HBox(
                (
                    self.btn_prev,
                    widgets.Label("PAGE {}/{}".format(self.page + 1, self.max_pages)),
                    self.btn_next,
                    self.select_page,
                )
            )

            display(self.control)
            display(self.get_page())
            display(self.control)

        display(self.output)

    def next_page(self, b):
        self.page = min(self.max_pages - 1, self.page + 1)
        self.show()

    def prev_page(self, b):
        self.page = max(0, self.page - 1)
        self.show()

    def slide_page(self, change_dict):
        self.page = change_dict["new"] - 1
        self.show()
