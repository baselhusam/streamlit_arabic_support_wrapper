import streamlit as st

def ara_markdown():
    st.html("""<style>
.stMarkdown {
    direction: rtl;
    text-align: right;
}
</style>""", )
    
def ara_selectbox():
    st.html("""
<style>
.stSelectbox {
    direction: RTL;
    unicode-bidi: bidi-override;
    text-align: right;
}
</style>
""", )
    
    st.html("""
<style>
.stTooltipHoverTarget {
    direction: RTL;
    unicode-bidi: bidi-override;
    text-align: right;
}
</style>
""", )
    

    
def ara_textinput():
    st.html("""
<style>
.stTextInput {
    direction: RTL;
    unicode-bidi: bidi-override;
    text-align: right;
}
</style>
""", )
    
def ara_multiselect():
    st.html("""
<style>
.stMultiSelect {
    direction: RTL;
    unicode-bidi: bidi-override;
    text-align: right;
}
</style>
""", )
    
def ara_input():
    st.html("""
<style>
input, label, {
    direction: RTL;
    unicode-bidi: bidi-override;
    text-align: right;
}
</style>
""", )
    
def ara_alert():
    st.html("""
<style>
.stAlert {
    direction: RTL;
    unicode-bidi: bidi-override;
    text-align: right;
}
</style>
""", )
    
def ara_textarea():
    st.html("""
<style>
.stTextArea {
    direction: RTL;
    unicode-bidi: bidi-override;
    text-align: right;
}
</style>
""", )
    
def ara_expander():
    st.html("""
<style>
.stMarkdownContainer, stExpander {
    direction: RTL;
    unicode-bidi: bidi-override;
    text-align: right;
}
</style>
""", )


def support_all():
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
