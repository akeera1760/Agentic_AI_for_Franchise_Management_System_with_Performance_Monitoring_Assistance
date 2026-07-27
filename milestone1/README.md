# ⚡ Infosys Portal - Authentication System

A complete **Streamlit-based authentication portal** with login, signup, forgot password, and admin dashboard capabilities.

---

## 🎯 Features

✅ **Three Authentication Pages**
- **Login Page** - Secure email/password authentication with JWT tokens
- **Signup Page** - User registration with email validation and security questions
- **Forgot Password Page** - Dual recovery methods (security question or OTP via Gmail)

✅ **Admin Dashboard**
- View all registered users
- System health metrics and analytics
- Admin-only control panel

✅ **User Dashboard**
- Personal analytics cards (Documents, Searches, Efficiency, Security Status)
- System health gauge visualization
- Logout functionality

✅ **Security Features**
- Bcrypt password hashing (optimized for performance)
- JWT session tokens (4-hour expiry)
- Email validation with regex support
- Security questions for password recovery
- OTP verification via Gmail SMTP

✅ **Performance Optimized**
- Reduced bcrypt rounds (10) for faster signup/login
- No artificial delays - instant UI feedback
- Progress spinners for user feedback during operations

---

## 📋 Requirements

- Python 3.8+
- Streamlit 1.59.1
- bcrypt 5.0.0
- PyJWT 2.13.0
- Plotly 6.9.0
- streamlit_option_menu
- SQLite3 (built-in with Python)

---

## 🚀 Installation & Setup

### **Local Installation (VS Code)**

1. **Clone/Extract the project**
```bash
cd path/to/infosys project
```

2. **Install dependencies**
```bash
pip install streamlit bcrypt pyjwt plotly streamlit_option_menu pillow
```

3. **Run the app**
```bash
streamlit run app.py
```

The app will open at **http://localhost:8501**

---

## 🌐 Google Colab Setup

### **Step 1: Create 3 Cells in Colab**

**Cell 1: Install Dependencies**
```python
!pip install streamlit bcrypt pyjwt plotly streamlit_option_menu pyngrok google-colab pillow
```

**Cell 2: Create Files**
```python
# Copy entire app.py content
with open('app.py', 'w') as f:
    f.write('''[PASTE FULL app.py CONTENT HERE]''')

# Copy entire launch_colab.py content
with open('launch_colab.py', 'w') as f:
    f.write('''[PASTE FULL launch_colab.py CONTENT HERE]''')

print("✅ Files created successfully!")
```

**Cell 3: Add Secrets (Optional - for OTP)**
```python
from google.colab import userdata

# Add to Colab Secrets tab:
# - NGROK_AUTHTOKEN: Your ngrok auth token (from https://dashboard.ngrok.com)
# - EMAIL_PASSWORD: Gmail App Password (16 chars, from Google Account settings)
# - JWT_SECRET: Any random string (auto-generated if not provided)
# - EMAIL_ADDRESS: Your Gmail address (auto-set to mohamedsipli@gmail.com)
```

**Cell 4: Run the App**
```python
%run launch_colab.py
```

The app will create an ngrok public URL automatically!

---

## 👤 Default Admin Credentials

```
Email: admin@gmail.com
Password: Admin@123
Security Question Answer: admin
```

---

## 📖 How to Use

### **1. Login**
- Sign in with email and password
- Uses JWT tokens for session management (4-hour expiry)

### **2. Signup**
- Create new account with:
  - Full name/Username
  - Email address (supports alphanumeric: user123@gmail.com)
  - Password (min 8 chars: uppercase, lowercase, number, symbol)
  - Security question answer
- Auto-login after successful signup

### **3. Forgot Password**
- **Option A:** Answer security question you set during signup
- **Option B:** Receive 6-digit OTP via email (requires EMAIL_PASSWORD)

### **4. Admin Dashboard**
- Login with admin@gmail.com / Admin@123
- View all registered users
- See system metrics and health indicators

### **5. User Dashboard**
- View analytics cards
- System performance gauge
- Logout to return to login

---

## 🗄️ Database Schema

**SQLite Database: `infosys_portal.db`**

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    security_question TEXT,
    security_answer_hash TEXT,
    is_admin INTEGER DEFAULT 0
)
```

---

## 🔧 Environment Variables

Set these for Colab deployment:

| Variable | Description | Default |
|----------|-------------|---------|
| `JWT_SECRET` | Secret key for JWT tokens | `super-secret-infosys-key-2026` |
| `EMAIL_ADDRESS` | Gmail address for OTP | `mohamedsipli@gmail.com` |
| `EMAIL_PASSWORD` | Gmail App Password (16 chars) | *(Optional)* |
| `NGROK_AUTHTOKEN` | ngrok tunnel token | *(Colab only)* |

---

## 🛠️ Configuration

Edit `.streamlit/config.toml` for theme customization:
- Light theme with yellow accent (#ffd803)
- Custom color scheme
- Error details disabled for security

---

## 📁 Project Structure

```
infosys project/
├── app.py                  # Main Streamlit application
├── launch_colab.py         # Google Colab launcher
├── .streamlit/
│   └── config.toml         # Streamlit configuration
├── infosys_portal.db       # SQLite database (auto-created)
└── README.md               # This file
```

---

## 🚨 Troubleshooting

### **Issue: "File does not exist: app.py" in Colab**
- Make sure you pasted `app.py` content in Cell 2
- Run Cell 2 before running Cell 4

### **Issue: "Gmail authentication failed" for OTP**
- Ensure 2-Step Verification is ON in Google Account
- Create an App Password (16 characters)
- Add it as EMAIL_PASSWORD in Colab Secrets
- Use your actual Gmail address

### **Issue: Streamlit runs slowly**
- Clear browser cache (Ctrl+Shift+Delete)
- Restart the streamlit server
- Check internet connection

### **Issue: ngrok connection refused in Colab**
- Check that NGROK_AUTHTOKEN is set in Secrets
- Get token from: https://dashboard.ngrok.com
- Ensure ngrok is installed: `!pip install pyngrok`

---

## 📊 Performance Optimizations

✅ Bcrypt rounds reduced to 10 (from default 12) = **faster hashing**
✅ All artificial delays removed = **instant UI response**
✅ Progress spinners added = **better user feedback**
✅ CSS optimized = **faster rendering**

---

## 🔐 Security Notes

- Passwords hashed with bcrypt (salt rounds: 10)
- JWT tokens expire after 4 hours
- OTP codes expire after 5 minutes
- Email validation prevents invalid addresses
- Password requires: uppercase, lowercase, number, symbol
- Security questions stored hashed (never plaintext)

---

## 🚀 Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Streamlit** | Web application framework |
| **SQLite3** | Database |
| **bcrypt** | Password hashing |
| **PyJWT** | Session tokens |
| **Plotly** | Analytics charts |
| **ngrok** | Colab tunneling |

---

## 📝 License

Built for Infosys Portal 2026

---

## ✉️ Support

For issues or questions, check:
1. Email validation format
2. Password requirements (8+ chars, mixed case, number, symbol)
3. Gmail App Password (not regular password)
4. Environment variables set correctly

---

**Last Updated:** July 2026
