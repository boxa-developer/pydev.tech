from .salary_views import *
from django.urls import path

urlpatterns = [
    # Config URLs
    path('config/set_base', set_base_salary),
    path('config/get_base', get_base_salary),

    # Account Urls
    path('account/add', add_account),  # method = post
    path('account/check', retrieve_accounts),  # method = post
    path('account/update', edit_account),  # method = put
    path('account/delete', delete_account),  # method = delete

    # Positions Urls
    path('position/add', add_position),  # method = post
    path('position/get_all', get_positions),  # method= get
    path('position/update', update_position),  # method = put
    path('position/delete', delete_position),  # method = delete

    # Bonuses Urls
    path('bonus/get_all', get_bonuses), # method = get
    path('bonus/add', add_bonus),  # method = post
    path('bonus/update', update_bonus),  # method = put
    path('bonus/delete', delete_bonus)  # method = delete
]
