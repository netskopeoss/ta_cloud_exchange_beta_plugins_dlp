"""Microsoft File Share EDM Plugin Constants file."""

MICROSOFT_FILE_SHARE_EDM_FIELDS = {
    "SMB": [
        {
            "label": "Server IP/Hostname",
            "key": "smb_server_ip",
            "type": "text",
            "default": "",
            "mandatory": True,
            "placeholder": "e.g. 192.0.2.19/www.example.com",
            "description": (
                "IP address or Hostname of the Windows machine from which "
                "the CSV file should be pulled."
            ),
        },
        {
            "label": "Machine Name",
            "key": "smb_machine_name",
            "type": "text",
            "default": "",
            "mandatory": True,
            "placeholder": "e.g. WIN-131CUS090LI",
            "description": "NetBIOS machine name of the Windows server.",
        },
        {
            "label": "Username",
            "key": "smb_username",
            "type": "text",
            "default": "",
            "mandatory": True,
            "placeholder": "Username",
            "description": (
                "Username of the Windows machine which has read access "
                "to shared directory."
            ),
        },
        {
            "label": "Password",
            "key": "smb_password",
            "type": "password",
            "default": "",
            "mandatory": True,
            "placeholder": "Password",
            "description": "Password for the provided Windows username.",
        },
        {
            "label": "Shared Directory Name",
            "key": "smb_shared_directory_name",
            "type": "text",
            "default": "",
            "mandatory": True,
            "placeholder": "e.g. file_share_edm",
            "description": "Name of the Windows shared directory.",
        },
        {
            "label": "CSV File Path",
            "key": "smb_filepath",
            "type": "text",
            "default": "",
            "mandatory": True,
            "placeholder": "e.g. files-data\\netskope-data\\data.csv",
            "description": (
                "Path of the CSV file to be pulled from the configured Windows machine. "
                "This path must be relative to the shared directory."
            ),
            "helperText": "Note: Only .csv file with a maximum of 25 columns are supported."
        },
    ],
    "SFTP": [
        {
            "label": "Server IP/Hostname",
            "key": "sftp_server_ip",
            "type": "text",
            "default": "",
            "mandatory": True,
            "placeholder": "e.g. 192.0.2.19/www.example.com",
            "description": (
                "IP address or Hostname of the Windows machine "
                "from which the CSV file should be pulled."
            ),
        },
        {
            "label": "Username",
            "key": "sftp_username",
            "type": "text",
            "default": "",
            "mandatory": True,
            "placeholder": "Username",
            "description": (
                "Username of the Windows machine that is configured "
                "to use OpenSSH service on the machine."
            ),
        },
        {
            "label": "Password",
            "key": "sftp_password",
            "type": "password",
            "default": "",
            "mandatory": True,
            "placeholder": "Password",
            "description": "Password for the provided Windows username.",
        },
        {
            "label": "Port",
            "key": "sftp_port",
            "type": "number",
            "default": 22,
            "mandatory": True,
            "placeholder": "e.g. 22",
            "description": (
                "TCP port number to use for connecting to "
                "the OpenSSH service on the Windows machine."
            ),
        },
        {
            "label": "CSV File Path",
            "key": "sftp_filepath",
            "type": "text",
            "default": "",
            "mandatory": True,
            "placeholder": "e.g. C:\\Users\\Administrator\\files-data\\netskope-data\\data.csv",
            "description": "Path of the CSV file to be pulled from the configured Windows machine.",
            "helperText": "Note: Only .csv file with a maximum of 25 columns are supported."
        },
    ],
}
