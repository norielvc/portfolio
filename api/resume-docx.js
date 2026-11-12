const { buildResumeDocxBuffer } = require('../lib/resume-docx');

module.exports = async (req, res) => {
  if (req.method !== 'GET') {
    return res.status(405).send('Method not allowed');
  }

  try {
    const buffer = await buildResumeDocxBuffer();
    res.setHeader(
      'Content-Type',
      'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    );
    res.setHeader(
      'Content-Disposition',
      'attachment; filename="Nino_Noriel_V_Cruz_Resume.docx"'
    );
    res.send(Buffer.from(buffer));
  } catch (err) {
    console.error('resume.docx:', err);
    res.status(500).send('Could not generate Word document.');
  }
};
