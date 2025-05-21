from django.urls import path
from .views import DashboardsView
from .views import PieCountbySeverity, LineCountByMonth, MultilineIncidentTop3Country, MultipleBarbySeverity


urlpatterns = [
    path('', DashboardsView.as_view(template_name="dashboard_analytics.html"), name="index"),
    path('dashboard/analytics/', DashboardsView.as_view(template_name="dashboard_analytics.html"), name='dashboard-chart'),
    path('pieChart/', PieCountbySeverity, name='chart'),
    path('lineChart/', LineCountByMonth, name='chart'),
    path('multiLineChart/', MultilineIncidentTop3Country, name='chart'),
    path('multiBarChart/', MultipleBarbySeverity, name='chart'),
]
