""".
__main__.py  .
"""
import subprocess
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
    # TODO update print and return statements
    # print only if necessary
    # return an appropriate value
    # is return statement needed?
    print(f"Generated WiFi QR code for SSID: {weefee_ssid}")
    qrc.make_image().save(f"qr_{weefee_ssid}.png")

    return qrc.print_ascii()

def main():
    # Get current Wi-Fi name
    output = subprocess.check_output(["nmcli", "dev", "wifi"])
    output = output.splitlines()
    current_wifi = output[1].split()[1:3]
    current_wifi_joined = ' '.join([item.decode("utf-8") for item in current_wifi])

    print(current_wifi_joined)

    # Get Wi-Fi password
    output = subprocess.check_output(
        ["nmcli", "connection", "show", current_wifi_joined]
    )
    output = output.decode("utf-8").splitlines()
    password_line = next(
        (line for line in output if "802-11-wireless-security.psk" in line),
        None
    )
    if password_line is None:
        raise Exception("Password not found for Wi-Fi: " + current_wifi_joined)
    password = password_line.split(":")[1].strip()

    # Generate QR code for the current Wi-Fi
    generate_weefee_qr(weefee_ssid=current_wifi_joined, weefee_password=password)


if __name__ == "__main__":  # pragma: no cover
    main()
