import streamlit as st

def about_dataset():

    # ==============================
    # STYLE
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
        margin-top: 18px;
        margin-bottom: 8px;
        color: #1f2937;
    }
    .text-muted {
        color: #6b7280;
        font-size: 14px;
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
    # HERO
    # ==============================
    st.markdown("""
    <div class="hero">
        <h2>🩺 Analisis Diabetes Berbasis Data & Machine Learning</h2>
        <p style="margin:0;">
        Studi Kasus: Pima Indians Diabetes Database ·
        <a href="https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database" 
           target="_blank" style="color:#bfdbfe;">
           Kaggle Dataset
        </a>
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ==============================
    # DATASET
    # ==============================
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="title">📊 Penjelasan Dataset</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(
            "https://media.istockphoto.com/id/905659224/id/vektor/diabetes-konsep-kesehatan-gula-darah-tinggi-glukometer-glukosa-meter-kartun-vektor-ilustrasi.jpg?s=1024x1024&w=is&k=20&c=-INyZ2G_hgv7zsfgmr7IPkRTf3vkwRO4mKJVxgofldU=",
            use_column_width=True
        )

    with col2:
        st.markdown("""
        Dataset **Pima Indians Diabetes Database** merupakan kumpulan data medis
        yang berisi hasil pemeriksaan kesehatan **pasien wanita dewasa**
        dari suku Pima Indian di Amerika Serikat.

        Dataset ini sangat populer dalam dunia **biostatistika, epidemiologi,
        dan machine learning kesehatan** karena memiliki karakteristik data
        yang realistis, variabel klinis penting, serta struktur yang cocok
        untuk analisis prediktif.

        Setiap baris data merepresentasikan **satu individu pasien**,
        sementara setiap kolom menggambarkan **indikator medis kuantitatif**
        seperti kadar glukosa, tekanan darah, indeks massa tubuh (BMI),
        kadar insulin, hingga faktor genetik.

        Data ini bersifat **observasional**, artinya dikumpulkan dari
        pemeriksaan kesehatan tanpa intervensi eksperimental.
        Oleh karena itu, dataset ini ideal untuk:
        - analisis faktor risiko penyakit  
        - pemodelan prediksi klinis  
        - edukasi statistik kesehatan  
        """)

    st.markdown('<div class="highlight">📌 Dataset ini sering digunakan sebagai <b>benchmark</b> dalam penelitian prediksi diabetes.</div>', unsafe_allow_html=True)

    st.markdown("""
    🔗 **Referensi Dataset & Studi:**
    - https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database  
    - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5078596/  
    - https://archive.ics.uci.edu/ml/datasets/diabetes
    """)

    st.markdown('</div>', unsafe_allow_html=True)

    # ==============================
    # VARIABEL
    # ==============================
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="title">🧬 Penjelasan Variabel Penelitian</div>', unsafe_allow_html=True)

    st.markdown("""
    Variabel dalam dataset ini merepresentasikan **kondisi metabolik,
    fisiologis, dan genetik** yang berkaitan erat dengan diabetes tipe 2.
    """)

    st.markdown("""
    - **🧪 Glucose** → indikator utama diagnosis diabetes  
    - **💉 Insulin** → fungsi pankreas & regulasi gula darah  
    - **⚖️ BMI & SkinThickness** → obesitas & lemak tubuh  
    - **🧬 DPF** → faktor genetik / riwayat keluarga  
    - **👩 Age & Pregnancies** → faktor demografis & hormonal  
    - **🎯 Outcome** → status diabetes (0 = tidak, 1 = ya)
    """)

    st.markdown('<div class="highlight">📌 Variabel <b>Glucose</b>, <b>BMI</b>, dan <b>Insulin</b> secara konsisten menjadi prediktor paling signifikan dalam banyak studi.</div>', unsafe_allow_html=True)

    st.markdown("""
    🔗 **Referensi Medis:**
    - https://www.who.int/news-room/fact-sheets/detail/diabetes  
    - https://www.cdc.gov/diabetes/basics/diabetes.html
    """)

    st.markdown('</div>', unsafe_allow_html=True)

    # ==============================
    # REGRESI LOGISTIK
    # ==============================
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="title">🧠 Metode Utama: Regresi Logistik</div>', unsafe_allow_html=True)

    st.markdown("""
    Regresi logistik adalah metode statistik yang digunakan ketika
    **variabel target bersifat biner**, seperti sakit atau tidak sakit.

    Dalam studi ini, regresi logistik digunakan untuk
    **mengestimasi probabilitas seorang pasien menderita diabetes**
    berdasarkan kombinasi variabel klinis.

    Metode ini sangat populer dalam **penelitian kesehatan**
    karena mampu menjelaskan **hubungan sebab-akibat secara kuantitatif**
    melalui nilai **Odds Ratio (OR)**.
    """)

    st.latex(r"\ln\left(\frac{p}{1-p}\right) = \beta_0 + \beta_1X_1 + \cdots + \beta_kX_k")

    st.markdown("""
    Setiap koefisien (\(\beta\)) menunjukkan **arah dan kekuatan pengaruh**
    suatu variabel terhadap risiko diabetes.
    """)

    st.markdown('<div class="highlight">📈 Odds Ratio memudahkan tenaga kesehatan memahami seberapa besar risiko meningkat atau menurun.</div>', unsafe_allow_html=True)

    st.markdown("""
    🔗 **Referensi Regresi Logistik:**
    - https://towardsdatascience.com/logistic-regression-detailed-overview-46c4da4303bc  
    - https://www.statisticssolutions.com/logistic-regression  
    - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5078596/
    """)

    st.markdown('</div>', unsafe_allow_html=True)

    # ==============================
    # KMEANS
    # ==============================
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="title">🔍 Analisis Tambahan: K-Means Clustering</div>', unsafe_allow_html=True)

    st.markdown("""
    K-Means Clustering digunakan sebagai **analisis eksploratif**
    untuk mengelompokkan pasien berdasarkan kemiripan kondisi medis.

    Metode ini membantu menemukan **pola tersembunyi**
    seperti kelompok pasien berisiko tinggi,
    meskipun belum terdiagnosis diabetes.
    """)

    st.latex(r"J = \sum_{i=1}^{n} \sum_{j=1}^{k} \|x_i - \mu_j\|^2")

    st.markdown("""
    🔗 **Referensi K-Means:**
    - https://scikit-learn.org/stable/modules/clustering.html#k-means  
    - https://towardsdatascience.com/k-means-clustering-explained-6f2b4e970e7b
    """)

    st.markdown('</div>', unsafe_allow_html=True)

    # ==============================
    # KESIMPULAN
    # ==============================
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="title">🎯 Kesimpulan</div>', unsafe_allow_html=True)

    st.markdown("""
    Pendekatan berbasis data ini memungkinkan pemahaman
    **risiko diabetes secara objektif dan terukur**.

    Regresi logistik memberikan interpretasi yang jelas,
    sementara K-Means membantu eksplorasi pola pasien.
    Dashboard ini dirancang agar **ilmiah, edukatif,
    dan mudah dipahami oleh masyarakat umum**.
    """)

    st.markdown('</div>', unsafe_allow_html=True)
