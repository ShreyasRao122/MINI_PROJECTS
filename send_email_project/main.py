from MINI_PROJECTS.send_email_project.settings import EMAIL_DATA_JSON_PATH, EMAIL, PASSWORD, ATTACHMENT_PATH
from services.generate_email_details import generate_email_details
from services.send_email import send_email

if __name__ == "__main__":
    data = generate_email_details(EMAIL_DATA_JSON_PATH)
    send_email(
        EMAIL,
        PASSWORD,
        data,
        attach_path=ATTACHMENT_PATH,
    )
