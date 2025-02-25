from enum import Enum


class ElementRepositoryEN(Enum):
    # Landing Flow
    # Landing Page
    LOGIN_REMOTE_BUTTON = "com.pccw.nowotttv:id/tv_text"
    LANDING_TITLE_TEXT = "com.pccw.nowotttv:id/title"
    # Login AC&PW Page
    ID_TEXT_FIELD = "com.pccw.nowotttv:id/login_edit"
    ID_CONTINUE_BUTTON = "com.pccw.nowotttv:id/tv_text"
    PW_TEXT_FILED = "com.pccw.nowotttv:id/password_edit"
    PW_LOGIN_BUTTON = "com.pccw.nowotttv:id/tv_text"
    # MUP Page
    MUP_HELLO_TEXT = "com.pccw.nowotttv:id/profile_view_hello"
    MUP_PROFILE_ICON = "com.pccw.nowotttv:id/item_profile_txt"

    ###HKO - project
    #Landing
    #ID
    DISCLAIMER_TITLE = "hko.MyObservatory_v1_0:id/txt_title"
    AGREE_BUTTON = "hko.MyObservatory_v1_0:id/btn_agree"
    ANDROID_OK_BUTTON = "android:id/button1"
    LOCATION_ALLOW_PERMISSION_BUTTON = "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
    NOTIFICATION_ALLOW_BUTTON = "com.android.permissioncontroller:id/permission_allow_button"
    BANNER_NEXT_PAGE_BUTTON = "hko.MyObservatory_v1_0:id/exit_btn"
    #XPATH
    ANDROID_BACK_BUTTON = "//android.widget.ImageButton[@content-desc=\"Back\"]"

    #HOME
    #XPATH
    HOME_TITLE = "//android.widget.TextView[contains(@text, 'MyObservatory')]"
    #AID
    HOME_MENU_BUTTON = "Navigate up"

    #MENU
    #XPATH
    FORECAST_MENU_BUTTON = "//android.widget.TextView[contains(@text, 'Forecast & Warning Services')]"
    NINE_DAY_MENU_BUTTON = "//android.widget.TextView[contains(@text, '9-Day Forecast')][contains(@resource-id," \
                           "'hko.MyObservatory_v1_0:id/title')] "

    #9day Menu
    #XPATH
    FIRST_DAY_IN_NINE_DAY_FORECAST = "//android.widget.TextView[@content-desc="



