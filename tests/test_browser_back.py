import pytest
from playwright.async_api import Page, expect
from qaseio.pytest import qase

@qase.id(341)
@qase.title("Browser back button after logout")
@pytest.mark.asyncio
async def test_browser_back_after_logout(page: Page):
    """STPCT-341: Browser back button after logout"""
    
    with qase.step("Open CloudFX homepage"):
        await page.goto("https://cloudfydemo.cloudfyuat.com/", timeout=30000)
        qase.attach("Homepage URL", page.url)
    
    with qase.step("Click Account button"):
        await page.click("text=Account", timeout=10000)
    
    with qase.step("Fill username field"):
        await page.fill("input[name='USERNAME']", "user.16062@cloudfy.com")
    
    with qase.step("Fill password field"):
        await page.fill("input[name='PASSWORD']", "Testing123!")
    
    with qase.step("Click Login button"):
        await page.click("text=Login", timeout=10000)
        await page.wait_for_load_state("networkidle", timeout=30000)
    
    with qase.step("Verify My Account page is displayed"):
        await expect(page.locator("h2:has-text('My Account')")).to_be_visible(timeout=10000)
        screenshot = await page.screenshot()
        qase.attach("My Account page", screenshot, "image/png")
    
    with qase.step("Click Account button for logout"):
        await page.click("text=Account", timeout=10000)
    
    with qase.step("Click Log out button"):
        await page.click("text=Log out", timeout=10000)
        await page.wait_for_load_state("networkidle", timeout=30000)
    
    with qase.step("Press browser back button"):
        await page.go_back()
        await page.wait_for_load_state("networkidle", timeout=30000)
    
    with qase.step("Verify user is redirected to Login page"):
        await expect(page.locator("h2:has-text('Login')")).to_be_visible(timeout=10000)
        screenshot = await page.screenshot()
        qase.attach("Login page after back", screenshot, "image/png")
