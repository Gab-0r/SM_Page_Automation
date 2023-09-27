from selenium.webdriver import Chrome

class WebDriverManager:
    def __init__(self, driver_name: str):
        self.driver_name = driver_name

    def create_driver(self) -> Chrome:
        if self.driver_name == "Chrome":
            return Chrome()