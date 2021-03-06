from django.urls import path
from .views import ApiWhiteList, ApiWhiteListEntry, ServiseAuth, UsersAuthorization, UserSessions, UserRegistration, AccountManagement 

urlpatterns = [
    path('lists/', ApiWhiteList.as_view()),
    path('list/<uuid:uuid>', ApiWhiteListEntry.as_view()),

    path('services/', ServiseAuth.as_view()),
    
    path('accounts/', AccountManagement.as_view()),

    path('registration/', UserRegistration.as_view()),

    path('authorization/', UsersAuthorization.as_view()),

    path('sessions/', UserSessions.as_view()),
]
