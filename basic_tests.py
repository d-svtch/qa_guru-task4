from selene  import browser, command
import os
def test_full_complited_form():
    browser.open("/automation-practice-form")
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






