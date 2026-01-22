import streamlit as st
import pandas as pd
import joblib

def prediction_app():

    # =========================
    # PAGE CONFIG (AMAN DI DALAM FUNGSI)
    # =========================
    st.markdown("""
    <style>
    .main { background-color: #f8fafc; }

    .hero-box {
        background: linear-gradient(135deg, #1e3a8a, #2563eb);
        padding: 35px 40px;
        border-radius: 22px;
        margin-bottom: 35px;
        box-shadow: 0 15px 40px rgba(37, 99, 235, 0.35);
    }

    .hero-title {
        font-size: 32px;
        font-weight: 800;
        color: white;
    }

    .hero-subtitle {
        font-size: 15px;
        color: #e0f2fe;
        line-height: 1.6;
    }

    .card {
        background-color: white;
        padding: 28px;
        border-radius: 18px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.08);
        margin-bottom: 25px;
    }

    .section-title {
        font-size: 22px;
        font-weight: 700;
        color: #1e3a8a;
        margin-bottom: 12px;
    }

    .desc {
        font-size: 14px;
        color: #475569;
        line-height: 1.7;
    }

    .result-box {
        padding: 25px;
        border-radius: 18px;
        text-align: center;
        margin-top: 20px;
    }

    .high-risk {
        background-color: #fee2e2;
        color: #991b1b;
    }

    .low-risk {
        background-color: #dcfce7;
        color: #166534;
    }
    </style>
    """, unsafe_allow_html=True)

    # =========================
    # LOAD MODEL
    # =========================
    model = joblib.load("model_diabetes.pkl")
    scaler = joblib.load("scaler.pkl")

    # =========================
    # HERO HEADER
    # =========================
    st.markdown("""
    <div class="hero-box">
        <div class="hero-title">🔮 Prediksi Risiko Diabetes</div>
        <div class="hero-subtitle">
            Sistem prediksi berbasis <b>Machine Learning</b>
            untuk membantu deteksi dini Diabetes Mellitus
            berdasarkan data klinis pasien.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # PENJELASAN
    # =========================
    st.markdown("""
    <div class="card">
        <div class="section-title">📘 Penjelasan</div>
        <p class="desc">
        Halaman ini menggunakan model Machine Learning
        untuk menghitung <b>probabilitas risiko diabetes</b>
        berdasarkan karakteristik klinis pasien.
        Hasil prediksi bersifat pendukung keputusan,
        bukan diagnosis medis.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # INPUT DATA
    # =========================
    st.markdown("""
    <div class="card">
        <div class="section-title">📝 Input Data Pasien</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        pregnancies = st.number_input("🤰 Jumlah Kehamilan", 0, 20, 1)
        glucose = st.number_input("🧪 Kadar Glukosa", 0, 200, 120)
        blood_pressure = st.number_input("💉 Tekanan Darah", 0, 150, 70)
        skin = st.number_input("📏 Ketebalan Kulit", 0, 100, 20)

    with col2:
        insulin = st.number_input("💊 Insulin", 0, 900, 80)
        bmi = st.number_input("⚖️ BMI", 0.0, 60.0, 25.0)
        dpf = st.number_input("🧬 Diabetes Pedigree Function", 0.0, 3.0, 0.5)
        age = st.number_input("🎂 Usia", 1, 120, 30)

    # =========================
    # PREDIKSI
    # =========================
    if st.button("🔍 Prediksi Risiko", use_container_width=True):

        data = [[
            pregnancies, glucose, blood_pressure, skin,
            insulin, bmi, dpf, age
        ]]

        df = pd.DataFrame(data, columns=[
            "Pregnancies", "Glucose", "BloodPressure",
            "SkinThickness", "Insulin", "BMI",
            "DiabetesPedigreeFunction", "Age"
        ])

        df_scaled = scaler.transform(df)
        prob = model.predict_proba(df_scaled)[0][1]

        st.markdown("""
        <div class="card">
            <div class="section-title">📊 Hasil Prediksi</div>
        </div>
        """, unsafe_allow_html=True)

        if prob >= 0.5:
            st.markdown(f"""
            <div class="result-box high-risk">
                <h2>⚠️ Risiko Tinggi Diabetes</h2>
                <h3>{prob*100:.2f}%</h3>
                <p>Disarankan pemeriksaan medis lanjutan.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="result-box low-risk">
                <h2>✅ Risiko Rendah Diabetes</h2>
                <h3>{prob*100:.2f}%</h3>
                <p>Tetap jaga pola hidup sehat.</p>
            </div>
            """, unsafe_allow_html=True)

    # =========================
    # CATATAN
    # =========================
    st.markdown("""
    <div class="card">
        <div class="section-title">ℹ️ Catatan</div>
        <p class="desc">
        Model ini dibuat dari data historis dan
        memiliki keterbatasan.
        Tidak menggantikan diagnosis dokter.
        </p>
    </div>
    """, unsafe_allow_html=True)
