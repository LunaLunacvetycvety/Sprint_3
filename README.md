test_registration.py - тесты с регистрацией:
test_registration_success - успешная регистрация ,
test_registration_password_error - ошибка для некорректного пароля;

test_auth.py - тесты на авторизацию :
(так как форма авторизации подгружается одна и та же,
то в первом тесте проверяю авторизацию, а дальше проверяю переходы к этой форме)
test_main_auth_from_account_success - вход через кнопку «Личный кабинет»,
test_main_auth_success - переход вход по кнопке «Войти в аккаунт» на главной,
test_auth_from_reg_success-вход через кнопку в форме регистрации,
test_auth_from_recovery_password_success-вход через кнопку в форме восстановления пароля;

test_account_transit.py - тесты перехода в личный кабинет :
test_auth_main_screen_success - переход в личный кабинет по клику на «Личный кабинет»;

test_transit_to_constructor.py - тесты перехода из личного кабинета в конструктор:
test_transit_to_constructor_from_button_success - переход по клику на кнопку «Конструктор» ,
test_transit_to_constructor_from_logo_success -  переход по клику на логотип Stellar Burgers;

test_logout.py - выход из аккаунта:
test_logout_success - успешный выход по кнопке «Выйти» в личном кабинете;

test_constructor.py - тесты перехода к подразделам Конструктора:
test_transit_to_bread_success - успешный переход к разделу «Булки», «Начинки».
test_transit_to_sauces_success - успешный переход к разделу «Соусы»,
test_transit_to_filling_success - успешный переход к разделу «Начинки»;

locators.py - описаны локаторы для используемых в тестах элементов;

conftest.py - описание фикстур;
