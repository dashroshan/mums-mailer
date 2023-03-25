# IIIT-Bh MUMS Mailer

**Latest notices from M-UMS to college group emails**

<details>
<summary>View screenshot</summary>

---

![](/documentation/screenshot.jpg)

</details>

## Setup

Create a `config.json` file in the same directory as the `main.py` file with the below content:

```json
{
  "latestSentNotice": "",
  "loginId": "mums_id",
  "loginPass": "mums_password",
  "emailId": "email_id_of_sender",
  "emailPass": "password_of_sender",
  "toEmail": ["group1@iiit-bh.ac.in", "group2@iiit-bh.ac.in"]
}
```

Run below commands in the same directory as the `main.py` file:

```
python -m venv venv
pip install -r requirements.txt
python main.py
```
