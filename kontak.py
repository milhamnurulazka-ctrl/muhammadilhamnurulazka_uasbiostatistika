import streamlit as st

def contact_me():

    # =========================
    # STYLE GLOBAL (SAMA DENGAN PAGE LAIN)
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

    .profile-img {
        width:130px;
        height:130px;
        border-radius:50%;
        object-fit:cover;
        border:4px solid #2563eb;
    }

    .social-icon img {
        transition: transform 0.3s ease;
    }

    .social-icon img:hover {
        transform: scale(1.15);
    }
    </style>
    """, unsafe_allow_html=True)

    # =========================
    # HERO HEADER
    # =========================
    st.markdown("""
    <div class="hero-box">
        <div class="hero-title">📬 Kontak & Informasi Pengembang</div>
        <div class="hero-subtitle">
            Informasi resmi pengembang serta media komunikasi
            untuk <b>Diabetes Analytics Dashboard</b>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # PROFIL PENGEMBANG
    # =========================
    st.markdown("""
    <div class="card">
        <div class="section-title">👨‍💻 Profil Pengembang</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 3])

    with col1:
        st.markdown("""
        <div style="text-align:center;">
            <img src="https://i.pinimg.com/originals/05/5a/91/055a91979264664a1ee12b9453610d82.png"
                 class="profile-img">
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <p class="desc">
        <b>Nama:</b> Muhammad Ilham Nurul Azka<br>
        <b>NIM:</b> B2D023007<br>
        <b>Universitas:</b> Universitas Muhammadiyah Semarang<br>
        <b>Program Studi:</b> S1 Sains Data<br>
        <b>Dosen Pembimbing:</b> Alwan Fadlurohman, S.Stat., M.Stat
        </p>
        """, unsafe_allow_html=True)

    # =========================
    # MEDIA SOSIAL
    # =========================
    st.markdown("""
    <div class="card">
        <div class="section-title">🌐 Media Sosial & Kontak</div>
        <p class="desc">Klik ikon di bawah untuk terhubung langsung</p>
    </div>
    """, unsafe_allow_html=True)

    social_links = {
        "Email": ("mailto:milhamnurulazka@gmail.com", "https://img.icons8.com/fluency/48/gmail-new.png"),
        "GitHub": ("https://github.com/milhamnurulazka-ctrl", "https://img.icons8.com/ios-glyphs/48/github.png"),
        "WhatsApp": ("https://wa.me/6285878599921", "https://img.icons8.com/fluency/48/whatsapp.png"),
        "Instagram": ("https://www.instagram.com/ilhnrlazk", "https://img.icons8.com/fluency/48/instagram-new.png")
    }

    cols = st.columns(len(social_links))

    for col, (name, (url, icon)) in zip(cols, social_links.items()):
        with col:
            st.markdown(f"""
            <div class="social-icon" style="text-align:center;">
                <a href="{url}" target="_blank">
                    <img src="{icon}" width="45">
                </a>
                <p style="font-size:13px; margin-top:6px; font-weight:600;">{name}</p>
            </div>
            """, unsafe_allow_html=True)

    # =========================
    # FORM FEEDBACK
    # =========================
    st.markdown("""
    <div class="card">
        <div class="section-title">✉️ Kirim Pesan / Feedback</div>
    </div>
    """, unsafe_allow_html=True)

    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Nama Lengkap")
        email = st.text_input("Email")
        message = st.text_area("Pesan / Feedback", height=120)
        submit = st.form_submit_button("📤 Kirim Pesan")

        if submit:
            if name and email and message:
                st.success("✅ Terima kasih! Pesan Anda berhasil dikirim.")
            else:
                st.error("⚠️ Mohon lengkapi semua kolom.")

    # =========================
    # FOOTNOTE
    # =========================
    st.markdown("""
    <div class="card">
        <p class="desc">
        Dashboard ini dikembangkan untuk keperluan akademik
        <b>UAS Machine Learning & Biostatistika</b>.
        </p>
    </div>
    """, unsafe_allow_html=True)
