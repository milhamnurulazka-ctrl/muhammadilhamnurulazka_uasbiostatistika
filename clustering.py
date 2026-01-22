import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
def clustering_app():
    # =========================
    # PAGE CONFIG
    # =========================
    st.set_page_config(page_title="Clustering Analysis", layout="wide")
    
    # =========================
    # GLOBAL STYLE (SAMA DENGAN EDA)
    # =========================
    st.markdown("""
    <style>
    .main {
        background-color: #f8fafc;
    }
    
    /* HERO HEADER */
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
        color: #ffffff;
        margin-bottom: 8px;
    }
    
    .hero-subtitle {
        font-size: 15px;
        color: #e0f2fe;
        line-height: 1.6;
    }
    
    /* CARD */
    .card {
        background-color: #ffffff;
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
    
    .highlight {
        color: #2563eb;
        font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # =========================
    # HERO HEADER
    # =========================
    st.markdown("""
    <div class="hero-box">
        <div class="hero-title">🧩 Clustering Analysis (K-Means)</div>
        <div class="hero-subtitle">
            Analisis pengelompokan pasien diabetes untuk memahami pola klinis
            dan segmentasi karakteristik pasien berdasarkan kemiripan data.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # =========================
    # LOAD DATA
    # =========================
    df = pd.read_csv("diabetes.csv")
    
    # =========================
    # PENJELASAN UMUM
    # =========================
    st.markdown("""
    <div class="card">
        <div class="section-title">📌 Tujuan Analisis Clustering</div>
        <p>
        Clustering merupakan metode <span class="highlight">unsupervised learning</span>
        yang bertujuan untuk mengelompokkan pasien berdasarkan kemiripan karakteristik klinis
        tanpa menggunakan label diagnosis.
        </p>
        <p>
        Pada konteks kesehatan, clustering berguna untuk:
        <ul>
            <li>Mengidentifikasi kelompok pasien dengan profil risiko yang serupa</li>
            <li>Mendukung segmentasi pasien dalam layanan medis</li>
            <li>Memberikan gambaran awal sebelum analisis inferensial</li>
        </ul>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # =========================
    # FITUR CLUSTERING
    # =========================
    features = ["Glucose", "BMI", "Age", "Insulin"]
    X = df[features]
    
    st.markdown("""
    <div class="card">
        <div class="section-title">🧬 Variabel yang Digunakan</div>
        <ul>
            <li><b>Glucose</b> → indikator utama kadar gula darah</li>
            <li><b>BMI</b> → mencerminkan status berat badan</li>
            <li><b>Age</b> → faktor risiko yang tidak dapat dimodifikasi</li>
            <li><b>Insulin</b> → berhubungan dengan regulasi gula darah</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # =========================
    # STANDARDISASI
    # =========================
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    st.markdown("""
    <div class="card">
        <div class="section-title">⚙️ Standarisasi Data</div>
        <p>
        Seluruh variabel distandarisasi menggunakan <b>StandardScaler</b>
        agar berada pada skala yang sama, sehingga tidak ada variabel
        yang mendominasi pembentukan cluster.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # =========================
    # ELBOW METHOD
    # =========================
    inertia = []
    K_range = range(2, 7)
    
    for k in K_range:
        km = KMeans(n_clusters=k, random_state=42, n_init=10)
        km.fit(X_scaled)
        inertia.append(km.inertia_)
    
    fig_elbow = px.line(
        x=list(K_range),
        y=inertia,
        markers=True,
        template="plotly_white",
        color_discrete_sequence=["#2563eb"],
        labels={"x": "Jumlah Cluster (k)", "y": "Inertia"},
        title="Elbow Method – Penentuan Jumlah Cluster Optimal"
    )
    
    st.plotly_chart(fig_elbow, use_container_width=True)
    
    # =========================
    # PILIH JUMLAH CLUSTER
    # =========================
    k = st.slider("🔢 Pilih Jumlah Cluster", 2, 5, 3)
    
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    df["Cluster"] = model.fit_predict(X_scaled)
    
    st.success(f"Model berhasil membagi data menjadi **{k} cluster**")
    
    # =========================
    # VISUALISASI CLUSTER
    # =========================
    fig_cluster = px.scatter(
        df,
        x="Glucose",
        y="BMI",
        color="Cluster",
        size="Age",
        template="plotly_white",
        color_discrete_sequence=[
            "#1e3a8a",
            "#2563eb",
            "#38bdf8",
            "#0ea5e9"
        ],
        labels={
            "Glucose": "Kadar Glukosa",
            "BMI": "Body Mass Index",
            "Cluster": "Cluster Pasien"
        },
        title="Visualisasi Segmentasi Pasien Diabetes"
    )
    
    st.plotly_chart(fig_cluster, use_container_width=True)
    
    # =========================
    # RINGKASAN CLUSTER
    # =========================
    cluster_summary = df.groupby("Cluster")[features].mean().round(2)
    
    st.markdown("""
    <div class="card">
        <div class="section-title">📊 Rata-rata Karakteristik Setiap Cluster</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.dataframe(cluster_summary, use_container_width=True)
    
    # =========================
    # INTERPRETASI
    # =========================
    st.markdown("""
    <div class="card">
        <div class="section-title">🧠 Interpretasi Umum</div>
        <p>
        <b>Cluster Risiko Rendah</b>: Glukosa dan BMI relatif normal.<br>
        <b>Cluster Risiko Sedang</b>: Glukosa meningkat dengan BMI sedang.<br>
        <b>Cluster Risiko Tinggi</b>: Glukosa dan BMI tinggi, berpotensi diabetes.
        </p>
        <p style="color:#dc2626;">
        ⚠️ Clustering bukan alat diagnosis medis, hanya untuk analisis pola data.
        </p>
    </div>
    """, unsafe_allow_html=True)
