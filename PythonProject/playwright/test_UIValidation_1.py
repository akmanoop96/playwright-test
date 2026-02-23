from playwright.sync_api import Page, expect


def test_UIValidationDynamicScript(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("username").fill("rahulshettyacademy")
    page.get_by_label("password").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name='terms and conditions').click()
    page.get_by_role("button", name='Sign In').click()

    iphoneProduct = page.locator("app-card").filter(has_text="iphone X")
    iphoneProduct.get_by_role("button").click()
    nokiaProduct = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaProduct.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)


def test_childWindodwHandle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as new_page_info:
        page.locator(".blinkingText").click()
        childPage=new_page_info.value
        text=childPage.locator(".red").text_content()
        print(text)#Please email us at mentor@rahulshettyacademy.com with below template to receive response
        words=text.split("at")#0Please email us 1 mentor@rahulshettyacademy.com with below template to receive response
        email=words[1].strip().split(" ")[0]
        assert email== "mentor@rahulshettyacademy.com"



#Please email us at mentor@rahulshettyacademy.com with below template to receive response