from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """ Главная страница """

    template_name = 'logistics/home.html'

    # def get_context_data(self, **kwargs):
    #     """ Определяем контекстную информацию """
    #
    #     context = super().get_context_data(**kwargs)
    #
    #     questionnaires = Questionnaire.objects.filter(is_public=True)  # Получаем все опубликованные опросы
    #
    #     user = self.request.user  # получаем текущего пользователя
    #
    #     user_questionnaires = []  # задаем список опросов, в которых участвовал пользователь
    #
    #     try:
    #         user_answers = UserAnswer.objects.filter(user=user)  # Получаем все ответы пользователя в опросах
    #
    #         # получаем список опросов, в которых участвовал пользователь
    #         user_questionnaires = [user_answer.questionnaire for user_answer in user_answers]
    #
    #     except TypeError:
    #         pass
    #
    #     # если опубликованные опросы есть, выводим случайный опрос на главную страницу
    #     if len(questionnaires) >= 1:
    #         questionnaire_random = sample(list(questionnaires), 1)[0]  # Получаем 1 случайный опрос
    #
    #         context['questionnaire_random'] = questionnaire_random  # объект опрос
    #
    #         # если пользователь уже участвовал в опросе, задаем метку
    #         if questionnaire_random in user_questionnaires:
    #             context['questionnaire_done'] = True
    #
    #     return context
