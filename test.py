import gspread
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import scrolledtext 
from tkinter import messagebox 

def validate_inputs(json_file, email_address, password ,sheet_url):
    # Kiểm tra xem có ô nhập nào không được điền
    if not json_file or not email_address or not password or not sheet_url:
        messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin!")
        return False
    return True

def send_emails():
    try :
        # Tạo một chuỗi để lưu thông tin về email đã gửi
        sent_email_info = ""

        json_file = json_file_entry.get()
        email_address = email_address_entry.get()
        password = password_entry.get()
        sheet_url = sheet_url_entry.get()
        if not validate_inputs(json_file, email_address, password, sheet_url):
            return
        gc = gspread.service_account(filename=json_file)
        # sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1vY20VHnx5hHFjyF1P3ifHQH4TsC77TAkh--BOutUmoI/edit?usp=sharing')
        sh = gc.open_by_url(sheet_url)
        worksheet = sh.get_worksheet(0)
        data = worksheet.get_all_values()

        smtp_server = 'mail.qntdata.com'
        smtp_port = 587
        # email_address = 'ray.huynh@qt-globalgroup.com'
        # password = 'demo123'
        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_connection.starttls()
        smtp_connection.login(email_address, password)
    
        for row in data:
            recipient_email = row[0]
            subject = row[1]
            html_body = f"""
            <html>
                <body>
                    <p>Xin chào bạn</p>
                    <p>{row[2]}</p>
                    <p>Cảm ơn vì đã quan tâm </p>
                </body>
            </html>"""
            message = MIMEText(html_body, 'html')
            message['From'] = email_address
            message['To'] = recipient_email
            message['Subject'] = subject

            smtp_connection.sendmail(email_address, recipient_email, message.as_string())
            print('Email sent successfully')
            sent_email_info += f"Sent email to: {recipient_email}, Subject: {subject}\n"

        smtp_connection.quit()
        # Hiển thị thông tin về email đã gửi trong ô hiển thị
        info_text.config(state=tk.NORMAL)
        info_text.delete("1.0", tk.END)
        info_text.insert(tk.END, sent_email_info)
        info_text.config(state=tk.DISABLED)
        messagebox.showinfo("Thông báo", "Email đã được gửi thành công!")
    except smtplib.SMTPAuthenticationError:
        messagebox.showerror("Lỗi", "Lỗi xác thực SMTP: Vui lòng kiểm tra lại tên đăng nhập và mật khẩu.")
    except gspread.exceptions.APIError:
        messagebox.showerror("Lỗi", "Lỗi API Google Sheets: Vui lòng kiểm tra URL hoặc quyền truy cập.")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Có lỗi xảy ra khi gửi email: {str(e)}")
def browse_file():
    json_file = filedialog.askopenfilename()
    json_file_entry.delete(0, tk.END)
    json_file_entry.insert(0, json_file)

root = tk.Tk()
root.title("Send Emails")
root.geometry("400x600") 

json_file_label = ttk.Label(root, text="Credentials File: (*.Json)")
json_file_label.pack(padx=20, pady=5)

json_file_entry = ttk.Entry(root, width=150)
json_file_entry.pack(padx=20, pady=5)

browse_button = ttk.Button(root, text="Browse", command=browse_file, width=150)
browse_button.pack(padx=20, pady=5)

email_address_label = ttk.Label(root, text="Email Sent Address:")
email_address_label.pack(padx=20, pady=5)

email_address_entry = ttk.Entry(root, width=150)
email_address_entry.pack(padx=20, pady=5)

password_label = ttk.Label(root, text="Password:")
password_label.pack(padx=20, pady=5)

password_entry = ttk.Entry(root, show="*", width=150)  # Show asterisks for password entry
password_entry.pack(padx=20, pady=5)

sheet_url_label = ttk.Label(root, text="Sheet URL:")
sheet_url_label.pack(padx=20, pady=5)

sheet_url_entry = ttk.Entry(root, width=150)
sheet_url_entry.pack(padx=20, pady=5)

send_button = ttk.Button(root, text="Send Emails", command=send_emails, width=150)
send_button.pack(padx=20, pady=10)


# Tạo và cấu hình ô hiển thị thông tin
info_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=150, height=100)
info_text.pack(padx=20, pady=10)
info_text.config(state=tk.DISABLED)  # Không cho phép chỉnh sửa nội dung

root.mainloop()
