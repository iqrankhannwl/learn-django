from django.urls import path
from .views import root, details, results, vote
urlpatterns = [
    path("", root, name="index"),
    path("<int:question_id>/", details, name="detail"),
    path("<int:question_id>/results/", results, name="results"),
    path("<int:question_id>/vote/", vote, name="vote"),
]