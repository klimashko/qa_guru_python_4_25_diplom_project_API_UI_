# qa_guru_python_4_25_diplom_project_API
My diplom project, the 4 course automation testing with python at QA GURU school
https://jenkins.autotests.cloud/job/klimashko_%20qa_guru_python_4_25_diplom_project_API/
ссылка на сборку в Jenkins

# Проект автоматического тестирования сервиса бронирования номеров Restful Booker Platform"
> <a target="_blank" href="https://automationintesting.online/">Created by Mark Winteringham / Richard Bradshaw</a>


## Проверяется следующий функционал сервиса:
#### API автотесты
- [x] Проверка работоспособности, чтобы убедиться, что API запущен и работает.
- [x] Создание нового токена авторизации для доступа к обновлению или удалению бронирования.
- [x] Создание нового бронирования в API.
- [x] Возврат id всех бронирований, существующих в API.
- [x] Возврат конкретного бронирования.
- [x] Обновление бронирования.
- [x] Частичное обновление бронирования.
- [x] Удаление бронирования.
#### UI  автотесты
- [x] Отправка пользователем сообщения на главной странице сервиса.
- [x] Создание админом всех видов гостинничных номеров, отображение их на главной странице.
- [x] Создание админом гостинничного номера, отображение его на главной странице.

## Особенности тестов
Тест test_create_room параметризован, таким образом тест создается каждый вид гостинничного номера.

## Проект реализован с использованием
Python PyCharm Pytest Selen Jenkins Selenoid Allure Report Allure TestOps Jira Telegram GitHub
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

# Запуск автотестов выполняется на сервере Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/......./">Ссылка на проект в Jenkins</a>



### Для запуска автотестов в Jenkins
#### 1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/09-ElenaSeversk-unit13/">проект</a>

![This is an image](/design/images/jenkins1.png)

#### 2. Выбрать пункт **Собрать с параметрами**
#### 3. В случае необходимости изменить параметры, выбрав значения из выпадающих списков
#### 4. Нажать **Собрать**
#### 5. Результат запуска сборки можно посмотреть в отчёте Allure

![This is an image](/design/images/jenkins2a.png)

## Локальный запуск автотестов
Пример командной строки:
```
pytest tests
```

Получение отчёта:
```
allure serve allure-results
```

# Полная статистика по прохождению тестпланов, отчёты и приложения к ним хранятся в Allure TestOps
> <a target="_blank" href="https://allure.autotests.cloud/....../">Сссылка на проект в AllureTestOps</a> (запрос доступа admin@qa.guru)

### Тест-планы проекта
![This is an image](/design/images/testplans.png)

### Пример видеозаписи прохождения теста
![This is an image](/design/images/Video.gif)




# Результаты выполнения тестов интегрированы с Atlassian Jira
> <a target="_blank" href="https://jira.autotests.cloud/browse/HOMEWORK-764">Ссылка на задачу в Jira</a> (запрос доступа admin@qa.guru)





# Настроено автоматическое оповещение о результатах сборки Jenkins в Telegram-бот
![This is an image](/design/images/bot.png)