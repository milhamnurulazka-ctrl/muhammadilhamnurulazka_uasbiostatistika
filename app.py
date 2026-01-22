import streamlit as st

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Diabetes Analytics Dashboard",
    page_icon="🩺",
    layout="wide"
)

# =========================
# STYLE GLOBAL (PREMIUM)
# =========================
st.markdown("""
<style>
body {
    background-color: #f5f7fa;
}
.section {
    background: white;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0px 6px 25px rgba(0,0,0,0.08);
    margin-bottom: 30px;
}
.metric-card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.08);
    text-align: center;
}
.title {
    font-size: 26px;
    font-weight: 700;
}
.subtitle {
    color: #6b7280;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("<div class='title'>🩺 Diabetes Risk Analysis Dashboard</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>UAS Machine Learning – Universitas Muhammadiyah Semarang</div>", unsafe_allow_html=True)

# =========================
# TABS
# =========================
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📘 About Dataset",
    "📊 Dashboard",
    "🧩 Clustering",
    "🤖 Machine Learning",
    "🔮 Prediction",
    "📩 Contact"
])

# =========================
# TAB 1 - ABOUT
# =========================
with tab1:
    try:
        import about
        about.about_dataset()
    except Exception as e:
        st.error("Halaman About Dataset belum siap atau terjadi error.")
        st.code(e)

# =========================
# TAB 2 - DASHBOARD
# =========================
with tab2:
    try:
        import visualisasi
        if hasattr(visualisasi, "chart"):
            visualisasi.chart()
        else:
            st.warning("Fungsi chart() tidak ditemukan di visualisasi.py")
    except Exception as e:
        st.error("Halaman Dashboard belum siap.")
        st.code(e)

# =========================
# TAB 3 - CLUSTERING
# =========================
with tab3:
    try:
        import clustering
        if hasattr(clustering, "clustering_app"):
            clustering.clustering_app()
        else:
            st.warning("Fungsi clustering_app() tidak ditemukan di clustering.py")
    except Exception as e:
        st.error("Halaman Clustering belum siap.")
        st.code(e)

# =========================
# TAB 4 - MACHINE LEARNING
# =========================
with tab4:
    try:
        import machine_learning
        if hasattr(machine_learning, "ml_model"):
            machine_learning.ml_model()
        else:
            st.warning("Fungsi ml_model() tidak ditemukan di machine_learning.py")
    except Exception as e:
        st.error("Halaman Machine Learning belum siap.")
        st.code(e)

# =========================
# TAB 5 - PREDICTION
# =========================
with tab5:
    try:
        import prediction
        if hasattr(prediction, "prediction_app"):
            prediction.prediction_app()
        else:
            st.warning("Fungsi prediction_app() tidak ditemukan di prediction.py")
    except Exception as e:
        st.error("Halaman Prediction belum siap.")
        st.code(e)

# =========================
# TAB 6 - CONTACT
# =========================
with tab6:
    try:
        import kontak
        if hasattr(kontak, "contact_me"):
            kontak.contact_me()
        else:
            st.warning("Fungsi contact_me() tidak ditemukan di kontak.py")
    except Exception as e:
        st.error("Halaman Contact belum siap.")
        st.code(e)
