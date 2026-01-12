from pages.testbox import TextBox
def test_select_post(browser):
    name = 'ivan'
    email = 'ageasrg@sdgsdg.ru'
    current_address = 'sdghsgsdgsd'
    permanent_address = 'asgshnfghfdh'

    data_list = [name, email, current_address, permanent_address]

    text_box = TextBox(browser)
    text_box.open()
    text_box.scroll_down()

    name_field = text_box.select_input_field_name()
    name_field.click(browser)
    name_field.insert_value(name)

    email_field = text_box.select_input_field_email()
    email_field.click(browser)
    email_field.insert_value(email)

    current_address_field = text_box.select_input_field_current_address()
    current_address_field.click(browser)
    current_address_field.insert_value(current_address)

    permanent_address_field = text_box.select_input_permanent_address()
    permanent_address_field.click(browser)
    permanent_address_field.insert_value(permanent_address)

    submit_button = text_box.select_submit_button()
    submit_button.click(browser)

    check_data_list = text_box.get_result()

    for i in range(len(data_list)):
        assert check_data_list[i] == data_list[i]