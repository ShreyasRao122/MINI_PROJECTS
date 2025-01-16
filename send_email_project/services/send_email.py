import yagmail


def send_email(email, passwd, email_data, attach_path=""):
    if email and passwd and email_data.get("to"):
        yag = yagmail.SMTP(email, passwd)
        yag.send(
            to=email_data.get("to"),
            contents=email_data.get("contents", ""),
            subject=email_data.get("subject", ""),
            attachments=attach_path,
        )
