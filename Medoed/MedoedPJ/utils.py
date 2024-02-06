points = [{"title":"Главная страница","url_name" : "Home"},
          {"title":"Продукты в наличие","url_name" : "info"},
          {"title":"Добавление статьи","url_name" : "add_prod"},
          {"title":"Связь с нами","url_name" : "contact"}
          ]



class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context["points"] = points
        return context