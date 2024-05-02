import streamlit as st
from arabic_support import support_arabic_text

support_arabic_text(all=True)

# ------------- APP -------------
st.title("تجربة دعم اللغة العربية")
st.write()
st.write("هذا التطبيق يوضح كيفية دعم اللغة العربية في Streamlit, يمكنك تجربة النصوص والمدخلات والمسجات وغيرها من العناصر, يمكنك العثور على الكود الخاص بالتطبيق في الجزء السفلي من الصفحة.")
st.write("حمل الباكج من الأمر التالي:")
st.code("""
pip install streamlit-arabic-support-wrapper
""", language="bash")
st.divider()

# ------------- SUPPORTED COMPONENTS -------------
st.subheader("العناصر المدعومة")
st.markdown("""
- النصوص - ***st.write, st.markdown***
- المدخلات - ***st.text_input, st.text_area, st.selectbox, st.multiselect***
- مسجات الحالة - ***st.warning, st.success, st.error***
""")
st.code("""
import streamlit as st
from arabic_support import support_arabic_text
        
support_arabic_text(components=["alert", "input", "markdown", "multiselect", "selectbox", "textinput", "textarea"])
""", language="python")


# ------------- SUPPORT ALL -------------
st.write("يمكنك استخدام الباراميتر **`all=True`** لدعم جميع العناصر المدعومة في Streamlit.")
st.code("""
import streamlit as st
from arabic_support import support_arabic_text
        
support_arabic_text(all=True)
""", language="python")


# ------------- TEXT -------------
st.divider()
st.subheader("النصوص")
st.write("هذا النص مكتوب باللغة العربية - ***st.write***")
st.markdown("هذا النص مكتوب باللغة العربية - ***st.markdown***")
st.code("""
import streamlit as st
from arabic_support import support_arabic_text
        
support_arabic_text(components=["markdown"])
st.markdown("هذا النص مكتوب باللغة العربية")
st.write("هذا النص مكتوب باللغة العربية")
    """, language="python")


# ------------- INPUTS -------------
st.divider()
st.subheader("المدخلات")
st.text_input("أدخل نصًا - ***st.text_input***", value="أدخل نصًا هنا")
st.text_area("أدخل نصًا - ***st.text_area***", placeholder="أدخل نصًا هنا")
st.selectbox("اختر - ***st.selectbox***", ["الخيار 1", "الخيار 2"], index=None, placeholder="اختر احد الخيارات التالية")
st.multiselect("اختر - ***st.multiselect***", ["الخيار 1", "الخيار 2"], placeholder="اختر واحد او اكثر من الخيارات التالية")
st.code("""
import streamlit as st
from arabic_support import support_arabic_text
        
support_arabic_text(components=["input", "selectbox", "multiselect", "textarea"])
st.text_input("أدخل نصًا")
st.text_area("أدخل نصًا")
st.selectbox("اختر", ["الخيار 1", "الخيار 2"])
st.multiselect("اختر", ["الخيار 1", "الخيار 2"])
    """, language="python")


# ------------- ALERTS -------------
st.divider()
st.subheader("مسجات الحالة : تحذير - نجاح - خطأ")
col1, col2, col3 = st.columns(3, gap="small")
col1.warning("تحذير - هذا النص مكتوب بالعربية")
col2.success("نجاح - هذا النص مكتوب بالعربية")
col3.error("خطأ - هذا النص مكتوب بالعربية")
st.code("""
import streamlit as st
from arabic_support import support_arabic_text
            
support_arabic_text(components=["alert"])
st.warning("تحذير - هذا النص مكتوب بالعربية")
st.success("نجاح - هذا النص مكتوب بالعربية")
st.error("خطأ - هذا النص مكتوب بالعربية")
    """, language="python")
