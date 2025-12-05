import pytest
from playwright.async_api import Page, expect
from pytest import StepReport

@pytest.mark.qase(ids=341)
@pytest.mark.asyncio
async def test_browser_back_after_logout(page: Page):
    """STPCT-341: Browser back button after logout"""
    
    # Step 1: Open homepage
    await page.goto("https://cloudfydemo.cloudfyuat.com/", timeout=30000)
    await page.screenshot(path="step1_homepage.png")
    
    # Step 2: Click Account
    await page.click("text=Account", timeout=10000)
    await page.screenshot(path="step2_account_menu.png")
    
    # Step 3: Fill username
    await page.fill("input[name='USERNAME']", "user.16062@cloudfy.com")
    
    # Step 4: Fill password
    await page.fill("input[name='PASSWORD']", "Testing123!")
    await page.screenshot(path="step4_credentials_filled.png")
    
    # Step 5: Click Login
    await page.click("text=Login", timeout=10000)
    await page.wait_for_load_state("networkidle", timeout=30000)
    
    # Step 6: Verify My Account page
    await expect(page.locator("h2:has-text('My Account')")).to_be_visible(timeout=10000)
    await page.screenshot(path="step6_my_account.png")
    
    # Step 7: Click Account for logout
    await page.click("text=Account", timeout=10000)
    
    # Step 8: Click Log out
    await page.click("text=Log out", timeout=10000)
    await page.wait_for_load_state("networkidle", timeout=30000)
    await page.screenshot(path="step8_logged_out.png")
    
    # Step 9: Press browser back button
    await page.go_back()
    await page.wait_for_load_state("networkidle", timeout=30000)
    
    # Step 10: Verify redirect to Login
    await expect(page.locator("h2:has-text('Login')")).to_be_visible(timeout=10000)
    await page.screenshot(path="step10_login_page.png")
