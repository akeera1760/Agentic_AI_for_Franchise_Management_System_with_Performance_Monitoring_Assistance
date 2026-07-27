import os
import re
import sqlite3
import secrets
import smtplib
import time
import datetime
import subprocess
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate, make_msgid

import bcrypt
import jwt
import plotly.graph_objects as go
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Infosys Portal", page_icon="⚡", layout="wide", initial_sidebar_state="expanded")

os.makedirs(".streamlit", exist_ok=True)
with open(".streamlit/config.toml", "w", encoding="utf-8") as f:
    f.write('[theme]\nbase="light"\nprimaryColor="#ffd803"\nbackgroundColor="#f9fcfc"\nsecondaryBackgroundColor="#e3f6f5"\ntextColor="#2d334a"\n[client]\nshowErrorDetails=false\n')

COLORS = {
    "bg_main": "#f9fcfc",
    "bg_sidebar": "#e3f6f5",
    "bg_card": "#ffffff",
    "bg_card_alt": "#bae8e8",
    "text_main": "#2d334a",
    "text_heading": "#272343",
    "text_muted": "#64748b",
    "accent": "#ffd803",
    "accent_hover": "#e6c300",
    "accent_text": "#272343",
    "border": "#272343",
    "border_light": "#bae8e8",
    "success": "#34d399",
    "danger": "#f87171",
}

JWT_SECRET = os.getenv("JWT_SECRET", "super-secret-infosys-key-2026")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS", "mohamedsipli@gmail.com")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
OTP_EXPIRY_MINUTES = 5
ADMIN_EMAIL = "admin@gmail.com"
ADMIN_PASSWORD = "Admin@123"
DB_NAME = "infosys_portal.db"

st.markdown(
    f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Inter:wght@300;400;500;600&display=swap');
    * {{ margin: 0; padding: 0; }}
    html, body, .stApp {{ background: {COLORS['bg_main']} !important; font-family: 'Inter', sans-serif !important; color: {COLORS['text_main']} !important; }}
    footer, div[data-testid="stDecoration"] {{ visibility: hidden !important; display: none !important; }}
    header {{ background: transparent !important; z-index: 999999 !important; }}
    button[kind="header"], div[data-testid="stSidebarCollapsedControl"] button {{
        visibility: visible !important; display: flex !important; opacity: 1 !important;
        background-color: {COLORS['accent']} !important; border: 2px solid {COLORS['border']} !important;
        border-radius: 8px !important; padding: 6px !important; margin: 8px !important;
        box-shadow: 3px 3px 0px {COLORS['border']} !important;
    }}
    button[kind="header"] svg, div[data-testid="stSidebarCollapsedControl"] svg {{
        fill: {COLORS['text_heading']} !important; color: {COLORS['text_heading']} !important; stroke: {COLORS['text_heading']} !important;
    }}
    .block-container {{ padding: 2rem 2.5rem !important; max-width: 1200px; }}
    h1, h2, h3, h4 {{ font-family: 'Poppins', sans-serif !important; color: {COLORS['text_heading']} !important; }}
    label p {{ font-weight: 600 !important; color: {COLORS['text_heading']} !important; }}
    div[data-baseweb="base-input"], div[data-baseweb="select"] > div {{ background-color: transparent !important; border: none !important; }}
    div[data-baseweb="input"], div[data-baseweb="select"] {{ background-color: {COLORS['bg_card']} !important; border: 2px solid {COLORS['border']} !important; border-radius: 10px !important; }}
    div[data-baseweb="input"]:focus-within {{ border-color: {COLORS['accent']} !important; box-shadow: 4px 4px 0px {COLORS['border']} !important; }}
    input, div[data-baseweb="select"] span {{ color: {COLORS['text_main']} !important; -webkit-text-fill-color: {COLORS['text_main']} !important; }}
    div[data-testid="stButton"] button {{
        background-color: {COLORS['accent']} !important; color: {COLORS['accent_text']} !important;
        border: 2px solid {COLORS['border']} !important; border-radius: 10px !important;
        font-family: 'Inter', sans-serif !important; font-weight: 700 !important; font-size: 14px !important;
        height: 48px !important; min-height: 48px !important; white-space: nowrap !important;
        display: flex !important; align-items: center !important; justify-content: center !important;
        padding: 0px 16px !important; box-shadow: 4px 4px 0px {COLORS['border']} !important; width: 100%; transition: all 0.2s ease !important;
    }}
    div[data-testid="stButton"] button:hover {{
        background-color: {COLORS['accent_hover']} !important; transform: translate(-2px, -2px) !important;
        box-shadow: 6px 6px 0px {COLORS['border']} !important;
    }}
    section[data-testid="stSidebar"] {{ background: {COLORS['bg_sidebar']} !important; border-right: 2px solid {COLORS['border']} !important; }}
    .pn-card {{ background: {COLORS['bg_card']}; border: 2px solid {COLORS['border']}; border-radius: 14px; padding: 24px; box-shadow: 4px 4px 0px {COLORS['border_light']}; }}
</style>
""",
    unsafe_allow_html=True,
)


def get_db():
    conn = sqlite3.connect(DB_NAME, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def hash_txt(text: str) -> str:
    salt = bcrypt.gensalt(rounds=10)
    return bcrypt.hashpw(text.encode("utf-8"), salt).decode("utf-8")


def check_txt(text: str, hashed: str) -> bool:
    return bcrypt.checkpw(text.encode("utf-8"), hashed.encode("utf-8")) if hashed else False


def init_db():
    with get_db() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                security_question TEXT,
                security_answer_hash TEXT,
                is_admin INTEGER DEFAULT 0
            )
            """
        )
        conn.commit()

        existing_admin = conn.execute("SELECT 1 FROM users WHERE email=?", (ADMIN_EMAIL,)).fetchone()
        if not existing_admin:
            conn.execute(
                """
                INSERT INTO users (username, email, password_hash, security_question, security_answer_hash, is_admin)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                ("Administrator", ADMIN_EMAIL, hash_txt(ADMIN_PASSWORD), "What is your pet name?", hash_txt("admin"), 1),
            )
            conn.commit()


def validate_email(email: str) -> bool:
    return bool(re.fullmatch(r"[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", email))


def validate_password(password: str) -> bool:
    return bool(
        re.fullmatch(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$", password)
    )


def make_jwt(email: str, username: str, is_admin: bool):
    payload = {
        "email": email,
        "username": username,
        "is_admin": is_admin,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=4),
    }
    return jwt.encode(payload, JWT_SECRET, algorithm="HS256")


def verify_jwt(token):
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
    except Exception:
        return None


def generate_otp():
    return f"{secrets.randbelow(900000) + 100000}"


def make_otp_token(email: str, otp: str):
    payload = {
        "sub": email,
        "otp_hash": hash_txt(otp),
        "type": "password_reset_otp",
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=OTP_EXPIRY_MINUTES),
    }
    return jwt.encode(payload, JWT_SECRET, algorithm="HS256")


def verify_otp_token(token: str, input_otp: str, email: str):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        if payload.get("sub") != email or payload.get("type") != "password_reset_otp":
            return False, "Security token mismatch."
        if check_txt(input_otp, payload["otp_hash"]):
            return True, "Valid"
        return False, "Invalid 6-digit OTP code."
    except jwt.ExpiredSignatureError:
        return False, f"⚠️ This OTP code expired after {OTP_EXPIRY_MINUTES} minutes. Please request a new one."
    except Exception:
        return False, "Invalid or corrupted verification token."


def send_professional_email(to_email: str, otp: str, app_pass: str):
    msg = MIMEMultipart("alternative")
    msg["From"] = f"Infosys Support <{EMAIL_ADDRESS}>"
    msg["To"] = to_email
    msg["Subject"] = "Infosys Portal - Verification Code"
    msg["Date"] = formatdate(localtime=True)
    msg["Message-ID"] = make_msgid()
    msg["Reply-To"] = EMAIL_ADDRESS

    text_body = f"Your verification code for Infosys Portal is: {otp}\nThis code will expire in {OTP_EXPIRY_MINUTES} minutes.\nIf you did not request this code, please ignore this email."
    html_body = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; background-color: #f9fcfc; margin: 0; padding: 20px; }}
            .container {{ max-width: 500px; margin: 0 auto; background-color: #ffffff; border: 2px solid #272343; border-radius: 12px; padding: 30px; text-align: center; }}
            .title {{ color: #272343; font-size: 20px; font-weight: bold; margin-bottom: 15px; }}
            .text {{ color: #4a5568; font-size: 15px; line-height: 1.5; margin-bottom: 20px; }}
            .otp-box {{ background-color: #ffd803; color: #272343; font-size: 28px; font-weight: bold; letter-spacing: 5px; padding: 15px 20px; border: 2px solid #272343; border-radius: 8px; display: inline-block; margin: 10px 0; }}
            .footer {{ color: #718096; font-size: 12px; margin-top: 25px; border-top: 1px solid #edf2f7; padding-top: 15px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="title">Infosys Portal Verification</div>
            <div class="text">We received a request to reset your password for <b>{to_email}</b>. Please use the verification code below:</div>
            <div class="otp-box">{otp}</div>
            <div class="text">This code expires in <b>{OTP_EXPIRY_MINUTES} minutes</b>.</div>
            <div class="footer">If you did not request this code, you can safely ignore this email.<br>&copy; 2026 Infosys Portal.</div>
        </div>
    </body>
    </html>
    """
    msg.attach(MIMEText(text_body, "plain"))
    msg.attach(MIMEText(html_body, "html"))
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as s:
            s.starttls()
            s.login(EMAIL_ADDRESS, app_pass)
            s.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())
        return True, "Email sent successfully!"
    except smtplib.SMTPAuthenticationError:
        return False, "Gmail authentication failed. Check: EMAIL_ADDRESS and EMAIL_PASSWORD (App Password) are correct and 2-Step Verification is ON."
    except Exception as exc:
        return False, f"Error: {str(exc)}"


init_db()

for key, default in [("token", None), ("page", "Login"), ("reset_mode", None), ("reset_email", ""), ("otp_jwt", ""), ("otp_stage", "email")]:
    if key not in st.session_state:
        st.session_state[key] = default


def navigate(page_name: str):
    st.session_state.page = page_name
    st.rerun()


def auth_header(title: str, sub: str = "Intelligent Analytics Portal"):
    st.markdown(
        f"""
        <div style="text-align:center;padding:1.5rem 0 1rem;">
            <div style="font-size:40px;margin-bottom:10px;">⚡</div>
            <h1 style="font-size:2rem !important;margin:0;">Infosys Portal</h1>
            <p style="color:{COLORS['text_muted']};font-size:14px;margin:4px 0 0;">{sub}</p>
        </div>
        <div style="text-align:center;margin-bottom:1.5rem;"><span style="font-size:1.1rem;font-weight:700;color:{COLORS['text_heading']};">{title}</span></div>
        """,
        unsafe_allow_html=True,
    )


if not st.session_state.token:
    if st.session_state.page not in ["Login", "Signup", "Forgot"]:
        st.session_state.page = "Login"

    _, mid, _ = st.columns([1, 1.45, 1])
    with mid:
        if st.session_state.page == "Login":
            auth_header("Sign in to your account")
            email = st.text_input("Email address", placeholder="you@infosys.com").strip().lower()
            pwd = st.text_input("Password", type="password", placeholder="••••••••")
            st.markdown("<br>", unsafe_allow_html=True)

            col_l, col_c, col_r = st.columns([1, 1.15, 1.3])
            if col_l.button("Sign In →", use_container_width=True):
                if not email or not pwd:
                    st.error("⚠️ Email and password are required.")
                elif not validate_email(email):
                    st.error("⚠️ Please enter a valid email format.")
                else:
                    with st.spinner("Signing in..."):
                        with get_db() as conn:
                            user = conn.execute(
                                "SELECT username, email, password_hash, is_admin FROM users WHERE email=?",
                                (email,),
                            ).fetchone()
                        if user and check_txt(pwd, user["password_hash"]):
                            st.session_state.token = make_jwt(user["email"], user["username"], bool(user["is_admin"]))
                            st.session_state.page = "Dashboard"
                            st.success("✅ Login successful")
                            st.rerun()
                        else:
                            st.error("❌ Invalid username or password.")

            if col_c.button("Create Account", use_container_width=True):
                navigate("Signup")
            if col_r.button("Forgot Password", use_container_width=True):
                navigate("Forgot")

        elif st.session_state.page == "Signup":
            auth_header("Create an account", "Join Infosys Portal today")
            uname = st.text_input("Full name / Username", placeholder="Jane Doe").strip()
            email = st.text_input("Email address", placeholder="you@infosys.com").strip().lower()
            pwd = st.text_input("Password", type="password", placeholder="Min. 8 chars")
            confirm_pwd = st.text_input("Confirm password", type="password", placeholder="Re-enter password")
            sq = st.selectbox(
                "Security Question",
                [
                    "What is your pet name?",
                    "What is your mother's maiden name?",
                    "What is your favourite city?",
                ],
            )
            sa = st.text_input("Your answer", placeholder="Security answer").strip().lower()
            st.markdown("<br>", unsafe_allow_html=True)

            if st.button("Create Account & Login →", use_container_width=True):
                if not uname or not email or not pwd or not confirm_pwd or not sa:
                    st.error("⚠️ All fields are required.")
                elif not validate_email(email):
                    st.error("⚠️ Please enter a valid email format.")
                elif not validate_password(pwd):
                    st.error("⚠️ Password must be at least 8 characters with uppercase, lowercase, number and symbol.")
                elif pwd != confirm_pwd:
                    st.error("❌ Passwords do not match.")
                else:
                    with st.spinner("Creating account..."):
                        with get_db() as conn:
                            existing = conn.execute("SELECT 1 FROM users WHERE username=? OR email=?", (uname, email)).fetchone()
                            if existing:
                                st.error("❌ Username or email already registered.")
                            else:
                                conn.execute(
                                    "INSERT INTO users (username, email, password_hash, security_question, security_answer_hash, is_admin) VALUES (?, ?, ?, ?, ?, ?)",
                                    (uname, email, hash_txt(pwd), sq, hash_txt(sa), 0),
                                )
                                conn.commit()
                        st.session_state.token = make_jwt(email, uname, False)
                        st.session_state.page = "Dashboard"
                        st.success("✅ Account created and logged in.")
                        st.rerun()

            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("← Back to Sign In", use_container_width=True):
                navigate("Login")

        elif st.session_state.page == "Forgot":
            auth_header("Reset your password", "Choose your verification method")
            if st.session_state.reset_mode is None:
                email = st.text_input("Registered email address", placeholder="you@infosys.com").strip().lower()
                st.markdown("<br>", unsafe_allow_html=True)

                col_sq, col_otp = st.columns(2)
                if col_sq.button("Via Security Question", use_container_width=True):
                    if not email:
                        st.error("⚠️ Please enter an email address.")
                    elif not validate_email(email):
                        st.error("⚠️ Please enter a valid email format.")
                    else:
                        with get_db() as conn:
                            user = conn.execute(
                                "SELECT security_question FROM users WHERE email=?",
                                (email,),
                            ).fetchone()
                        if user and user["security_question"]:
                            st.session_state.reset_email = email
                            st.session_state.reset_mode = "sq"
                            st.rerun()
                        else:
                            st.error("❌ Email not found or no security question is set.")

                if col_otp.button("Via OTP", use_container_width=True):
                    if not email:
                        st.error("⚠️ Please enter an email address.")
                    elif not validate_email(email):
                        st.error("⚠️ Please enter a valid email format.")
                    else:
                        with get_db() as conn:
                            exists = conn.execute("SELECT 1 FROM users WHERE email=?", (email,)).fetchone()
                        if exists:
                            st.session_state.reset_email = email
                            st.session_state.reset_mode = "otp"
                            st.session_state.otp_stage = "email"
                            st.rerun()
                        else:
                            st.error("❌ Email address not registered in the system.")
            else:
                if st.session_state.reset_mode == "sq":
                    with get_db() as conn:
                        user = conn.execute(
                            "SELECT security_question FROM users WHERE email=?",
                            (st.session_state.reset_email,),
                        ).fetchone()
                    st.info(f"❓ **Security Question:** {user['security_question']}")
                    ans = st.text_input("Your answer").strip().lower()
                    npw = st.text_input("New password (min 8 chars)", type="password")
                    confirm_npw = st.text_input("Confirm new password", type="password")
                    st.markdown("<br>", unsafe_allow_html=True)
                    if st.button("Reset Password →", use_container_width=True):
                        if not ans or not npw or not confirm_npw:
                            st.error("⚠️ All fields are required.")
                        elif not validate_password(npw):
                            st.error("⚠️ Password must be at least 8 characters with uppercase, lowercase, number and symbol.")
                        elif npw != confirm_npw:
                            st.error("❌ Passwords do not match.")
                        else:
                            with get_db() as conn:
                                stored = conn.execute(
                                    "SELECT security_answer_hash FROM users WHERE email=?",
                                    (st.session_state.reset_email,),
                                ).fetchone()
                            if stored and check_txt(ans, stored["security_answer_hash"]):
                                with get_db() as conn:
                                    conn.execute(
                                        "UPDATE users SET password_hash=? WHERE email=?",
                                        (hash_txt(npw), st.session_state.reset_email),
                                    )
                                st.success("✅ Password updated successfully!")
                                st.session_state.reset_email = ""
                                st.session_state.reset_mode = None
                                navigate("Login")
                            else:
                                st.error("❌ Incorrect security answer.")

                elif st.session_state.reset_mode == "otp":
                    if st.session_state.otp_stage == "email":
                        if not EMAIL_PASSWORD or EMAIL_PASSWORD.strip() == "":
                            st.error("❌ Gmail App Password is missing! Steps:\n1. Go to your Google Account settings\n2. Turn on 2-Step Verification\n3. Search for 'App Passwords'\n4. Create an app password for Infosys\n5. Copy it\n6. In Colab Secrets, add EMAIL_PASSWORD with the 16-character password")
                        else:
                            otp = generate_otp()
                            with st.spinner("Sending 6-digit OTP..."):
                                ok, msg = send_professional_email(st.session_state.reset_email, otp, EMAIL_PASSWORD)
                            if ok:
                                st.session_state.otp_jwt = make_otp_token(st.session_state.reset_email, otp)
                                st.session_state.otp_stage = "otp"
                                st.success("✅ 6-digit OTP sent! Check your inbox.")
                                st.rerun()
                            else:
                                st.error(f"❌ {msg}")
                    elif st.session_state.otp_stage == "otp":
                        st.info(f"📧 Code sent to **{st.session_state.reset_email}** (Valid for {OTP_EXPIRY_MINUTES} mins).")
                        otp_input = st.text_input("6-Digit Verification Code", placeholder="e.g. 849201", max_chars=6)
                        npw = st.text_input("New password (min 8 chars)", type="password")
                        confirm_npw = st.text_input("Confirm new password", type="password")
                        st.markdown("<br>", unsafe_allow_html=True)
                        c1, c2 = st.columns([1.2, 1])
                        if c1.button("Verify Code →", use_container_width=True):
                            if not otp_input or len(otp_input) != 6:
                                st.error("⚠️ Please enter the valid 6-digit code.")
                            elif not validate_password(npw):
                                st.error("⚠️ Password must be at least 8 characters with uppercase, lowercase, number and symbol.")
                            elif npw != confirm_npw:
                                st.error("❌ Passwords do not match.")
                            else:
                                ok, msg = verify_otp_token(st.session_state.otp_jwt, otp_input, st.session_state.reset_email)
                                if ok:
                                    with get_db() as conn:
                                        conn.execute(
                                            "UPDATE users SET password_hash=? WHERE email=?",
                                            (hash_txt(npw), st.session_state.reset_email),
                                        )
                                    st.success("🎉 Password updated successfully!")
                                    st.session_state.reset_email = ""
                                    st.session_state.reset_mode = None
                                    st.session_state.otp_jwt = ""
                                    st.session_state.otp_stage = "email"
                                    navigate("Login")
                                else:
                                    st.error(f"❌ {msg}")
                        if c2.button("← Back", use_container_width=True):
                            st.session_state.reset_mode = None
                            st.session_state.otp_jwt = ""
                            st.session_state.otp_stage = "email"
                            st.session_state.reset_email = ""
                            navigate("Login")

            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("← Cancel", use_container_width=True):
                st.session_state.reset_email = ""
                st.session_state.reset_mode = None
                st.session_state.otp_jwt = ""
                st.session_state.otp_stage = "email"
                navigate("Login")

else:
    payload = verify_jwt(st.session_state.token)
    if not payload:
        st.session_state.token = None
        st.session_state.page = "Login"
        st.rerun()

    email = payload["email"]
    with get_db() as conn:
        user = conn.execute("SELECT username, is_admin FROM users WHERE email=?", (email,)).fetchone()

    if not user:
        st.session_state.token = None
        st.session_state.page = "Login"
        st.rerun()

    uname = user["username"]
    is_admin = bool(user["is_admin"])

    with st.sidebar:
        st.markdown(
            f"""
            <div style="padding:16px 8px;text-align:center;">
                <div style="font-size:28px;">⚡</div>
                <div style="font-weight:700;font-size:16px;color:{COLORS['text_heading']};">Infosys Portal</div>
                <div style="font-size:11px;color:{COLORS['text_muted']};">{'Admin Panel' if is_admin else 'Intelligent Analytics'}</div>
            </div><hr style="border-color:{COLORS['border_light']};">
            """,
            unsafe_allow_html=True,
        )
        opts = ["Dashboard", "Logout"] if is_admin else ["Dashboard", "Analytics", "Reports", "Logout"]
        menu = option_menu(
            None,
            opts,
            icons=["house", "box-arrow-right"] if is_admin else ["house", "graph-up", "file-text", "box-arrow-right"],
            styles={
                "container": {"background-color": COLORS["bg_sidebar"]},
                "nav-link-selected": {"background-color": COLORS["accent"], "color": COLORS["accent_text"]},
            },
        )
        if menu == "Logout":
            st.session_state.token = None
            st.session_state.page = "Login"
            st.session_state.reset_mode = None
            st.session_state.reset_email = ""
            st.session_state.otp_jwt = ""
            st.session_state.otp_stage = "email"
            st.rerun()

    if is_admin:
        st.markdown(
            f"""
            <div style="background:{COLORS['text_heading']};border-radius:16px;padding:24px 32px;display:flex;justify-content:space-between;align-items:center;margin-bottom:24px;">
                <div><h1 style="color:{COLORS['accent']} !important;margin:0;font-size:24px !important;">⚡ Infosys Portal</h1><div style="color:{COLORS['bg_card_alt']};font-size:13px;">Admin Control Panel</div></div>
                <div style="background:{COLORS['accent']};padding:8px 18px;border-radius:30px;font-weight:700;color:{COLORS['text_heading']};">🛡️ {uname}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            f"""
            <div class="pn-card" style="text-align:center;padding:40px 20px;margin-bottom:26px;">
                <h2 style="font-size:30px !important;margin-bottom:10px;">🛡️ Admin Dashboard</h2>
                <p style="color:{COLORS['text_muted']};font-size:16px;font-weight:500;">Welcome to the administrator area.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        with get_db() as conn:
            users = conn.execute("SELECT username, email FROM users WHERE is_admin=0 ORDER BY username").fetchall()
        if users:
            st.markdown("<h3>Registered Users</h3>", unsafe_allow_html=True)
            st.table([{"Username": row["username"], "Email": row["email"]} for row in users])
        else:
            st.info("No non-admin users are currently registered.")
    else:
        st.markdown(
            f"""
            <div style="background:{COLORS['text_heading']};border-radius:16px;padding:24px 32px;display:flex;justify-content:space-between;align-items:center;margin-bottom:24px;">
                <div><h1 style="color:{COLORS['accent']} !important;margin:0;font-size:24px !important;">⚡ Infosys Portal</h1><div style="color:{COLORS['bg_card_alt']};font-size:13px;">Analytics Dashboard</div></div>
                <div style="background:{COLORS['accent']};padding:8px 18px;border-radius:30px;font-weight:700;color:{COLORS['text_heading']};">👤 {uname}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        c1, c2, c3, c4 = st.columns(4)
        for col, icon, lbl, val in [
            (c1, "📄", "Documents Indexed", "128"),
            (c2, "🔍", "Searches Today", "47"),
            (c3, "📊", "Efficiency Score", "98.4%"),
            (c4, "🛡️", "Security Status", "Secured"),
        ]:
            col.markdown(
                f"""
                <div class="pn-card" style="text-align:center;">
                    <div style="font-size:28px;">{icon}</div>
                    <div style="font-size:26px;font-weight:700;color:{COLORS['text_heading']};">{val}</div>
                    <div style="color:{COLORS['text_muted']};font-size:12px;font-weight:600;">{lbl}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("<br>", unsafe_allow_html=True)
        fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=92,
                title={"text": "System Health Index", "font": {"color": COLORS["text_heading"], "size": 14}},
                gauge={
                    "axis": {"range": [0, 100]},
                    "bar": {"color": COLORS["accent"]},
                    "bgcolor": COLORS["bg_card_alt"],
                    "borderwidth": 1,
                    "bordercolor": COLORS["border"],
                },
            )
        )
        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            font={"color": COLORS["text_main"], "family": "Inter"},
            height=260,
            margin=dict(l=10, r=10, t=40, b=10),
        )
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(
            f"<div class='pn-card' style='padding:18px;'>Welcome <b>{uname}</b>! You are logged in as <b>{email}</b>.</div>",
            unsafe_allow_html=True,
        )
