import gspread
import smtplib
from email.mime.text import MIMEText
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import messagebox

from flask import Flask


from flask import Flask, request, abort
from datetime import datetime

app = Flask(__name__)


@app.route("/<id>")
def track_pixel(id):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - Email opened "

    with open("tracking_log.txt", "a") as log_file:
        if "favico" not in id:
            log_file.write(id + " - " + log_entry + "\n")

    # Send an email notification (if needed)
    # send_email('Email Opened Notification', log_entry)

    transparent_pixel = ""

    return transparent_pixel, 200, {"Content-Type": "image/gif"}
    # return 200, {"Content-Type": "image/gif"}


def validate_inputs(json_file, email_address, password, sheet_url, url):
    # Kiểm tra xem có ô nhập nào không được điền
    if not json_file or not email_address or not password or not sheet_url:
        messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin!")
        return False
    if url == "Please run socketxp in command prompt to get Public URL and paste here":
        messagebox.showerror("Lỗi", "Vui lòng điền socketxp url")
        return False
    return True


def send_emails():
    try:
        # Tạo một chuỗi để lưu thông tin về email đã gửi
        sent_email_info = ""

        json_file = json_file_entry.get()
        email_address = email_address_entry.get()
        password = password_entry.get()
        sheet_url = sheet_url_entry.get()
        url_ = url_entry.get()
        if not validate_inputs(json_file, email_address, password, sheet_url, url_):
            return
        gc = gspread.service_account(filename=json_file)
        # sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1vY20VHnx5hHFjyF1P3ifHQH4TsC77TAkh--BOutUmoI/edit?usp=sharing')
        sh = gc.open_by_url(sheet_url)
        worksheet = sh.get_worksheet(0)
        data = worksheet.get_all_values()

        smtp_server = "mail.qntdata.com"
        smtp_port = 587
        # email_address = 'ray.huynh@qt-globalgroup.com'
        # password = 'demo123'
        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_connection.starttls()
        smtp_connection.login(email_address, password)
        i = 1
        for row in data:
            if i:
                i = 0
                continue
            subject = row[0]
            recipient_email = row[2]
            for recipientemail in recipient_email.split(","):
                html_body = f"""
                <html>
                    <body>
                        <p>Hello</p>
                        <p>{row[1]}</p>
                        <p>Thank for reading. </p>
                        <img src="{url_}/{recipientemail}" height="0" width="0" alt="Pixel" style="display:none;">
                </html>"""
                message = MIMEText(html_body, "html")
                message["From"] = email_address
                message["To"] = recipientemail
                message["Subject"] = subject

                smtp_connection.sendmail(
                    email_address, recipientemail, message.as_string()
                )
                print("Email sent successfully")
                sent_email_info += (
                    f"Sent email to: {recipientemail}, Subject: {subject}\n"
                )

        smtp_connection.quit()
        # Hiển thị thông tin về email đã gửi trong ô hiển thị
        info_text.config(state=tk.NORMAL)
        info_text.delete("1.0", tk.END)
        info_text.insert(tk.END, sent_email_info)
        info_text.config(state=tk.DISABLED)
        messagebox.showinfo("Thông báo", "Email đã được gửi thành công!")
    except smtplib.SMTPAuthenticationError:
        messagebox.showerror(
            "Lỗi", "Lỗi xác thực SMTP: Vui lòng kiểm tra lại tên đăng nhập và mật khẩu."
        )
    except gspread.exceptions.APIError:
        messagebox.showerror(
            "Lỗi", "Lỗi API Google Sheets: Vui lòng kiểm tra URL hoặc quyền truy cập."
        )
    except Exception as e:
        messagebox.showerror("Lỗi", f"Có lỗi xảy ra khi gửi email: {str(e)}")


def browse_file():
    json_file = filedialog.askopenfilename()
    json_file_entry.delete(0, tk.END)
    json_file_entry.insert(0, json_file)


def tracking():
    app.run(host="127.0.0.1", port=5000, debug=False)


root = tk.Tk()
root.title("Send Emails")
root.geometry("400x600")

json_file_label = ttk.Label(root, text="Credentials File: (*.Json)")
json_file_label.pack(padx=20, pady=5)

json_file_entry = ttk.Entry(root, width=150)
json_file_entry.pack(padx=20, pady=5)
json_file_entry.insert(
    0, "C:/Users/ADMIN/Desktop/auto-sent-mail-sogo-python-0f294f0cd072.json"
)
browse_button = ttk.Button(root, text="Browse", command=browse_file, width=150)
browse_button.pack(padx=20, pady=5)

email_address_label = ttk.Label(root, text="Email Sent Address:")
email_address_label.pack(padx=20, pady=5)

email_address_entry = ttk.Entry(root, width=150)
email_address_entry.pack(padx=20, pady=5)
email_address_entry.insert(0, "ray.huynh@qt-globalgroup.com")
password_label = ttk.Label(root, text="Password:")
password_label.pack(padx=20, pady=5)

password_entry = ttk.Entry(
    root, show="*", width=150
)  # Show asterisks for password entry
password_entry.pack(padx=20, pady=5)
password_entry.insert(0, "demo123")
sheet_url_label = ttk.Label(root, text="Sheet URL:")
sheet_url_label.pack(padx=20, pady=5)

sheet_url_entry = ttk.Entry(root, width=150)
sheet_url_entry.pack(padx=20, pady=5)
sheet_url_entry.insert(
    0,
    "https://docs.google.com/spreadsheets/d/14ipYHx-XRda0p-Tl6K8zNZZl7LZQbTw5OkYVXB16DJE/edit?usp=sharing",
)
url_label = ttk.Label(root, text="Token:")
url_label.pack(padx=20, pady=5)

url_entry = ttk.Entry(root, width=150)
url_entry.pack(padx=20, pady=5)
url_entry.insert(
    0,
    "Please run socketxp in command prompt to get Public URL and paste here",
)
send_button = ttk.Button(root, text="Send Emails", command=send_emails, width=150)
send_button.pack(padx=20, pady=10)

tracking_button = ttk.Button(root, text="Tracking", command=tracking, width=150)
tracking_button.pack(padx=20, pady=5)

# Tạo và cấu hình ô hiển thị thông tin
info_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=150, height=100)
info_text.pack(padx=20, pady=10)
info_text.config(state=tk.DISABLED)  # Không cho phép chỉnh sửa nội dung

root.mainloop()
