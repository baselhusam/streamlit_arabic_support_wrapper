"""
This package contains the necessary tools to support Arabic Alignment in Streamlit Apps.

Author: @Basel Husam
"""
from . import arabic_supprt as ara

def support_arabic_text(
        components: list = [],
        all: bool = False
    ) -> None:
    """
    This function supports Arabic alignment in Streamlit components.

    Parameters:
    ----------
    components: list
        A list of components to support.
        Supported components: alert, input, markdown, multiselect, selectbox,
        textinput, textarea, expander.
    all: bool
        If True, it will support all components.

    Returns:
    -------
    None
    Instead, it will apply the necessary CSS to support Arabic alignment
    in Streamlit components.

    Example:
    --------
    >>> import streamlit as st
    >>> from arabic_support import support_arabic_text
    >>> support_arabic_text(components=["alert", "input", "markdown"])

    >>> support_arabic_text(all=True)

    >>> support_arabic_text(components=["selectbox", "textinput"])
    """

    if all:
        ara.support_all()
    else:
        for component in components:
            if component == "alert":
                ara.ara_alert()
            elif component == "input":
                ara.ara_input()
            elif component == "markdown":
                ara.ara_markdown()
            elif component == "multiselect":
                ara.ara_multiselect()
            elif component == "selectbox":
                ara.ara_selectbox()
            elif component == "textinput":
                ara.ara_textinput()
            elif component == "textarea":
                ara.ara_textarea()
            elif component == "expander":
                ara.ara_expander()
            else:
                raise ValueError(f"""
Unsupported component: {component} \nSupported components: alert, input, markdown,
multiselect, selectbox, textinput \nYou can also use support_all() to support all components.
\nCheck the documentation for more information.""")
