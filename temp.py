# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import panel as pn
import numpy as np
import holoviews as hv

pn.extension(sizing_mode = 'stretch_width')

ACCENT_COLOR = pn.template.FastGridTemplate.accent_base_color
XS = np.linspace(0, np.pi)

def sine(freq, phase):
    return hv.Curve((XS, np.sin(XS * freq + phase))).opts(
        responsive=True, min_height=400, title="Sine", color=ACCENT_COLOR
    ).opts(line_width=6)

def cosine(freq, phase):
    return hv.Curve((XS, np.cos(XS * freq + phase))).opts(
        responsive=True, min_height=400, title="Cosine", color=ACCENT_COLOR
    ).opts(line_width=6)

freq = pn.widgets.FloatSlider(name="Frequency", start=0, end=10, value=2)
phase = pn.widgets.FloatSlider(name="Phase", start=0, end=np.pi)

sine = pn.bind(sine, freq=freq, phase=phase)
cosine = pn.bind(cosine, freq=freq, phase=phase)

template = pn.template.FastGridTemplate(
    site="Panel", title="FastGridTemplate",
    sidebar=[pn.pane.Markdown("## Settings"), freq, phase],
)

template.main[:3, :6] = pn.pane.HoloViews(hv.DynamicMap(sine), sizing_mode="stretch_both")
template.main[:3, 6:] = pn.pane.HoloViews(hv.DynamicMap(cosine), sizing_mode="stretch_both")
template.servable()