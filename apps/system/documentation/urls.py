from django.urls                        import path
from .technical_docs.views              import TechnicalDocView

app_name = 'documentation'

urlpatterns = [
    path('technical_doc/', TechnicalDocView.as_view(),  name='technical_doc'),
]
