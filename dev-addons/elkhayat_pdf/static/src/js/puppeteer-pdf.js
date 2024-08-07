// puppeteer-pdf.js
const puppeteer = require("puppeteer");

async function generatePdf(htmlContent, outputPath) {
  const browser = await puppeteer.launch({
    headless: true, // Run in headless mode
    args: ["--no-sandbox", "--disable-setuid-sandbox"], // Required for some environments
  });
  const page = await browser.newPage();

  // Set content
  await page.setContent(htmlContent, {
    waitUntil: "networkidle0", // Wait until there are no network connections for at least 500ms
  });

  // Set PDF options
  await page.pdf({
    path: outputPath,
    format: "A4",
    printBackground: true,
    margin: {
      top: "50px",
      right: "50px",
      bottom: "50px",
      left: "50px",
    },
  });

  await browser.close();
}

// Read command-line arguments
const htmlFilePath = process.argv[2];
const outputPath = process.argv[3];

// Read HTML file and generate PDF
const fs = require("fs");
fs.readFile(htmlFilePath, "utf8", (err, htmlContent) => {
  if (err) {
    console.error("Error reading HTML file:", err);
    return;
  }
  generatePdf(htmlContent, outputPath)
    .then(() => console.log("PDF generated successfully!"))
    .catch((err) => console.error("Error generating PDF:", err));
});
