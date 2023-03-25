def makeHtml(notice):
    """
    Adds the notice details to the HTML email template.
    """

    # Include the Download Attachment button if the notice has any attachment
    attachment = ""
    if notice["attachment"]:
        attachment = f"""
        <a href="{notice["attachment"]}" style="color: inherit; text-decoration: inherit;">
            <div
                style="border-radius: 5px; background: #04AA6D; width: fit-content; color: white; padding: 10px 15px; margin-left: 3px;">
                <b>Download Attchment</b>
            </div>
        </a>"""

    # Assemble and return the HTML content
    return f"""
        <html>
        <head></head>

        <body style="font-family: Arial, Helvetica, sans-serif; margin: 0;">
            <table style="width: 100%; border-spacing: 3px; color: white;">
                <tr>
                    <td style="padding: 10px; border-radius: 5px; font-weight: bold; background: #218cce;">Date</td>
                    <td style="padding: 10px; border-radius: 5px; background: #009dff;">{notice["date"]}</td>
                </tr>
                <tr>
                    <td style="padding: 10px; border-radius: 5px; font-weight: bold; background: #218cce;">Posted by</td>
                    <td style="padding: 10px; border-radius: 5px; background: #009dff;">{notice["postedBy"]}</td>
                </tr>
                <tr>
                    <td style="padding: 10px; border-radius: 5px; font-weight: bold; background: #218cce;">For</td>
                    <td style="padding: 10px; border-radius: 5px; background: #009dff;">{notice["for"]}</td>
                </tr>
            </table>
            {attachment}
            <h2 style="margin: 20px 3px;">{notice["title"]}
            </h2>
            <div style="margin: 0 3px;">
                {notice["content"]}
            </div>
        </body>
        </html>"""
