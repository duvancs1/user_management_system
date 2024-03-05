from django.urls                        import path
from .technical_docs.views              import TechnicalDocView
from .user_guide.views                  import UserGuideView

app_name = 'documentation'

urlpatterns = [
    path('technical_doc/', TechnicalDocView.as_view(),  name='technical_doc'),
    path('user_guide/',    UserGuideView.as_view(),  name='user_guide'),
]
