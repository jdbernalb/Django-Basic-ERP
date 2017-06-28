from polls.models import AnyModel
from model_report.report import reports, ReportAdmin

class AnyModelReport(ReportAdmin):
    title = _('AnyModel Report Name')
    model = Consumo
    fields = [
        'nombre_liquido',
    ]
    list_order_by = ('nombre_liquido',)
    type = 'report'

reports.register('anymodel-report', AnyModelReport)