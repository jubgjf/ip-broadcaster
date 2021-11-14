# ip-broadcaster

将内网 ip 发给邮箱

# 配置

配置文件为 `config.yaml`，以使用 outlook 进行发送为例：

```yaml
subject: "今日 ip 更新"                  # 邮件主题
content_file: "content.html"            # 邮件正文内容文件
sender:
  sender_host: "smtp.office365.com"     # 发送方邮件服务器
  sender_user: "my-email@outlook.com"   # 发送方用户名
  sender_passwd: "my-passwd"            # 发送方密码
  sender_email: "my-email@outlook.com"  # 发送方邮箱
receivers:
  recv-0@qq.com: "username-0"           # 接收方邮箱及其 ssh 用户名
  recv-1@outlook.com: "username-1"
  recv-2@stu.hit.edu.cn: "username-2"
```
