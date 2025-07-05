from forex_python.converter import CurrencyRates
import smtplib
from email.message import EmailMessage
import traceback
import time


EMAIL_SENDER = 'rhiodelacruz0717@gmail.com'      
EMAIL_PASSWORD = 'uqftddxkaxqtiuil'          
EMAIL_RECEIVER = 'rhiodelacruz032723@gmail.com'      
THRESHOLD_RATE = 53.00                            
CHECK_INTERVAL_SECONDS = 300                      

def send_email_alert(rate):
    msg = EmailMessage()
    msg['Subject'] = '🚨 USD Rate Alert!'
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER
    msg.set_content(f"📈 USD to PHP is now ₱{rate:.2f}.\n\nCheck now if you want to act.")

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print(f"[EMAIL SENT] USD to PHP = ₱{rate:.2f}")
    except Exception:
        print("[ ERROR] Failed to send email:")
        traceback.print_exc()

def check_usd_to_php():
    try:
        c = CurrencyRates()
        rate = c.get_rate('USD', 'PHP')
        print(f"[INFO] USD to PHP = ₱{rate:.2f}")
        if rate >= THRESHOLD_RATE:
            print(f"[ALERT] Rate hit ₱{rate:.2f}, sending email...")
            send_email_alert(rate)
        else:
            print(f"[OK] Rate ₱{rate:.2f} is below threshold ₱{THRESHOLD_RATE:.2f}")
    except Exception:
        print("[ ERROR] Failed to check exchange rate:")
        traceback.print_exc()


print("[RUNNING] Auto-checking USD to PHP every 5 minutes...\n")
while True:
    check_usd_to_php()
    time.sleep(CHECK_INTERVAL_SECONDS)