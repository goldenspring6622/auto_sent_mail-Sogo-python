# auto_sent_mail-python
Ứng dụng đang được thử nghiệm trên Windows
Clone repo về.

auto sent mail write via python
Read carefully before use app.
Note: Program uses account Sogo to send email, so you need account Sogo to input in to email 
and password.
<h1>1. Get credential file:</h1>
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
<h1>2. Socketxp</h1>
- Register account at https://portal.socketxp.com<br>

![image](https://github.com/goldenspring6622/auto_sent_mail-Sogo-python/assets/79317931/fd675e09-51f8-4409-9d35-4e985b4369db)

- Click Auth Token, copy the code in Login Command like this :<br>
![image](https://github.com/goldenspring6622/auto_sent_mail-Sogo-python/assets/79317931/8ca639ed-7e19-4c74-bec5-3b0ce64c5cfc)

<br>
Using app socketxp.exe in this repo or download  at <a href="https://portal.socketxp.com/download/windows/amd64/socketxp.exe">socketxp.exe</a> 
<br>
Open command prompt, cd into socketxp.exe directory, for example app directory is <i>C:\Users\ADMIN\Documents\GitHub\auto_sent_mail-Sogo-python</i>, then type <code>cd C:\Users\ADMIN\Documents\GitHub\auto_sent_mail-Sogo-python</code> like this:<br> 
![image](https://github.com/goldenspring6622/auto_sent_mail-Sogo-python/assets/79317931/b41804c1-8663-4e23-983c-d0561c6ff223)

Type token then press Enter.
![image](https://github.com/goldenspring6622/auto_sent_mail-Sogo-python/assets/79317931/e7563b93-99d2-4730-b9b5-22df88294a2e)

Type <code>socketxp connect http://127.0.0.1:5000</code>. There should be a Public URL on your console, copy the URL. <strong>Dont shut the console down.</strong>
![image](https://github.com/goldenspring6622/auto_sent_mail-Sogo-python/assets/79317931/8df46d02-7b13-4b2d-bcaf-542416f4095d)

<h1>3. Usage</h1>

step 1: Click “Brower” to choose file credentials

![image](https://github.com/goldenspring6622/auto_sent_mail-Sogo-python/assets/79317931/a738f28a-62ed-413b-9fc7-e8c5dff86c2e)

Step 2: input all value email addresses, password, sheet URL, Public URL and click “Send Email” button.

![image](https://github.com/goldenspring6622/auto_sent_mail-Sogo-python/assets/79317931/e2313c85-d1d6-4470-ba1c-d05dec5b740d)


Step 3: wait a minute, email will be sent to and display result below box.

![image](https://github.com/goldenspring6622/auto_sent_mail-Sogo-python/assets/79317931/0e827dc7-d496-4501-826a-ed32b0e7b473)

 <br>Step 4: Click "Tracking", Attention : App and command prompt in part 1 must be running while tracking.<br>
If recipient open mail and mail server dont block pixel tracking, then the last column in the sheet of the mail's row will be "opened"
Then every time recipients in the sheet open the mail will be logged in file tracking_logs.txt.
