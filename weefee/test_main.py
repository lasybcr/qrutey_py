import unittest
from unittest.mock import patch

from weefee.main import generate_weefee_qr, main


class TestGenerateWeefeeQR(unittest.TestCase):
    @patch("builtins.print")
    @patch("builtins.open")
    @patch(
        "weefee.main.wifi_qrcode"
    )  # Patch the wifi_qrcode function instead of QRCode
    def test_generate_weefee_qr(self, mock_wifi_qrcode, mock_open, mock_print):
        # Test normal case
        expected_output = "ASCII QR code"

        mock_qrcode_instance = mock_wifi_qrcode.return_value
        mock_qrcode_instance.print_ascii.return_value = expected_output

        generate_weefee_qr("MyWiFi", "password", "WPA", False)

        mock_wifi_qrcode.assert_called_with(
            authentication_type="WPA",
            hidden=False,
            password="password",
            ssid="MyWiFi",
        )
        mock_qrcode_instance.make_image.return_value.save.assert_called_with(
            "qr_MyWiFi.png"
        )

        self.assertEqual(mock_qrcode_instance.print_ascii.return_value, expected_output)
    @patch("weefee.main.subprocess.check_output")
    @patch("weefee.main.print")
    @patch("weefee.main.generate_weefee_qr")
    def test_main(self, mock_generate_weefee_qr, mock_print, mock_check_output):
        # Mock subprocess.check_output to return a known output
        mock_check_output.side_effect = [
            b"SSID          MODE             CHAN  RATE       SIGNAL  BARS  SECURITY\nMyWifi       Infra  36    270 Mbit/s  100     12345  WPA2  \n",
            b"connection.id:                MyWifi\n802-11-wireless-security.psk:  password123\n",
            b"",
        ]

        # Call the main function
        main()

        # Assert that the expected functions were called
        mock_generate_weefee_qr.assert_called_with(
            weefee_ssid="Infra 36", weefee_password="password123"
        )
        mock_print.assert_called_with("Infra 36")