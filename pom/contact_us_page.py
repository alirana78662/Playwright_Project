class ContactUs:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://symonstorozhenko.wixsite.com/website-1/contact")

    def submit_form(self, name, address, email, number, subject, message):
        # self.page.fill("placeholder=\"Enter your name\"]", name)
        # self.page.fill("placeholder=\"Enter your address\"]", address)
        # self.page.fill("placeholder=\"Enter your email\"]", email)
        # self.page.fill("placeholder=\"Enter your phone number\"]", number)
        # self.page.fill("placeholder=\"Type the subject\"]", subject)
        # self.page.fill("textarea", msg)
        # # self.page.fill("//button[@class='kuTaGy wixui-button zKbzSQ']","Enter")
        self.page.locator("//input[@name= 'name']").fill(name)
        self.page.locator("//input[@name= 'address']").fill(address)
        self.page.locator("//input[@name= 'email']").fill(email)
        self.page.locator("//input[@name= 'phone']").fill(number)
        self.page.locator("//input[@name= 'subject']").fill(subject)
        self.page.locator("//textarea[@id= 'textarea_comp-kqx72xe2']").fill(message)
