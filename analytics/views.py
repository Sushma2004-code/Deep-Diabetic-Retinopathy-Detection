from django.shortcuts import render
from datasets.models import FundusImage
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta

def dashboard(request):
    total = FundusImage.objects.count()
    recent = FundusImage.objects.filter(uploaded_at__gte=timezone.now()-timedelta(days=30)).count()
    # group by day (simple)
    qs = FundusImage.objects.extra(select={'day':'date(uploaded_at)'}).values('day').annotate(c=Count('id')).order_by('day')[:30]
    chart_data = [{'day': r['day'].isoformat(), 'count': r['c']} for r in qs]
    return render(request, 'analytics/dashboard.html', {'total': total, 'recent': recent, 'chart_data': chart_data})
