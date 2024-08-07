from odoo import models, api
import subprocess
import os
import tempfile

class ReportPuppeteer(models.AbstractModel):
    _name = 'report.custom_report_puppeteer.report_template'

    @api.model
    def _render_qweb_pdf(self, report_ref, docids, data=None):
        # Fetch the report content using the usual qweb rendering
        report = self.env['ir.actions.report']._get_report_from_name(report_ref)
        html = report.render_qweb_html(docids, data=data)[0]

        # Create temporary files for HTML and PDF
        with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as html_file, \
             tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as pdf_file:
            
            html_file.write(html.encode('utf-8'))
            html_file.flush()
            pdf_file_path = pdf_file.name

            # Call Puppeteer to generate PDF
            script_path = os.path.join(os.path.dirname(__file__), '../static/src/js/puppeteer-pdf.js')
            subprocess.run(['node', script_path, html_file.name, pdf_file_path], check=True)

            # Read the generated PDF
            with open(pdf_file_path, 'rb') as pdf_file:
                pdf_content = pdf_file.read()

        # Clean up temporary files
        os.unlink(html_file.name)
        os.unlink(pdf_file_path)

        return pdf_content, 'pdf'
