"""
This Module provides functions to support Arabic alignment in Streamlit components.
It supports different Streamlit components such as text inputs, select boxes, alerts, and more.

Created on: May 2 2024
Author: Basel Husam
"""
import streamlit as st

def ara_template(html_component: str) -> None:
    """
    This function creates a CSS template for Arabic alignment.

    Parameters:
    ----------
    html_component: str
        The HTML component to apply the CSS template to.

    Returns:
    -------
    None
    Instead, it will apply the necessary CSS to support Arabic alignment
    in the specified HTML component.
    """
    html_pattern = f"""
<style>
{html_component} {{
    direction: rtl;
    unicode-bidi: bidi-override;
    text-align: right;
}}
</style>
"""
    st.html(html_pattern)

def ara_markdown():
    ara_template(".stMarkdownContainer")
    ara_template(".stMarkdown")
    ara_template(".stHeadingWithActionElements")


def ara_selectbox():
    ara_template(".stSelectbox")
    ara_template(".stTooltipHoverTarget")


def ara_textinput():
    ara_template(".stTextInput")


def ara_multiselect():
    ara_template(".stMultiSelect")


def ara_input():
    ara_template("input")
    ara_template("label")


def ara_alert():
    ara_template(".stAlert")


def ara_textarea():
    ara_template(".stTextArea")


def ara_expander():
    ara_template(".stMarkdownContainer")
    ara_template("stExpander")



def support_all() -> None:
    """
    This function supports Arabic alignment in all Streamlit components.

    Parameters:
    ----------
    None

    Returns:
    -------
    None
    Instead, it will apply the necessary CSS to support Arabic alignment
    in all Streamlit components.
    """
    ara_markdown()
    ara_selectbox()
    ara_textinput()
    ara_multiselect()
    ara_input()
    ara_alert()
    ara_textarea()
    ara_expander()
