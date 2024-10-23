from typing import List
from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.response import Response

import pandas as pd
from openpyxl import Workbook
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

from corpsystem_teste.app.modules.sales.models import Sale


class SalesActions:

    def __export_to_xlsx(self, sales: List[Sale]) -> HttpResponse:
        df = pd.DataFrame(list(sales.values()))
        df.to_excel('sales.xlsx', index=False)
        return HttpResponse(open('sales.xlsx', 'rb'), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    
    def __export_to_pdf(self, sales: List[Sale]) -> HttpResponse:
        data = []
        for sale in sales:
            data.append([sale.id, sale.seller, sale.client, sale.product, sale.quantity, sale.total_price, sale.status, sale.created_at, sale.updated_at])

        doc = SimpleDocTemplate("sales.pdf", pagesize=letter)
        table = Table(data, colWidths=[50, 50, 50, 50, 50, 50, 50, 50, 50])
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 12),
        ])
        table.setStyle(style)
        doc.build([table])
        return HttpResponse(open('sales.pdf', 'rb'), content_type='application/pdf')
        

    @action(detail=True, methods=['GET'])
    def export(self, request, seller_id=None) -> HttpResponse:
        sales = Sale.objects.filter(seller_id=seller_id)
        if request.GET.get('format') == 'xlsx':
            return self.export_to_xlsx(sales)
        elif request.GET.get('format') == 'pdf':
            return self.export_to_pdf(sales)
        else:
            return HttpResponse('Format not supported')
        
        