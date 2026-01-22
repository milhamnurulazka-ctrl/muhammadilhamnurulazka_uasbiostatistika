import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, confusion_matrix, roc_curve, auc
)

import statsmodels.api as sm

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Machine Learning Analysis",
    page_icon="🤖",
    layout="wide"
)

# =========================
# GLOBAL STYLE (SAMA DENGAN CLUSTERING)
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
    <div class="hero-title">🤖 Machine Learning untuk Prediksi Risiko Diabetes</div>
    <div class="hero-subtitle">
        Pendekatan supervised learning untuk memprediksi
        kemungkinan Diabetes Mellitus berdasarkan data klinis pasien.
    </div>
</div>
""", unsafe_allow_html=True)

# =========================
# PENDAHULUAN
# =========================
st.markdown("""
<div class="card">
    <div class="section-title">📘 Pendahuluan</div>
    <p>
    <b>Machine Learning (ML)</b> merupakan cabang dari kecerdasan buatan
    yang memungkinkan komputer <span class="highlight">belajar dari data</span>
    tanpa harus diprogram secara eksplisit.
    Dalam bidang kesehatan, ML banyak digunakan untuk
    <b>deteksi dini penyakit, prediksi risiko, dan pengambilan keputusan klinis</b>.
    </p>
    <p>
    Pada penelitian ini, Machine Learning digunakan untuk
    <b>memprediksi risiko Diabetes Mellitus</b> berdasarkan
    data klinis pasien seperti kadar glukosa, BMI, usia, dan riwayat kesehatan lainnya.
    </p>
</div>
""", unsafe_allow_html=True)

# =========================
# KONSEP SUPERVISED LEARNING
# =========================
st.markdown("""
<div class="card">
    <div class="section-title">🧠 Konsep Supervised Learning</div>
    <p>
    Analisis ini menggunakan pendekatan <b>Supervised Learning</b>,
    yaitu metode Machine Learning yang dilatih menggunakan data
    yang sudah memiliki <span class="highlight">label atau target</span>.
    </p>
    <p>
    Pada dataset diabetes:
    <ul>
        <li><b>Fitur (X)</b> → data klinis pasien</li>
        <li><b>Target (y)</b> → status diabetes (0 = tidak, 1 = diabetes)</li>
    </ul>
    Model akan belajar pola hubungan antara fitur dan target
    untuk memprediksi status pasien baru.
    </p>
</div>
""", unsafe_allow_html=True)

# =========================
# LOAD DATA
# =========================
df = pd.read_csv("diabetes.csv")

features = [
    "Pregnancies", "Glucose", "BloodPressure",
    "SkinThickness", "Insulin", "BMI",
    "DiabetesPedigreeFunction", "Age"
]
target = "Outcome"

X = df[features]
y = df[target]

st.dataframe(df.head(), use_container_width=True)

# =========================
# SPLIT & SCALING
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# =========================
# REGRESI LOGISTIK (BIOSTATISTIKA)
# =========================
st.markdown("""
<div class="card">
    <div class="section-title">📊 Regresi Logistik (Pendekatan Statistik)</div>
    <p>
    Regresi logistik digunakan untuk menganalisis
    <span class="highlight">pengaruh masing-masing variabel</span>
    terhadap risiko diabetes.
    Metode ini sangat populer dalam bidang
    <b>biostatistika dan epidemiologi</b>.
    </p>
    <p>
    Output utama regresi logistik adalah:
    <ul>
        <li><b>Koefisien (β)</b></li>
        <li><b>Odds Ratio (OR)</b></li>
        <li><b>p-value</b> untuk signifikansi statistik</li>
    </ul>
    </p>
</div>
""", unsafe_allow_html=True)

X_sm = sm.add_constant(X)
logit_model = sm.Logit(y, X_sm).fit(disp=False)

summary_df = pd.DataFrame({
    "Koefisien (β)": logit_model.params,
    "Odds Ratio": np.exp(logit_model.params),
    "p-value": logit_model.pvalues
}).round(4)

st.dataframe(summary_df, use_container_width=True)

# =========================
# MODEL MACHINE LEARNING
# =========================
st.markdown("""
<div class="card">
    <div class="section-title">🤖 Model Machine Learning yang Digunakan</div>
    <ul>
        <li><b>Logistic Regression</b> → mudah diinterpretasikan secara klinis</li>
        <li><b>Random Forest</b> → menangkap hubungan non-linear</li>
        <li><b>Support Vector Machine (SVM)</b> → akurat untuk data kompleks</li>
    </ul>
</div>
""", unsafe_allow_html=True)

lr = LogisticRegression(max_iter=1000)
rf = RandomForestClassifier(n_estimators=200, random_state=42)
svm = SVC(kernel="rbf", probability=True, random_state=42)

lr.fit(X_train_scaled, y_train)
rf.fit(X_train_scaled, y_train)
svm.fit(X_train_scaled, y_train)

models = {
    "Logistic Regression": lr,
    "Random Forest": rf,
    "SVM": svm
}

# =========================
# EVALUASI MODEL
# =========================
results = []
for name, model in models.items():
    y_pred = model.predict(X_test_scaled)
    results.append({
        "Model": name,
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred),
        "Recall": recall_score(y_test, y_pred),
        "F1-Score": f1_score(y_test, y_pred)
    })

st.markdown("""
<div class="card">
    <div class="section-title">📈 Evaluasi Performa Model</div>
</div>
""", unsafe_allow_html=True)

st.dataframe(pd.DataFrame(results).round(3), use_container_width=True)

# =========================
# ROC CURVE
# =========================
fig_roc = go.Figure()
for name, model in models.items():
    y_prob = model.predict_proba(X_test_scaled)[:, 1]
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    fig_roc.add_trace(go.Scatter(
        x=fpr, y=tpr, mode="lines",
        name=f"{name} (AUC={auc(fpr, tpr):.2f})"
    ))

fig_roc.add_trace(go.Scatter(
    x=[0, 1], y=[0, 1],
    mode="lines", line=dict(dash="dash"),
    showlegend=False
))

fig_roc.update_layout(
    title="ROC Curve – Perbandingan Model",
    template="plotly_white"
)

st.plotly_chart(fig_roc, use_container_width=True)

# =========================
# KESIMPULAN
# =========================
st.markdown("""
<div class="card">
    <div class="section-title">🏁 Kesimpulan</div>
    <p>
    Machine Learning mampu membantu
    <b>prediksi risiko diabetes secara objektif</b>.
    Regresi Logistik unggul dalam interpretasi,
    sedangkan Random Forest dan SVM
    memberikan performa prediksi yang lebih tinggi.
    </p>
</div>
""", unsafe_allow_html=True)
