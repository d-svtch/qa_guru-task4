from selene import browser, command, have
import os


def test_full_complited_form():
    browser.element("#firstName").type("Ivan")
    browser.element("#lastName").type("Ivanovich")
    browser.element("#userEmail").type("Ivanovich@testmail.com")
    browser.element('#gender-radio-1').perform(command.js.click())
    browser.element("#userNumber").type("7999999999")
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").click().element('[value="5"]').click()
    browser.element(".react-datepicker__year-select").click().element('[value="1999"]').click()
    browser.element(".react-datepicker__day--028").click()
    browser.element("#subjectsInput").click().type("Eng").press_enter()
    browser.element("#hobbies-checkbox-1").perform(command.js.click())
    browser.element("#hobbies-checkbox-2").perform(command.js.click())
    browser.element("#uploadPicture").send_keys(os.path.abspath("images.png"))
    browser.element("#currentAddress").type("Test adress, 11/1")
    browser.element("#state").click().element("#react-select-3-option-2").click()
    browser.element("#city").click().element("#react-select-4-option-1").click()
    browser.element("#submit").click()

    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
    browser.all("//div[@class='table-responsive']//td[2]").should(
        have.exact_texts('Ivan Ivanovich', 'Ivanovich@testmail.com', 'Male', '7999999999', '28 June,1999', 'English',
                         'Sports, Reading', 'images.png', 'Test adress, 11/1', 'Haryana Panipat'))


def test_only_required_data():
    browser.element("#firstName").type("Ivan")
    browser.element("#lastName").type("Ivanovich")
    browser.element('#gender-radio-1').perform(command.js.click())
    browser.element("#userNumber").type("7999999999")
    browser.element("#submit").click()

    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))


def test_required_data_not_filled():
    browser.element("#firstName").type("Ivan")
    browser.element("#userNumber").type("7999999999")
    browser.element("#submit").click()

    browser.element('#example-modal-sizes-title-lg').should(have.no.exact_text('Thanks for submitting the form'))
