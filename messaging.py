import smtplib
import ssl

import keys


# SSL context
context = ssl.create_default_context()


def send_email(
    recipient_email: str, 
    recipient_name: str = None, 
    subject: str = None,
    content: str = None,
    message: str = None
) -> None:
    """
    Sends an email to the recipient.

    You _must_ pass the recipient's email.
    Either pass in the full SMTP message via `message` or
    pass all three other parameters. One or the other, no
    in-betweens. If you pass `message` _and_ other parameters,
    those other parameters are ignored.
    """
    if message is None:
        message = "From: Secret Santa <allthingsdoozy@gmail.com\n" \
            f"To: {recipient_name.title()} <{recipient_email}>\n" \
            f"Subject: {subject}\n\n" + \
            content

    # Deliver
    with smtplib.SMTP_SSL(host=keys.Gmail.SMTP_HOST, port=keys.Gmail.SMTP_PORT, context=context) as server:
        server.login(
            user = keys.Gmail.SENDER,
            password = keys.Gmail.PASSWORD
        )
        server.sendmail(
            from_addr=keys.Gmail.SENDER,
            to_addrs=recipient_email,
            msg=message
        )
