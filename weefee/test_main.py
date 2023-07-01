import unittest
from unittest.mock import patch
from weefee.main import generate_weefee_qr, main


class TestGenerateWeefeeQR(unittest.TestCase):
    @patch("builtins.print")
    @patch("qrcode.make")
    @patch("qrcode.QRCode.print_ascii")
    def test_generate_weefe_qr(self, mock_print, mock_make, mock_print_ascii):
        # Test case 1: Testing with default authentication type, hidden status False
        generate_weefee_qr("MyWiFi", "password")
        mock_make.assert_called_with(
            authentication_type="WPA", hidden=False, password="password", ssid="MyWiFi"
        )
        mock_print.assert_called_with("Generated WiFi QR code for SSID: MyWiFi")
        mock_print_ascii.assert_called_once()
        mock_make.return_value.make_image.assert_called_once()
        mock_make.return_value.make_image.return_value.save.assert_called_with(
            "qr_MyWiFi.png"
        )

        # Test case 2: Testing with custom authentication type, hidden status True
        generate_weefee_qr(
            "MyWiFi", "password", authentication_type="WPA2", hidden=True
        )
        mock_make.assert_called_with(
            authentication_type="WPA2", hidden=True, password="password", ssid="MyWiFi"
        )
        mock_print.assert_called_with("Generated WiFi QR code for SSID: MyWiFi")
        mock_print_ascii.assert_called_with()
        mock_make.return_value.make_image.assert_called_with()
        mock_make.return_value.make_image.return_value.save.assert_called_with(
            "qr_MyWiFi.png"
        )

    @patch("builtins.print")
    @patch("qrcode.make")
    @patch("qrcode.QRCode.print_ascii")
    @patch("getpass.getpass", side_effect=["test_ssid", "test_password"])
    def test_generate_weefee_qr_valid(self, mock_getpass, mock_print_ascii, mock_make, mock_print):
        expected_qr_code = "expected_qr_code"
        generated_qr_code = generate_weefee_qr(
            weefee_ssid="test_ssid", weefee_password="test_password"
        )
        self.assertEqual(generated_qr_code, expected_qr_code)

    @patch("builtins.print")
    @patch("qrcode.make")
    @patch("qrcode.QRCode.print_ascii")
    def test_generate_weefee_qr_empty(self, mock_print_ascii, mock_make, mock_print):
        expected_qr_code = ""
        generated_qr_code = generate_weefee_qr(weefee_ssid="", weefee_password="")
        self.assertEqual(generated_qr_code, expected_qr_code)

    @patch("builtins.print")
    @patch("qrcode.make")
    @patch("qrcode.QRCode.print_ascii")
    @patch("getpass.getpass", side_effect=["test_ssid", ""])
    @patch("weefee.main.generate_weefee_qr")
    def test_generate_weefee_qr_empty_password(self, mock_generate_weefee_qr, mock_getpass, mock_print_ascii, mock_make, mock_print):
        expected_qr_code = "expected_qr_code_with_empty_password"
        main()
        generated_qr_code = mock_generate_weefee_qr(
            weefee_ssid="test_ssid", weefee_password=""
        )
        self.assertEqual(generated_qr_code, expected_qr_code)


if __name__ == "__main__":
    unittest.main()
