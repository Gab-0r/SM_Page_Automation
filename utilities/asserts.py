

class Asserts:
    @staticmethod
    def is_page_visible(self, page, result):
        assert result, f"{page} is not displayed,"

    @staticmethod
    def was_element_found(self, element, result):
        assert result, f"{element} was not found."

    @staticmethod
    def were_fields_filled(self, result):
        assert result, "fields were not filled."

    @staticmethod
    def was_form_submitted(self, result):
        assert result, "form was submitted."

    @staticmethod
    def was_message_displayed_correct(self, result):
        assert result, "message displayed is not the expected."

    @staticmethod
    def was_file_attached(self, result):
        assert result, "file was not attached successfully."


