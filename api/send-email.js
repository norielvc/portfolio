const nodemailer = require('nodemailer');

module.exports = async (req, res) => {
  if (req.method !== 'POST') {
    return res.status(405).json({ success: false, error: 'Method not allowed' });
  }

  try {
    const { name, email, message } = req.body;

    const transporter = nodemailer.createTransport({
      service: 'gmail',
      auth: {
        user: process.env.GMAIL_USER,
        pass: process.env.GMAIL_PASS
      }
    });

    const mailOptions = {
      from: 'noriel.zurc@gmail.com',
      to: 'noriel.zurc@gmail.com',
      replyTo: email,
      subject: `Portfolio Contact: ${name}`,
      text: `Name: ${name}\nEmail: ${email}\n\nMessage:\n${message}`
    };

    const autoReplyHtml = `
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin:0;padding:0;background:#f4f4f5;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background:#f4f4f5;padding:40px 20px;">
    <tr>
      <td align="center">
        <table width="560" cellpadding="0" cellspacing="0" style="background:#ffffff;border-radius:12px;overflow:hidden;box-shadow:0 1px 3px rgba(0,0,0,0.08);">
          <tr>
            <td style="background:#111111;padding:32px 40px;text-align:center;">
              <h1 style="margin:0;color:#ffffff;font-size:22px;font-weight:700;letter-spacing:0.5px;">Noriel Cruz</h1>
              <p style="margin:6px 0 0;color:#888888;font-size:13px;letter-spacing:1px;text-transform:uppercase;">Full Stack Developer</p>
            </td>
          </tr>
          <tr>
            <td style="padding:40px;">
              <h2 style="margin:0 0 8px;color:#111111;font-size:20px;font-weight:700;">Hi ${name},</h2>
              <p style="margin:0 0 20px;color:#444444;font-size:15px;line-height:1.7;">
                Thank you for reaching out through my portfolio. I've received your message and will get back to you within 24 hours.
              </p>
              <div style="background:#f9f9f9;border-left:3px solid #111111;padding:16px 20px;margin:24px 0;border-radius:0 8px 8px 0;">
                <p style="margin:0 0 4px;color:#999999;font-size:12px;text-transform:uppercase;letter-spacing:1px;">Your message</p>
                <p style="margin:0;color:#333333;font-size:14px;line-height:1.6;font-style:italic;">${message}</p>
              </div>
              <p style="margin:24px 0 8px;color:#444444;font-size:15px;line-height:1.7;">
                Need a faster response? Reach me directly:
              </p>
              <table cellpadding="0" cellspacing="0" style="width:100%;margin:16px 0;">
                <tr>
                  <td style="padding:8px 0;">
                    <p style="margin:0;color:#999999;font-size:12px;text-transform:uppercase;letter-spacing:1px;">Email</p>
                    <p style="margin:2px 0 0;color:#111111;font-size:14px;font-weight:600;">noriel.zurc@gmail.com</p>
                  </td>
                </tr>
                <tr>
                  <td style="padding:8px 0;">
                    <p style="margin:0;color:#999999;font-size:12px;text-transform:uppercase;letter-spacing:1px;">Viber</p>
                    <p style="margin:2px 0 0;color:#111111;font-size:14px;font-weight:600;">+63 905 249 5512</p>
                  </td>
                </tr>
                <tr>
                  <td style="padding:8px 0;">
                    <p style="margin:0;color:#999999;font-size:12px;text-transform:uppercase;letter-spacing:1px;">Location</p>
                    <p style="margin:2px 0 0;color:#111111;font-size:14px;font-weight:600;">Calumpit, Bulacan & Quezon City, Philippines</p>
                  </td>
                </tr>
              </table>
              <p style="margin:32px 0 0;color:#444444;font-size:15px;line-height:1.7;">
                Looking forward to our conversation.
              </p>
              <p style="margin:8px 0 0;color:#111111;font-size:15px;font-weight:600;">
                Best regards,<br>Noriel Cruz
              </p>
            </td>
          </tr>
          <tr>
            <td style="background:#f9f9f9;padding:24px 40px;border-top:1px solid #eeeeee;text-align:center;">
              <p style="margin:0;color:#aaaaaa;font-size:12px;">This is an automated reply from norielcruz.com</p>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>`;

    const autoReply = {
      from: 'noriel.zurc@gmail.com',
      to: email,
      subject: 'Message Received — Noriel Cruz',
      html: autoReplyHtml,
      text: `Hi ${name},\n\nThank you for reaching out through my portfolio. I've received your message and will get back to you within 24 hours.\n\nNeed a faster response?\nEmail: noriel.zurc@gmail.com\nViber: +63 905 249 5512\n\nBest regards,\nNoriel Cruz`
    };

    await transporter.sendMail(mailOptions);
    transporter.sendMail(autoReply);

    return res.status(200).json({ success: true });
  } catch (err) {
    return res.status(500).json({ success: false, error: err.message });
  }
};
