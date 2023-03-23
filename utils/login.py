from headers import headers


def login(session, id, password):
    """
    Login to M-UMS using the provided requests session with the given login id and password.
    Returns True if the login attempt was successful.
    """

    req = session.post(
        "https://hib.iiit-bh.ac.in/m-ums-2.0/start/login/auth.php?client=iiit",
        data={
            "uid": id,
            "pwd": password,
            "txtInput": 10,  # Any random value as the captcha is only verified on frontend
        },
        headers={
            "Referer": "https://hib.iiit-bh.ac.in/m-ums-2.0/start/login/?client=iiit",
            **headers,
        },
    )

    # Return True if succesfully logged in
    return (
        req.url
        != "https://hib.iiit-bh.ac.in/m-ums-2.0/start/login/?client=iiit&mes=UserID_or_Password_Incorrect"
    )
