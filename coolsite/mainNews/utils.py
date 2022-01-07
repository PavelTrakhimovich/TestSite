from django.db.models.aggregates import Count
from .models import Category




menu = [{'title':"About site", 'url_name': 'about'},
        {'title':"Add news", 'url_name': 'add_page'},
        {'title':"Feedback", 'url_name': 'contact'},
        {'title':"Sign In", 'url_name': 'login'},
        ]





class DataMixin:
    paginate_by = 3
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('news'))

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context