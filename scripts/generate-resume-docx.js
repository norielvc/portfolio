const fs = require('fs');
const path = require('path');
const { buildResumeDocxBuffer } = require('../lib/resume-docx');

const out = path.join(__dirname, '..', 'resume.docx');

buildResumeDocxBuffer()
  .then((buffer) => {
    fs.writeFileSync(out, Buffer.from(buffer));
    console.log('Wrote', out, `(${buffer.length || buffer.byteLength} bytes)`);
  })
  .catch((err) => {
    console.error(err);
    process.exit(1);
  });
