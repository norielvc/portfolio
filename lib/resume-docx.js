const fs = require('fs');
const path = require('path');
const cheerio = require('cheerio');
const HTMLtoDOCX = require('html-to-docx');

const ACCENT = '#1e3a5f';
const BRASS = '#a68456';
const SIDEBAR_BG = '#f3f5f8';
const BORDER = '#e2e6ec';
const TEXT = '#1a2332';
const MUTED = '#6b7585';

const WORD_CSS = `
  body { font-family: Calibri, Arial, sans-serif; font-size: 11pt; color: ${TEXT}; line-height: 1.45; margin: 0; }
  .page { page-break-after: always; margin: 0 0 14pt; }
  .page:last-child { page-break-after: auto; }
  h1 { color: ${ACCENT}; font-size: 20pt; margin: 0 0 6pt; }
  h2 { color: ${ACCENT}; font-size: 14pt; margin: 0 0 6pt; }
  h3 { color: ${ACCENT}; font-size: 11pt; margin: 0 0 4pt; }
  .name-kicker { font-size: 9pt; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: ${BRASS}; }
  .role-title { font-size: 10pt; color: #3d4756; border-left: 2pt solid ${BRASS}; padding-left: 6pt; margin: 6pt 0 0; }
  .s-title, .m-title {
    font-size: 9pt; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em;
    color: ${ACCENT}; border-bottom: 1pt solid ${BRASS}; padding-bottom: 3pt; margin: 10pt 0 6pt;
  }
  .c-lbl { display: block; font-size: 8pt; color: #8a93a3; text-transform: uppercase; }
  .c-val { display: block; font-size: 10pt; margin-bottom: 5pt; }
  .c-val a { color: ${ACCENT}; text-decoration: none; font-weight: 600; }
  .link-chips { margin-top: 4pt; }
  .link-chip {
    display: inline-block;
    font-size: 8.5pt;
    font-weight: 600;
    padding: 2pt 5pt;
    background: ${ACCENT};
    color: #fff;
    text-decoration: none;
    margin: 0 3pt 3pt 0;
  }
  .tag-sublabel { font-size: 8pt; font-weight: 700; color: ${BRASS}; text-transform: uppercase; width: 100%; margin: 4pt 0 2pt; }
  ul { margin: 4pt 0 8pt 14pt; padding: 0; }
  li { margin-bottom: 3pt; font-size: 10pt; }
  .tag { display: inline-block; font-size: 8.5pt; border: 1pt solid ${ACCENT}; color: ${ACCENT}; padding: 2pt 5pt; margin: 0 3pt 3pt 0; border-radius: 2pt; }
  .exp-role { font-weight: 700; color: ${ACCENT}; font-size: 11pt; }
  .exp-date { font-size: 9.5pt; color: ${BRASS}; font-weight: 600; }
  .exp-company { font-size: 10pt; color: #3d4756; margin: 2pt 0 4pt; }
  .exp-item { margin-bottom: 10pt; padding-bottom: 8pt; border-bottom: 0.5pt solid ${BORDER}; }
  .profile-pillar { margin: 0 0 8pt; }
  .profile-pillar h3 { color: ${ACCENT}; font-size: 11pt; margin: 0 0 2pt; }
  .profile-pillar p { font-size: 10pt; margin: 0; }
  .exp-start { margin-top: 20pt; }
  .page-2-header p { font-size: 10pt; color: ${MUTED}; margin: 0 0 8pt; }
  .project-table { width: 100%; border-collapse: collapse; margin-top: 6pt; }
  .project-table td { vertical-align: top; padding: 6pt 8pt 6pt 0; font-size: 10pt; border-bottom: 0.5pt solid ${BORDER}; }
  .project-table td:first-child { width: 22%; font-weight: 600; color: ${ACCENT}; }
  .proj-link { display: block; font-size: 8.5pt; color: ${MUTED}; font-weight: 400; }
  .proj-meta { font-size: 9pt; color: ${BRASS}; font-weight: 600; margin-bottom: 3pt; }
  .proj-stack { font-size: 8.5pt; color: ${MUTED}; margin-top: 4pt; }
  .cv-footer { font-size: 8.5pt; color: ${MUTED}; margin-top: 10pt; border-top: 0.5pt solid ${BORDER}; padding-top: 5pt; }
  .how-i-work { margin-top: 12pt; border-top: 0.5pt solid ${BORDER}; padding-top: 8pt; }
  .edu-sidebar { margin-top: 8pt; padding-top: 6pt; border-top: 0.5pt solid #d5dbe3; }
  .edu-sidebar .edu-degree { font-weight: 700; color: ${ACCENT}; }
  .edu-sidebar .edu-meta { color: #3d4756; }
  .how-i-work h2 { color: ${ACCENT}; font-size: 13pt; margin: 0 0 6pt; }
  .how-i-work li { margin-bottom: 3pt; }
  a { color: ${ACCENT}; }
`;

function prepareResumeHtml() {
  const html = fs.readFileSync(path.join(__dirname, '..', 'resume.html'), 'utf8');
  const $ = cheerio.load(html, { decodeEntities: false });

  $('.download-bar, .print-hint, script').remove();
  $('.print-skip').remove();
  $('.portfolio-invite').remove();

  $('.page-inner').each((_, el) => {
    const inner = $(el);
    const sidebar = inner.children('.sidebar');
    const main = inner.children('.main');
    if (sidebar.length && main.length) {
      inner.empty().append(sidebar).append(main);
    }
  });

  $('.exp-head').each((_, el) => {
    const head = $(el);
    const role = head.find('.exp-role').html() || '';
    const date = head.find('.exp-date').html() || '';
    head.replaceWith(
      `<p class="exp-head"><span class="exp-role">${role}</span> <span class="exp-date">${date}</span></p>`
    );
  });

  $('.proj-grid').each((_, el) => {
    const grid = $(el);
    const blocks = grid.children('.proj-block');
    grid.replaceWith(`<div class="proj-grid">${blocks.toArray().map((b) => $.html(b)).join('')}</div>`);
  });

  $('[style*="var(--"]').each((_, node) => {
    const $n = $(node);
    let style = $n.attr('style') || '';
    style = style
      .replace(/var\(--border\)/g, BORDER)
      .replace(/var\(--accent\)/g, ACCENT)
      .replace(/var\(--brass\)/g, BRASS);
    $n.attr('style', style);
  });

  $('.page').each((_, el) => {
    const page = $(el);
    const footer = page.children('.cv-footer');
    const sheet = page.children('.page-sheet');
    const footerHtml = footer.length ? footer.clone() : null;
    const content = sheet.length ? sheet.html() : '';
    page.attr('class', 'page');
    page.empty();
    if (content) page.append(content);
    if (footerHtml && footerHtml.length) page.append(footerHtml);
  });

  $('.cv-footer').each((_, el) => {
    const foot = $(el);
    const spans = foot.children('span').toArray();
    if (spans.length >= 3) {
      foot.replaceWith(
        `<table class="cv-footer" style="border-collapse:collapse;">
          <tr>
            <td>${$(spans[0]).html()}</td>
            <td style="text-align:center;">${$(spans[1]).html()}</td>
            <td style="text-align:right;">${$(spans[2]).html()}</td>
          </tr>
        </table>`
      );
    }
  });

  $('aside').each((_, el) => {
    const $a = $(el);
    $a.replaceWith(`<div class="sidebar">${$a.html()}</div>`);
  });

  let body = '';
  $('.page').each((_, el) => {
    body += $.html(el);
  });

  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<style>${WORD_CSS}</style>
</head>
<body>
${body}
</body>
</html>`;
}

async function buildResumeDocxBuffer() {
  const html = prepareResumeHtml();
  const buffer = await HTMLtoDOCX(html, null, {
    title: 'Niño Noriel V. Cruz — Resume',
    font: 'Calibri',
    fontSize: 22,
    margin: {
      top: 720,
      right: 720,
      bottom: 720,
      left: 720,
    },
    table: { row: { cantSplit: false } },
    footer: false,
    pageNumber: false,
  });
  return buffer;
}

module.exports = { buildResumeDocxBuffer, prepareResumeHtml };
