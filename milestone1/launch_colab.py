import os
import time
import subprocess
from pyngrok import ngrok
from google.colab import userdata

try:
    os.environ['JWT_SECRET'] = userdata.get('JWT_SECRET') or 'super-secret-infosys-key-2026'
    os.environ['EMAIL_ADDRESS'] = userdata.get('EMAIL_ADDRESS') or 'mohamedsipli@gmail.com'
    email_pwd = userdata.get('EMAIL_PASSWORD')
    if email_pwd:
        os.environ['EMAIL_PASSWORD'] = email_pwd
    ngrok_token = userdata.get('NGROK_AUTHTOKEN')
    if ngrok_token:
        ngrok.set_auth_token(ngrok_token)
    print("✅ Secrets loaded successfully.")
except Exception as exc:
    print(f"⚠️ Secret setup warning: {exc}")

subprocess.run(["pkill", "-f", "streamlit"], check=False)
subprocess.run(["pkill", "-f", "ngrok"], check=False)
time.sleep(2)

print("\n🔄 Starting Streamlit...")
process = subprocess.Popen(
    ["streamlit", "run", "app.py", "--server.port", "8501", "--server.headless", "true"],
    env=os.environ.copy(),
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
)

# Wait longer for Streamlit to fully start
print("⏳ Waiting for Streamlit to initialize...")
time.sleep(6)

try:
    # Check if Streamlit started without errors
    if process.poll() is not None:
        _, stderr = process.communicate()
        print(f"❌ Streamlit failed to start:\n{stderr}")
        raise RuntimeError("Streamlit process exited unexpectedly")
    
    tunnels = ngrok.get_tunnels()
    if tunnels:
        public_url = tunnels[0].public_url
        print("♻️ Reusing existing active Ngrok tunnel...")
    else:
        public_url = ngrok.connect(8501).public_url
        print("🚀 Created new Ngrok tunnel...")

    print("=" * 70)
    print(f"👉 Infosys Portal Live URL: {public_url}")
    print("=" * 70)
    print("⏳ Server running! Press Ctrl+C or stop the cell to shut down.")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n🛑 Shutting down server...")
    process.terminate()
    subprocess.run(["pkill", "-f", "streamlit"], check=False)
    print("✅ Streamlit stopped.")
