from selene.support.shared import browser
from selene import be, have, by
import os


def test_demoqa_forms(start_settings_google):
    browser.open('/automation-practice-form')
    browser.element('[id="firstName"]').type('Test_First_Name')
    browser.element('[id="lastName"]').type('Test_Last_Name')
    browser.element('[id="userEmail"]').type('test@email.com')
    browser.element('#gender-radio-3').double_click()
    browser.element('#userNumber').type('89879880990')
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('.react-datepicker__month-select').click().element(
        by.text('May')).click()
    browser.element('.react-datepicker__year-select').click().element(
        by.text('1990')).click()
    browser.element('.react-datepicker__day--021.react-datepicker__day--021').click()
    browser.element('#subjectsInput').click().type('Math')
    browser.element('.subjects-auto-complete__menu').element(by.text('Maths')).click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[id="uploadPicture"]').set(os.path.abspath("file.txt")) \
        .should(have.attribute("value").value_containing("file.txt"))  # проверяем, что файл подгрузился
    browser.element('[id="currentAddress"]').type('Street Pirogovskaya 11-12')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Gurg').press_enter()
    browser.element('[id="submit"]').press_enter()
    browser.element('.modal-content').should(have.text('Thanks for submitting the form'))
    browser.element('.modal-body').should(have.exact_text(
        'Label Values\n'
        'Student Name Test_First_Name Test_Last_Name\n'
        'Student Email test@email.com\n'
        'Gender Other\n'
        'Mobile 8987988099\n'
        'Date of Birth 21 May,1990\n'
        'Subjects Maths\n'
        'Hobbies Reading\n'
        'Picture file.txt\n'
        'Address Street Pirogovskaya 11-12\n'
        'State and City NCR Gurgaon'
    ))
    browser.element('[id="closeLargeModal"]').click()  # закрываем окно