## Описание

<p>В проекте реализована API и UI автоматизации тестирования на Python.
<p>При написании тестов применялись инструменты ООП, а также использовался шаблон 
<p>проектирования PageObjects.
<p>Подключена система отчетности Allure Reports с вложениями (логи, скриншоты, видео). 
<p>В тестах шаги размечены с помощью allure.step.
<p>Браузер в UI-тестах запускается удаленно в Selenoid.
<p>Реализованы интеграции с Allure TestOps и Jira.
<p>Уведомление о прохождения теста отправляется в Telegram.

# Проект автоматического тестирования сервиса бронирования гостиничных номеров Restful Booker Platform"

#### Created by Mark Winteringham / Richard Bradshaw

> <a target="_blank" href="https://automationintesting.online/">Restful Booker
> Platform</a>
>
> <a target="_blank" href="http://restful-booker.herokuapp.com/apidoc/index.html">API
> документация</a>

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

## Используемые технологии

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

Запуск api тестов:

```bash
pytest tests/api
```

Запуск ui тестов:

```bash
pytest tests/ui
```

Получение отчёта:

```bash
allure serve allure-results
```


## Запуск автотестов c помощью [job в Jenkins](https://jenkins.autotests.cloud/job/Students/job/klimashko_%20qa_guru_python_4_25_diplom_project_API_UI/)

## Нажать "Собрать с параметрами"

![Нажать "Собрать с параметрами"](resources/screens/collect_with_params.png)


## Указать какие тесты будут запущены, нажать кнопку Собрать

![Указать какие тесты будут запущены](resources/screens/select_tests_push_button_collect.png)


## Посмотреть выполнение прогона

### Ссылка 1 на скриншоте для Allure Report, ссылка 2 для Allure_TestOps.

![Посмотреть выполнение прогона](resources/screens/test_run_results.png)

## Отчет прохождения API тестов

![Allure Report о прхождении API тестов](resources/screens/detail_report_api.png)

[Сборка с прохождением API suites](https://jenkins.autotests.cloud/job/Students/job/klimashko_%20qa_guru_python_4_25_diplom_project_API_UI/66/allure/)


## Отчет прохождения UI тестов

![Allure Report о прхождении  UI тестов](resources/screens/detail_report_ui.png)

[Сборка с прохождением UI suites](https://jenkins.autotests.cloud/job/Students/job/klimashko_%20qa_guru_python_4_25_diplom_project_API_UI/61/allure/)


## Пример видео о прохождении UI теста

![This is an image](resources/screens/example_video.gif)


## Результаты выполнения тестов интегрированы с Allure TestOps

## Dashboard_Allure_TestOps

![Dashboard_Allure_TestOps](resources/screens/dashboard_testops.png)


## Launches_Allure_TestOps

![Launches_Allure_TestOps](resources/screens/launches_testops.png)

[Проект в Allure_TestOps](https://allure.autotests.cloud/project/3428/dashboards)


## Отчеты Allure TestOps интегрированы с Atlassian Jira

![Посмотреть задачу_в_Jira](resources/screens/jira_task.png)

[Задача в Jira](https://jira.autotests.cloud/browse/HOMEWORK-764)


## Настроено автоматическое уведомление о результатах сборки Jenkins в Telegram-бот

[Telegram-бот](https://t.me/+Ctoxu_5DqE1hNDEy)

<p>
  <code><img width="30%" title="Telegram-бот" src="resources/screens/bot.png"></code>
</p>
