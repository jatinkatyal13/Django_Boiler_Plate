from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('', index, name = 'index'),
    path('feedback', feedback, name = 'feedback'),
    path('feedback_edit/<int:pk>', feedback_edit, name = 'feedback_edit'),
    path('success', TemplateView.as_view(template_name = 'form_learn/success.html'), name = 'success'),

    path('generic/form_view', GenericFormView.as_view()),
    path('generic/create_view', GenericAddView.as_view()),
    path('generic/update_view/<int:pk>', GenericUpdateView.as_view()),
    path('generic/delete_view/<int:pk>', GenericDeleteView.as_view()),
]
