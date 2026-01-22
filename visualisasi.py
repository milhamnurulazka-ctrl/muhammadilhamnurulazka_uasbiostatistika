import streamlit as st
import pandas as pd
import plotly.express as px

def chart():

    # ==============================
    # STYLE (SAMA DENGAN ABOUT)
    # ==============================
    st.markdown("""
    <style>
    .hero {
        background: linear-gradient(90deg,#1e3a8a,#2563eb);
        padding: 26px;
        border-radius: 16px;
        color: white;
        margin-bottom: 24px;
    }
    .card {
        background-color: #ffffff;
        padding: 26px;
        border-radius: 16px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.06);
        margin-bottom: 22px;
    }
    .title {
        font-size: 24px;
        font-weight: 800;
        margin-bottom: 12px;
        color: #111827;
    }
    .subtitle {
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 6px;
        color: #1f2937;
    }
    .highlight {
        background-color: #eff6ff;
        padding: 16px;
        border-left: 6px solid #2563eb;
        border-radius: 10px;
        margin-top: 16px;
        margin-bottom: 16px;
    }
    </style>
    """, unsafe_allow_html=True)

    # ==============================
    # LOAD DATA
    # ==============================
    df = pd.read_csv("diabetes.csv")

    # ==============================
    # HERO
    # ==============================
    st.markdown("""
    <div class="hero">
        <h2>📊 Exploratory Data Analysis (EDA)</h2>
        <p style="margin:0;">
        Analisis visual untuk memahami pola data klinis
        dan perbedaan karakteristik pasien diabetes
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ==============================
    # PENJELASAN AWAL
    # ==============================
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="title">🔎 Tujuan Exploratory Data Analysis</div>', unsafe_allow_html=True)

    st.markdown("""
    Exploratory Data Analysis (EDA) merupakan tahap awal yang sangat penting
    dalam analisis data kesehatan. Tujuan utama EDA adalah untuk
    **memahami karakteristik data secara visual**, menemukan pola,
    serta mengidentifikasi perbedaan antar kelompok pasien.

    Dalam konteks diabetes, EDA membantu menjawab pertanyaan dasar seperti:
    - Variabel apa yang paling membedakan pasien diabetes dan non-diabetes?
    - Bagaimana distribusi usia, BMI, dan glukosa dalam populasi?
    - Apakah terdapat indikasi awal faktor risiko yang dominan?
    """)

    st.markdown('<div class="highlight">💡 Semua visualisasi membandingkan dua kelompok: <b>Outcome = 0 (Tidak Diabetes)</b> dan <b>Outcome = 1 (Diabetes)</b>.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # ==============================
    # METRIK
    # ==============================
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="title">📌 Ringkasan Statistik Populasi</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    col1.metric("👥 Total Pasien", df.shape[0])
    col2.metric("🩺 Pasien Diabetes", int(df["Outcome"].sum()))
    col3.metric("📈 Prevalensi Diabetes", f"{df['Outcome'].mean()*100:.2f}%")

    st.markdown("""
    **Interpretasi:**  
    Sekitar **seperempat populasi** dalam dataset ini
    terdiagnosis diabetes. Angka ini menunjukkan bahwa
    diabetes merupakan masalah kesehatan yang cukup dominan
    pada kelompok pasien yang diteliti.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # ==============================
    # GLUCOSE
    # ==============================
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">🧪 Distribusi Kadar Glukosa</div>', unsafe_allow_html=True)

    fig_glucose = px.box(
        df,
        x="Outcome",
        y="Glucose",
        color="Outcome",
        labels={
            "Outcome": "Status Diabetes (0 = Tidak, 1 = Diabetes)",
            "Glucose": "Kadar Glukosa Plasma"
        }
    )

    st.plotly_chart(fig_glucose, use_container_width=True)

    st.markdown("""
    **Interpretasi:**  
    Terlihat perbedaan yang sangat jelas antara kedua kelompok.
    Pasien diabetes memiliki kadar glukosa yang secara konsisten
    lebih tinggi dibandingkan pasien non-diabetes.

    Visualisasi ini memperkuat peran **glukosa sebagai indikator utama**
    dalam diagnosis dan prediksi diabetes.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # ==============================
    # BMI
    # ==============================
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">⚖️ Distribusi Body Mass Index (BMI)</div>', unsafe_allow_html=True)

    fig_bmi = px.box(
        df,
        x="Outcome",
        y="BMI",
        color="Outcome",
        labels={
            "Outcome": "Status Diabetes",
            "BMI": "Body Mass Index (BMI)"
        }
    )

    st.plotly_chart(fig_bmi, use_container_width=True)

    st.markdown("""
    **Interpretasi:**  
    Pasien diabetes cenderung memiliki BMI lebih tinggi.
    Kelebihan berat badan meningkatkan resistensi insulin,
    sehingga tubuh kesulitan mengontrol kadar gula darah.

    Hal ini menjadikan BMI sebagai **faktor risiko penting**
    yang perlu diperhatikan dalam pencegahan diabetes.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # ==============================
    # AGE
    # ==============================
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">🎂 Distribusi Usia Pasien</div>', unsafe_allow_html=True)

    fig_age = px.histogram(
        df,
        x="Age",
        color="Outcome",
        barmode="overlay",
        labels={
            "Age": "Usia (Tahun)",
            "Outcome": "Status Diabetes"
        }
    )

    st.plotly_chart(fig_age, use_container_width=True)

    st.markdown("""
    **Interpretasi:**  
    Prevalensi diabetes meningkat pada kelompok usia yang lebih tua.
    Faktor usia berhubungan dengan penurunan fungsi metabolisme
    dan sensitivitas insulin.

    Usia merupakan faktor risiko **yang tidak dapat dimodifikasi**,
    sehingga penting dalam strategi skrining dan pencegahan dini.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # ==============================
    # KESIMPULAN
    # ==============================
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="title">🧾 Kesimpulan EDA</div>', unsafe_allow_html=True)

    st.markdown("""
    Berdasarkan hasil EDA dapat disimpulkan bahwa:
    - Pasien diabetes memiliki **kadar glukosa yang lebih tinggi**
    - **BMI tinggi** berkorelasi dengan peningkatan risiko diabetes
    - **Usia lanjut** menunjukkan prevalensi diabetes yang lebih besar

    Temuan ini menjadi dasar yang kuat untuk
    **analisis lanjutan menggunakan regresi logistik**
    serta **pengelompokan pasien dengan K-Means Clustering**.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
