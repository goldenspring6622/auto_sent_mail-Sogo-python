![image](https://github.com/goldenspring6622/auto_sent_mail-Sogo-python/assets/79317931/071a0a93-9119-4649-be3d-69cc04915681)# auto_sent_mail-python
Ứng dụng đang được thử nghiệm trên Windows
Clone repo về.

auto sent mail write via python
Read carefully before use app.
Note: Program uses account Sogo to send email, so you need account Sogo to input in to email 
and password.
1. How to get credential file:
Credentials, for detail, can see post via link :”https://developers.google.com/workspace/guides/create-credentials”
Detail:
Go to google cloud console, login with account google and create new project in here.

![image](https://github.com/botsamqntdata/auto_sent_mail-python/assets/128407982/47f47af8-6937-467a-b475-20beee0b28ca)

Go to dashboard, after that click API library, search for Google Sheet API and Enable.

![image](https://github.com/botsamqntdata/auto_sent_mail-python/assets/128407982/6dc8f04b-3a14-48a7-aeab-7954226baeac)

Return to dashboard, choose Credentials , create new service account and click it .
Select Tab Key -> Add key -> New Key-> JSON -> create .

![image](https://github.com/botsamqntdata/auto_sent_mail-python/assets/128407982/9f3008f5-c405-4b2f-a98c-0a3b51fe297b)

After that download this file.
Phần 1 : Socketxp
Sử dụng app socketxp.exe có sẵn trong repo hoặc download socketxp.exe tại https://portal.socketxp.com/download/windows/amd64/socketxp.exe và paste vào directory của repo <br>
Đăng ký tài khoản tại https://portal.socketxp.com, sau đó truy cập Auth Token https://portal.socketxp.com/#/basicauthtoken, lấy token trong phần Login Command, có dạng như sau :<br>
<code>socketxp login eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjI2NTIxMzEzMjAsImtleSI6IjM2MzY2YmEzLTZhYzktNDM2ZC1iYjE5LWNmMmQ5Y2QxNmNjMCJ9.xL_JqhQUwgn3L328jlThs8GkRHtgV_98kGWi0gEWz2</code><br>
Mở command prompt, cd vào directory của repository, nhập hết token vừa lấy vào rồi nhấn Enter. Sau đó nhập tiếp socketxp connect http://127.0.0.1:5000. Màn hình hiện ra dòng Public URL cùng với một URL. Cứ để cho command prompt chạy và chuyển sang phần 2.
<br>Phần 2 : Sử dụng app
<br>Click tiếp Tracking. Lưu ý : App và command prompt ở phần 1 sẽ chạy trong suốt quá trình tracking.
<br>Nếu người nhận mở mail và mail không bị chặn pixel tracking, request sẽ gửi về và được ghi vào tracking_logs.txt.
2.	How to run file
step 1: Click “Brower” to choose file credentials

![image](https://github.com/botsamqntdata/auto_sent_mail-python/assets/128407982/1549ad54-d98a-4782-b767-19e74152d131)

Step 2: input all value email addresses, password, sheet URL and click “Send Email” button.

![image](https://github.com/botsamqntdata/auto_sent_mail-python/assets/128407982/1263fa13-0e57-4ebc-8d71-68b0b261d150)

Step 3: wait a minute, email will be sent to and display result below box.

![image](https://github.com/botsamqntdata/auto_sent_mail-python/assets/128407982/a8d0ed13-95c6-4c87-9493-58d55f5fcb37)
