from pages.buttons import Buttons
def test_buttons(browser):
    buttons = Buttons(browser)

    buttons.open()

    first_element = buttons.choose_click_button()
    first_element.click(browser)

    assert buttons.check_click() == 'You have done a dynamic click'

    second_element = buttons.choose_double_click_button()
    second_element.double_click(browser)

    assert buttons.check_double_click() == 'You have done a double click'

    third_element = buttons.choose_right_click_button()
    third_element.right_click(browser)

    assert  buttons.check_right_click() == 'You have done a right click'