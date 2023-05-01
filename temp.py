# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import panel_highcharts as ph
import panel as pn




ph.config.theme("auto")
pn.extension('highchart')

widget = pn.widgets.TextInput(name='A widget', value='A string')

configuration = {
    "title": {"text": "HighChart Pane"},
    "series": [
        {
            "name": "series1",
            "data": [1, 2, 3, 4, 5],
        }
    ]
}
chart = ph.HighChart(object=configuration, sizing_mode="stretch_width")


template = pn.template.FastGridTemplate(
    site="Panel", title="FastGridTemplate",
    sidebar=[pn.pane.Markdown("## Settings")],
)




template = pn.template.FastGridTemplate(
   theme="dark",
                                       site="", title="Interactive stop and search tracker",
                                        sidebar=[
                                           pn.Spacer(height=15), widget, pn.Spacer(height=15)],
                                        sidebar_width=410, header_background='#130C16',
                                        header_neutral_color='#D9D9D9', accent_base_color='#D9D9D9', corner_radius=6, shadow=True,
                                        # , cols = {'lg': 18, 'md': 12, 'sm': 8, 'xs': 6, 'xxs': 4}
                                        prevent_collision=True, theme_toggle=False
                                        )

template.main[:2, :7] = pn.Column(chart, sizing_mode="stretch_both")
template.main[:2, 7:12] = pn.Column(chart, sizing_mode="stretch_both")
template.servable()
