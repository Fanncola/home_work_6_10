from pages.registration_page import RegistrationPage, User


def test_filling_form():
    demo_user = User(first_name='Demo',
                     last_name='QA',
                     email='demoqa@demo.qa',
                     gender='Male',
                     phone='1234567890',
                     hobbies='Music',
                     current_address='Asia/Kolkata',
                     birth_date={'day': '24', 'month': 'December', 'year': '1988'}
                     )

    registration_page = RegistrationPage()

    registration_page.open()
    registration_page.register(demo_user)
    registration_page.should_have_registered(demo_user)
    registration_page.close_submit_form()
