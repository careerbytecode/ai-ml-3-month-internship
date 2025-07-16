import imaplib
import email
from email.header import decode_header
import os
from dotenv import load_dotenv
import datetime

def fetch_resumes():
    # Load environment variables
    load_dotenv()
    EMAIL = os.getenv("EMAIL_ADDRESS")
    PASSWORD = os.getenv("EMAIL_APP_PASSWORD")

    if not EMAIL or not PASSWORD:
        print("❌ Email or password not found in .env file.")
        return

    print("📧 Connecting to Gmail...")
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(EMAIL, PASSWORD)
        mail.select("inbox")
    except Exception as e:
        print(f"❌ Failed to connect: {e}")
        return

    # Set date filter for last 7 days
    date = (datetime.date.today() - datetime.timedelta(days=7)).strftime("%d-%b-%Y")

    # Search for UNSEEN emails since that date
    status, messages = mail.search(None, f'(UNSEEN SINCE {date})')
    email_ids = messages[0].split()

    print(f"📬 Found {len(email_ids)} unread email(s) since {date}")

    if not email_ids:
        print("📭 No new resumes found.")
        return

    os.makedirs("data", exist_ok=True)

    for num in email_ids:
        try:
            _, msg_data = mail.fetch(num, "(RFC822)")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    
                    subject_raw = msg.get("Subject", "(No Subject)")
                    subject, encoding = decode_header(subject_raw)[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding or "utf-8", errors="ignore")
                    
                    print(f"\n📨 Processing email: {subject}")

                    for part in msg.walk():
                        content_dispo = part.get("Content-Disposition", "")
                        if "attachment" in content_dispo:
                            filename = part.get_filename()
                            if filename and filename.endswith(".pdf"):
                                filepath = os.path.join("data", filename)
                                with open(filepath, "wb") as f:
                                    f.write(part.get_payload(decode=True))
                                print(f"✅ Saved resume: {filename}")
                            elif filename:
                                print(f"❌ Skipped non-PDF attachment: {filename}")
        except Exception as e:
            print(f"⚠️ Error processing email {num}: {e}")

    mail.logout()
    print("\n📁 Resume fetch complete.\n")

