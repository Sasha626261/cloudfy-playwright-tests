import pytest
from playwright.async_api import Page, expect

@pytest.mark.qase(ids=341)
@pytest.mark.asyncio
async def test_browser_back_after_logout(page: Page):
    """STPCT-341: Browser back button after logout"""
    
    # Open page
    await page.goto("https://cloudfydemo.cloudfyuat.com/")
    
    # Check no errors
    await expect(page.locator("text=Error")).not_to_be_visible()
    await expect(page.locator("text=404")).not_to_be_visible()
    await expect(page.locator("text=500")).not_to_be_visible()
    
    # Login
    await page.click("text=Account")
    await page.fill("input[name='USERNAME']", "user.16062@cloudfy.com")
    await page.fill("input[name='PASSWORD']", "Testing123!")
    await page.click("text=Login")
    
    # Verify My Account page
    await expect(page.locator("h2:has-text('My Account')")).to_be_visible()
    
    # Logout
    await page.click("text=Account")
    await page.click("text=Log out")
    
    # Browser back button - KEY STEP
    await page.go_back()
    
    # Verify redirect to login
    await expect(page.locator("h2:has-text('Login')")).to_be_visible()
