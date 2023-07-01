""".
__main__.py  .
"""
import getpass
from wifi_qrcode_generator import wifi_qrcode


# trunk-ignore(ruff/D417)
def generate_weefee_qr(
    weefee_ssid: str, weefee_password: str, authentication_type="WPA", hidden=False
):
    """
    Generate a WiFi QR code for the given authentication type, SSID, password, and hidden status.

    Parameters
    ----------
    authentication_type: The type of authentication for the WiFi network.
    ssid: The SSID (network name) of the WiFi network.
    password: The password for the WiFi network.
    hidden: Indicates whether the WiFi network is hidden or not.

    Returns
    -------
    None
    """

    qrc = wifi_qrcode(
        authentication_type=authentication_type,
        hidden=hidden,
        password=weefee_password,
        ssid=weefee_ssid,
    )
    print("Generated WiFi QR code for SSID: " + weefee_ssid)
    qrc.make_image().save(f'qr_{weefee_ssid}.png')
    return qrc.print_ascii()


def main():
    ssid = getpass.getpass("Enter SSID: ")
    password = getpass.getpass("Enter password: ")
    generate_weefee_qr(weefee_ssid=ssid, weefee_password=password)

if __name__ == "__main__":  # pragma: no cover
    main()
