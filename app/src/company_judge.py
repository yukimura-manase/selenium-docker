from selenium import webdriver
from selenium.webdriver.common.by import By
import traceback

### 作成・Module ########################################################

# 1. 電話番号(会社の代表番号: 固定電話)から、会社名を特定する

########################################################################

if __name__ == '__main__':
    print('seleniumTest Call')

    # 電話番号
    tell = '050-5581-6910'  # 楽天株式会社・Tell
    # tell = '0277-46-1111'  # 桐生市役所・Tell

    # 検索パラメーター付きの URL
    phone_number_search_web_url = f'https://www.jpnumber.com/searchnumber.do?number={tell}'
    print('検索パラメーター付きの URL')
    print(phone_number_search_web_url)

    # webdriver.Remote() で Selenium Container を指定して、接続する。
    browser = webdriver.Remote(
        command_executor="http://selenium:4444/wd/hub",
        options=webdriver.ChromeOptions()
    )

    # 会社名
    result = ''
    browser.get(phone_number_search_web_url)

    try:
        result_element = browser.find_element(By.XPATH, '//*[@id="result-main-right"]/div[2]/table/tbody/tr/td[1]/div/dt[2]/strong/a')
        result = result_element.text

    except Exception as error:
        # traceback.format_exc() で例外の詳細情報を取得する
        error_msg: str = traceback.format_exc()
        print(error_msg)
        # 例外を無視したい場合は、pass を使用する
        pass

    finally:
        # ブラウザを閉じる (エラーが発生しても必ず実行)
        browser.quit()

        print('--------------------------------------------------------------')
        print('電話番号・検索の結果から取得した会社名')
        print(result)
