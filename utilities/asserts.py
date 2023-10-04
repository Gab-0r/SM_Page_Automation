

class Asserts:
    def is_page_visible(self, page, result):
        assert result, f"{page} is not displayed,"


    def was_element_found(self, element, result):
        assert result, f"{element} was not found."