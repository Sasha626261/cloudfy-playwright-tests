import pytest
from playwright.async_api import Page, expect

@pytest.mark.qase(ids=341)
@pytest.mark.asyncio
async def test_browser_back_after_logout(page: Page):
    """STPCT-341: Browser back button after logout"""
    
    print("=== Step 1: Open CloudFX homepage ===")
    await page.goto("https://cloudfydemo.cloudfyuat.com/", timeout=30000)
    print(f"Homepage loaded: {page.url}")
    
    print("=== Step 2: Click Account button ===")
    await page.click("text=Account", timeout=10000)
    print("Account menu opened")
    
    print("=== Step 3: Fill username ===")
    await page.fill("input[name='USERNAME']", "user.16062@cloudfy.com")
    print("Username filled")
    
    print("=== Step 4: Fill password ===")
    await page.fill("input[name='PASSWORD']", "Testing123!")
    print("Password filled")
    
    print("=== Step 5: Click Login button ===")
    await page.click("text=Login", timeout=10000)
    await page.wait_for_load_state("networkidle", timeout=30000)
    print("Login successful")
    
    print("=== Step 6: Verify My Account page ===")
    my_account_heading = page.locator("h2:has-text('My Account')")
    await expect(my_account_heading).to_be_visible(timeout=10000)
    print("My Account page verified")
    
    print("=== Step 7: Click Account button ===")
    await page.click("text=Account", timeout=10000)
    print("Account menu opened")
    
    print("=== Step 8: Click Log out ===")
    await page.click("text=Log out", timeout=10000)
    await page.wait_for_load_state("networkidle", timeout=30000)
    print("Logged out successfully")
    
    print("=== Step 9: Press browser back button ===")
    await page.go_back()
    await page.wait_for_load_state("networkidle", timeout=30000)
    print("Browser back button pressed")
    
    print("=== Step 10: Verify redirect to Login page ===")
    login_heading = page.locator("h2:has-text('Login')")
    await expect(login_heading).to_be_visible(timeout=10000)
    print("Verified: User redirected to Login page")
    
    print("=== TEST PASSED ===")
