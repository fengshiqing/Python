import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

sender = '938481169@qq.com' #发送人的邮箱
passWord = 'gykenxtteluibddf' #服务器授权码
# mail_host = 'smtp.qq.com' #服务器地址（这里是QQsmtp服务器）
receivers = ['938481169@qq.com','a938481169@163.com'] #receivers是邮件接收人，用列表保存，可以添加多个
msg = MIMEMultipart() #设置email信息
msg['Subject'] = input(f"{'请输入邮件主题：'}") #邮件主题
msg['From'] = sender #发送方信息
msg_content = input(f"{'请输入邮件内容:'}") #邮件正文是 MIMEText
msg.attach(MIMEText(msg_content, 'plain', 'utf-8'))
with open('D:/kunning/桌面/好身材.jpg', 'rb') as f: # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
    mime = MIMEBase('image', 'jpg', filename='fsq.png')# 设置附件的MIME和文件名，这里是jpg类型,可以换png或其他类型:
    mime.add_header('Content-Disposition', 'attachment', filename='fsq.png') # 加上必要的头信息
    mime.add_header('Content-ID', '<0>') # 加上必要的头信息
    mime.add_header('X-Attachment-Id', '0') # 加上必要的头信息
    mime.set_payload(f.read()) # 把附件的内容读进来
    encoders.encode_base64(mime) # 用Base64编码
    msg.attach(mime) # 添加到 MIMEMultipart

try:
    s = smtplib.SMTP_SSL("smtp.qq.com") #QQsmtp服务器的端口号为465或587，这里加了端口号反而连接不成功
    s.set_debuglevel(1)
    s.login(sender,passWord) #登录
    for i in range(len(receivers)): #给receivers列表中的联系人逐个发送邮件
        to = receivers[i]
        msg['To'] = to
        s.sendmail(sender,to,msg.as_string()) #发送邮件
        print('Success!')
    s.quit()
    print ("所有邮件已经发送成功!")
except smtplib.SMTPException as e:
    print ("【发送邮件时】【发生异常：】",e)
