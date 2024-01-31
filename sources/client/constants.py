class Constants:
    MAIN_URL = 'https://qa-scooter.praktikum-services.ru'

    ENDPOINT_COURIER_CREATE = '/api/v1/courier'
    ENDPOINT_COURIER_LOGIN = '/api/v1/courier/login'
    ENDPOINT_ORDERS_CREATE_GET_LIST = '/api/v1/orders'
    ENDPOINT_ORDER_CANCEL = '/api/v1/orders/cancel'

    RESPONSE_SUCCESS = {'ok': True}
    ERROR_MESSAGE_CREATE_WITHOUT_REQUIRED_FIELD = 'Недостаточно данных для создания учетной записи'
    ERROR_MESSAGE_FOR_EXIST_LOGIN = 'Этот логин уже используется'
    ERROR_MESSAGE_FOR_UNCORRECT_LOGIN_PASSWORD = 'Учетная запись не найдена'
    ERROR_MESSAGE_LOGIN_WITHOUT_REQUIRED_FIELD = 'Недостаточно данных для входа'

    TEST_FIRSTNAME_CUSTOMER = 'Натали'
    TEST_LASTNAME_CUSTOMER = 'Бажова'
    TEST_ADDRESS_CUSTOMER = 'Попова, 2'
    TEST_METROSTATION_CUSTOMER = 4
    TEST_PHONENUMBER_CUSTOMER = '89261001010'
    TEST_RENTTIME_CUSTOMER = 5
    TEST_DELIVERYDATE_CUSTOMER = '2024-02-06'
    TEST_COMMENT_CUSTOMER = 'В дверь не звонить!'

    TEST_COLOR_BLACK = ['BLACK']
    TEST_COLOR_GRAY = ['GRAY']
    TEST_COLOR_BLACK_AND_GRAY = ['BLACK', 'GRAY']
    TEST_COLOR_NONE = []

    test_data_customer = [
        TEST_FIRSTNAME_CUSTOMER,
        TEST_LASTNAME_CUSTOMER,
        TEST_ADDRESS_CUSTOMER,
        TEST_METROSTATION_CUSTOMER,
        TEST_PHONENUMBER_CUSTOMER,
        TEST_RENTTIME_CUSTOMER,
        TEST_DELIVERYDATE_CUSTOMER,
        TEST_COMMENT_CUSTOMER,
    ]

    test_data_color = [
        TEST_COLOR_BLACK,
        TEST_COLOR_GRAY,
        TEST_COLOR_BLACK_AND_GRAY,
        TEST_COLOR_NONE,
    ]
