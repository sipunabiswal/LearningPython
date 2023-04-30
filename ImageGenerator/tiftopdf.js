//code to convert tif to pdf
const { PDFDocumentFactory, PDFDocumentWriter } = require('pdf-lib');


// Read the TIF file as an Uint8Array.
const tifFileBytes = fs.readFileSync('input.tif');


// Create a new PDFDocument from the TIF file.
const pdfDoc = PDFDocumentFactory.load(tifFileBytes);


// Serialize the PDFDocument to bytes (a Uint8Array)
const pdfBytes = PDFDocumentWriter.saveToBytes(pdfDoc);


// Write the bytes to a file.
fs.writeFileSync('output.pdf', pdfBytes);

