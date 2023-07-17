from selene import browser, have, command
from dataclasses import dataclass

from data.users import User


@dataclass()
class RegistrationPage(User):
    def __init__(self):
        self.firstName = browser.element('#firstName')
        self.lastName = browser.element('#lastName')
        self.userEmail = browser.element('#userEmail')
        self.userGender = browser.all('[name=gender]')
        self.phoneNumber = browser.element('#userNumber')
        self.currentAddress = browser.element('#currentAddress')
        self.state = browser.element('#state')
        self.submitForm = browser.element('#submit')
        self.resultTable = browser.all('.modal-content td')

    @staticmethod
    def open():
        browser.open('/automation-practice-form')

    def register(self, user):
        self.firstName.type(user.first_name)
        self.lastName.type(user.last_name)
        self.userEmail.type(user.email)
        self.userGender.element_by(have.value(f'{user.gender}')).element('..').click()
        self.phoneNumber.type(f'{user.phone}')
        self.fill_birthday(user.birth_date['day'], user.birth_date['month'], user.birth_date['year'])
        browser.element(f'//label[contains(text(), "{user.hobbies}")]').click()
        self.currentAddress.type(f'{user.current_address}')
        browser.element('#stateCity-wrapper') \
            .perform(command.js.scroll_into_view)
        self.state.click()
        self.submitForm.click().press_enter()

    @staticmethod
    def fill_birthday(day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()

    @staticmethod
    def should_have_registered(user):
        browser.all('.modal-content td').should(have.exact_texts(
            ('Student Name', f'{user.first_name} {user.last_name}'),
            ('Student Email', user.email),
            ('Gender', user.gender),
            ('Mobile', user.phone),
            ('Date of Birth', f'{user.birth_date["day"]} {user.birth_date["month"]},{user.birth_date["year"]}'),
            ('Subjects', ''),
            ('Hobbies', user.hobbies),
            ('Picture', ''),
            ('Address', user.current_address),
            ('State and City', '')))

    @staticmethod
    def close_submit_form():
        browser.element('#closeLargeModal') \
            .perform(command.js.scroll_into_view).click()
        browser.element('#example-modal-sizes-title-lg') \
            .should(have.no.text('Thanks for submitting the form'))
