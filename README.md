# qa_guru_python_4_25_diplom_project_API

My diplom project, the 4 course automation testing with python at QA GURU school
https://jenkins.autotests.cloud/job/klimashko_%20qa_guru_python_4_25_diplom_project_API/
ссылка на сборку в Jenkins

# Проект автоматического тестирования сервиса бронирования гостиничных номеров Restful Booker Platform"

#### Created by Mark Winteringham / Richard Bradshaw

> <a target="_blank" href="https://automationintesting.online/">Restful Booker
> Platform</a>

## Проверяется функционал сервиса:

#### API автотесты

- [x] Проверка работоспособности, чтобы убедиться, что API запущен и работает.
- [x] Создание нового токена авторизации для доступа к обновлению или удалению
  бронирования.
- [x] Создание нового бронирования в API.
- [x] Возврат id всех бронирований, существующих в API.
- [x] Возврат конкретного бронирования.
- [x] Обновление бронирования.
- [x] Частичное обновление бронирования.
- [x] Удаление бронирования.

#### UI  автотесты

- [x] Отправка пользователем сообщения на главной странице сервиса.
- [x] Создание админом всех видов гостинничных номеров, отображение на главной
  странице.
- [x] Создание админом гостинничного номера, отображение на главной странице.

## Особенности тестов

Тест test_create_room параметризован, создается каждый вид гостиничного номера.

## Проект реализован с использованием

Python, PyCharm, Pytest, Selen, Jenkins, Selenoid, Allure Report, Allure TestOps, Jira,
Telegram, GitHub.
<p>
  <code><img width="5%" title="Python" src="resources/icons/python.png"></code>
  <code><img width="5%" title="Pycharm" src="resources/icons/pycharm.png"></code>
  <code><img width="5%" title="Pytest" src="resources/icons/pytest.png"></code>
  <code><img width="5%" title="Selene" src="resources/icons/selene.png"></code>
  <code><img width="5%" title="Jenkins" src="resources/icons/jenkins.png"></code>
  <code><img width="5%" title="selenoid" src="resources/icons/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="resources/icons/allure.png"></code>
  <code><img width="5%" title="Jira" src="resources/icons/jira.png"></code>
  <code><img width="5%" title="Telegram" src="resources/icons/tg.png"></code>
  <code><img width="5%" title="GitHub" src="resources/icons/github.png"></code>
</p>

## Локальный запуск автотестов

Запуск:

```bash
pytest tests
```

Получение отчёта:

```bash
allure serve allure-results
```

## Запуск автотестов c помощью [JOB в Jenkins](https://jenkins.autotests.cloud/job/Students/job/klimashko_%20qa_guru_python_4_25_diplom_project_API/)

## Нажать "Собрать с параметрами"

![Нажать "Собрать с параметрами"](resources/screens/collect_with_params.png)

## Указать какие тесты будут запущены, нажать кнопку Собрать

![Указать какие тесты будут запущены](resources/screens/select_tests_push_button_collect.png)

## Посмотреть выполнение прогона

![Посмотреть выполнение прогона](resources/screens/test_run_results.png)

## Посмотреть подробный отчет

![Посмотреть подробный отчет  API тестов](resources/screens/detail_report_api.png)

![Посмотреть подробный отчет  UI тестов](resources/screens/detail_report_ui.png)

[Ссылка](https://jenkins.autotests.cloud/job/StrelnikovaL_restful-booker/allure/)
Ссылка на Allure отчет API suites

[Ссылка](https://jenkins.autotests.cloud/job/StrelnikovaL_restful-booker/allure/)
Ссылка на Allure отчет UI suites

## Видео о прохождении теста
<a href="http://www.youtube.com/watch?feature=player_embedded&v=BuPl-mdW1Dw" target="_blank"><
img src="https://youtu.be/2mAulpJC9PA"
alt="Выполнение теста" width="240" height="180" border="10" /></a>

## Результаты выполнения тестов интегрированы с Allure TestOps

![Посмотреть dashboard_Allure_TestOps](resources/screens/dashboard_testops.png)

![Посмотреть launches_Allure_TestOps](resources/screens/launches_testops.png)

[Ссылка](https://allure.autotests.cloud/project/3428/dashboards)

## Результаты выполнения тестов интегрированы с Atlassian Jira
![Посмотреть задачу_в_Jira](resources/screens/jira_task.png)
> <a target="_blank" href="https://jira.autotests.cloud/browse/HOMEWORK-764">Ссылка на
> задачу в Jira</a> (запрос доступа admin@qa.guru)

# Настроено автоматическое уведомление о результатах сборки Jenkins в Telegram-бот

[Ссылка на Telegram-бот](https://t.me/+Ctoxu_5DqE1hNDEy)

<p>
  <code><img width="30%" title="Telegram-бот" src="resources/screens/bot.png"></code>
</p>
