from pages.registration_page import RegistrationPage


def test_filling_form():
    registration_page = RegistrationPage()

    registration_page.open()

    registration_page.have_title('DEMOQA')

    registration_page.fill_first_name('Demo')
    registration_page.fill_last_name('QA')
    registration_page.fill_email('demoqa@demo.qa')
    registration_page.fill_gender('Male')
    registration_page.fill_phone_number('1234567890')
    registration_page.fill_birthday('24', 'December', '1988')
    registration_page.fill_subjects('Computer Science')
    registration_page.fill_hobbies('Music')
    registration_page.upload_file('image.png')
    registration_page.fill_current_address('Asia/Kolkata')
    registration_page.fill_state_and_city('NCR', 'Delhi')

    registration_page.submit_form()

    registration_page.should_have_registered(
        ('Student Name', 'Demo QA'),
        ('Student Email', 'demoqa@demo.qa'),
        ('Gender', 'Male'),
        ('Mobile', '1234567890'),
        ('Date of Birth', '24 December,1988'),
        ('Subjects', 'Computer Science'),
        ('Hobbies', 'Music'),
        ('Picture', 'image.png'),
        ('Address', 'Asia/Kolkata'),
        ('State and City', 'NCR Delhi')
    )
    registration_page.close_submit_form()
