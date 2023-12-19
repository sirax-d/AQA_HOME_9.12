from selene.support.shared import browser
from selene import be, have, by
import os


file_path = os.path.join(os.environ['WORKSPACE'], "files/file.txt")

def test_demoqa_forms(setup_browser):
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Test_First_Name')
    browser.element('#lastName').type('Test_Last_Name')
    browser.element('#userEmail').type('test@email.com')
    browser.element('#gender-radio-3').double_click()
    browser.element('#userNumber').type('89879880990')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element(
        by.text('May')).click()
    browser.element('.react-datepicker__year-select').click().element(
        by.text('1990')).click()
    browser.element('.react-datepicker__day--021.react-datepicker__day--021').click()
    browser.element('#subjectsInput').click().type('Math')
    browser.element('.subjects-auto-complete__menu').element(by.text('Maths')).click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').set(file_path) \
        .should(have.attribute("value").value_containing("file.txt"))  # проверяем, что файл подгрузился
    browser.element('#currentAddress').type('Street Pirogovskaya 11-12')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Gurg').press_enter()
    browser.element('#submit').press_enter()
    browser.element('.modal-content').should(have.text('Thanks for submitting the form'))
    browser.element('.table').all('td').even.should(
        have.exact_texts('Test_First_Name Test_Last_Name', 'test@email.com', 'Other', '8987988099',\
                         '21 May,1990', 'Maths', 'Reading', 'file.txt', 'Street Pirogovskaya 11-12',\
                         'NCR Gurgaon'))
    browser.element('[id="closeLargeModal"]').click() # закрываем окно