import os
from selene import browser, have, command
from tests.conftest import FILE_DIR


class RegistrationPage:

    def __init__(self):
        self.firstName = browser.element('#firstName')
        self.lastName = browser.element('#lastName')
        self.userEmail = browser.element('#userEmail')
        self.phoneNumber = browser.element('#userNumber')
        self.currentAddress = browser.element('#currentAddress')
        self.result_table = browser.all('.modal-content td')

    @staticmethod
    def open():
        browser.open('/automation-practice-form')

    @staticmethod
    def have_title(title):
        browser.should(have.title(title))

    def fill_first_name(self, first_name):
        self.firstName.type(first_name)

    def fill_last_name(self, last_name):
        self.lastName.type(last_name)

    def fill_email(self, email):
        self.userEmail.type(email)

    @staticmethod
    def fill_gender(gender):
        browser.all('[name=gender]').element_by(have.value(f'{gender}')).element('..').click()

    def fill_phone_number(self, number):
        self.phoneNumber.type(f'{number}')

    @staticmethod
    def fill_birthday(day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()

    @staticmethod
    def fill_subjects(subjects):
        browser.element('#subjectsInput').type('Co')
        browser.element(f'//*[.="{subjects}"]').click()

    @staticmethod
    def fill_hobbies(hobbies):
        browser.element(f'//label[contains(text(), "{hobbies}")]').click()

    @staticmethod
    def upload_file(file_name):
        browser.element('#uploadPicture').send_keys(os.path.join(FILE_DIR, 'image.png'))

    def fill_current_address(self, address):
        self.currentAddress.type(f'{address}')

    @staticmethod
    def fill_state_and_city(state, city):
        browser.element('#stateCity-wrapper') \
            .perform(command.js.scroll_into_view)
        browser.element('#state').click()
        browser.element(f'//*[.="{state}"]').click()
        browser.element('#city').click()
        browser.element(f'//*[.="{city}"]').click()
        browser.element('#state').click()

    @staticmethod
    def submit_form():
        browser.element('#submit').click().press_enter()

    def should_have_registered(self, *args):
        self.result_table.should(have.exact_texts(*args))

    @staticmethod
    def close_submit_form():
        browser.element('#closeLargeModal') \
            .perform(command.js.scroll_into_view).click()
        browser.element('#example-modal-sizes-title-lg') \
            .should(have.no.text('Thanks for submitting the form'))