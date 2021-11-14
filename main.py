import ip
import time
import broadcaster
import yaml

if __name__ == "__main__":
    # 读取配置
    f = open("config.yaml")
    y = yaml.load(f, Loader=yaml.CLoader)

    # 发送方
    sender_host = y["sender"]["sender_host"]
    sender_user = y["sender"]["sender_user"]
    sender_passwd = y["sender"]["sender_passwd"]
    sender_email = y["sender"]["sender_email"]

    # 主题
    subject = y["subject"]
    # 正文
    with open(y["content_file"], "r") as f:
        raw_content = f.read()
    content = raw_content.replace("[[IP]]", ip.get_ip()).replace(
        "[[TIME]]", time.strftime("%Y年%m月%d日", time.localtime())
    )

    # 接收方
    receivers = y["receivers"]

    broadcaster.send_email(
        sender_host,
        sender_user,
        sender_passwd,
        sender_email,
        subject,
        content,
        receivers,
    )
