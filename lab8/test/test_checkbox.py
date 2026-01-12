from pages.checkbox import Checkbox
def test_checkbox(browser):
    checkbox = Checkbox(browser)
    checkbox.open()

    expand_button = checkbox.select_expand_button()
    expand_button.click(browser)

    checkbox.scroll_down()

    checkbox_button = checkbox.select_checkbox_button()
    checkbox_button.click(browser)

    assert checkbox.get_result() == 'public'
