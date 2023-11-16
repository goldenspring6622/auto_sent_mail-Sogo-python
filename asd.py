import imaplib
import email
from email.header import decode_header

# Email account details
email_address = "ray.huynh@qt-globalgroup.com"
password = "demo123"

# Connect to the mail server (in this example, using Gmail)
mail = imaplib.IMAP4_SSL("mail.qntdata.com")

# Login to the email account
mail.login(email_address, password)

# Select the mailbox (in this case, "inbox")
mail.select("inbox")

# Search for all emails in the inbox
status, messages = mail.search(None, "ALL")

# Get the list of email IDs
email_ids = messages[0].split()

# Loop through the email IDs and fetch the email data
for email_id in email_ids:
    # Fetch the email by ID
    status, msg_data = mail.fetch(email_id, "(RFC822)")

    # Parse the email data
    raw_email = msg_data[0][1]
    msg = email.message_from_bytes(raw_email)

    # Extract email details (subject, sender, etc.)
    subject, encoding = decode_header(msg["Subject"])[0]
    if isinstance(subject, bytes):
        subject = subject.decode(encoding or "utf-8")

    from_address = msg.get("From")
    date_sent = msg.get("Date")

    # Print or process the email details as needed
    print(f"Subject: {subject}")
    print(f"From: {from_address}")
    print(f"Date: {date_sent}")
    print("-----")

# Logout from the email account
mail.logout()
