{
    'name':'elkhayat PDF',
     'depends':['account','base', 'web'],
    'data':['report/elkhayat_pdf_report.xml','views/report_template.xml'],
    'assets': {
        'web.report_assets_common': [
            'elkhayat_pdf/static/src/css/styles.css',
        ],}
}