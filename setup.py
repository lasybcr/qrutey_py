from setuptools import setup

setup(
    name="weefee",
    version="0.0.1",
    install_requires=[
        "wifi_qrcode_generator",
    ],
    entry_points={
        "console_scripts": [
            "qr_weefee = weefee.main:main",
        ]
    }
)
