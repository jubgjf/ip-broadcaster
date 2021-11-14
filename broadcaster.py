import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send_email(
    sender_host: str,
    sender_user: str,
    sender_passwd: str,
    sender_email: str,
    subject: str,
    content: str,
    receivers: dict,
) -> None:
    """发送电子邮件

    Args:
        sender_host:   发送方邮件服务器
        sender_user:   发送方用户名
        sender_passwd: 发送方密码
        sender_email:  发送方邮箱
        subject:       邮件主题
        content:       邮件正文
        receivers:     接收者邮箱(key)及其 ssh 用户名(value)
    """

    for email in receivers.keys():
        new_content = content.replace("[[USERNAME]]", receivers[email])
        message = MIMEText(new_content, "html", "utf-8")
        message["Subject"] = Header(subject, "utf-8")

        try:
            smtp = smtplib.SMTP(sender_host)
            smtp.connect(sender_host, 587)
            smtp.ehlo()  # 用户认证
            smtp.starttls()  # TLS 加密
            smtp.login(sender_user, sender_passwd)
            smtp.sendmail(sender_email, email, message.as_string())
            smtp.close()
            print(">> Success: " + email)
        except smtplib.SMTPException:
            print(">> Error: " + email)
