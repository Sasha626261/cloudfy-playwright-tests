import pytest
from playwright.async_api import Page, expect
from conftest import add_step

@pytest.mark.qase(ids=341)
@pytest.mark.asyncio
async def test_browser_back_after_logout(page: Page):
    """STPCT-341: Browser back button after logout"""
    
    try:
        add_step("Open CloudFX homepage")
        await page.goto("https://cloudfydemo.cloudfyuat.com/", timeout=30000)
        
        add_step("Click Account button")
        await page.click("text=Account", timeout=10000)
        
        add_step("Fill username: user.16062@cloudfy.com")
        await page.fill("input[name='USERNAME']", "user.16062@cloudfy.com")
        
        add_step("Fill password")
        await page.fill("input[name='PASSWORD']", "Testing123!")
        
        add_step("Click Login button")
        await page.click("text=Login", timeout=10000)
        await page.wait_for_load_state("networkidle", timeout=30000)
        
        add_step("Verify My Account page is displayed")
        await expect(page.locator("h2:has-text('My Account')")).to_be_visible(timeout=10000)
        
        add_step("Click Account button to open menu")
        await page.click("text=Account", timeout=10000)
        
        add_step("Click Log out button")
        await page.click("text=Log out", timeout=10000)
        await page.wait_for_load_state("networkidle", timeout=30000)
        
        add_step("Press browser back button")
        await page.go_back()
        await page.wait_for_load_state("networkidle", timeout=30000)
        
        add_step("Verify user is redirected to Login page")
        await expect(page.locator("h2:has-text('Login')")).to_be_visible(timeout=10000)
        
        add_step("TEST COMPLETED SUCCESSFULLY", "passed")
        
    except Exception as e:
        add_step(f"TEST FAILED: {str(e)}", "failed")
        raise
