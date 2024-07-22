{
    'name':'invoice PDF',
     'depends':['account'],
    'data':['report/custom_invoice_inherit.xml','views/report_template.xml'],
    'assets': {
        'web.report_assets_common': [
            'invoice_pdf/static/src/css/styles.css',
        ],}
}