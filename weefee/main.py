# trunk-ignore(ruff/D415)
# trunk-ignore(ruff/D400)
"""
__main__.py
"""
import getpass
from wifi_qrcode_generator import wifi_qrcode


# trunk-ignore(ruff/D417)
def generate_weefee_qr(
    authentication_type: str, weefee_ssid: str, weefee_password: str, hidden: bool
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

    wifi_qrcode(
        authentication_type=authentication_type,
        hidden=hidden,
        password=weefee_password,
        ssid=weefee_ssid,
    )
    print("Generated WiFi QR code for SSID: " + weefee_ssid)


def main():
    AUTHENTICATION_TYPE = "WPA"
    HIDDEN = False
    ssid = getpass.getpass("Enter SSID: ")
    password = getpass.getpass("Enter password: ")
    generate_weefee_qr(AUTHENTICATION_TYPE, ssid, password, HIDDEN)


if __name__ == "__main__":  # pragma: no cover
    main()
