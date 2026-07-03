import asyncio
from playwright.async_api import async_playwright

async def run_bot():
    async with async_playwright() as p:
        # تشغيل المتصفح بوضع التخفي
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36')
        page = await context.new_page()
        
        # رابط الفيديو (ضعي رابط الفيديو الخاص بك هنا)
        video_url = 'https://youtube.com/shorts/lzz5lecuNeU'
        
        print("🚀 جاري الدخول للفيديو...")
        await page.goto(video_url)
        
        # محاكاة السلوك البشري: الانتظار للمشاهدة
        await asyncio.sleep(45) 
        
        # محاولة الاشتراك
        try:
            # النقر على زر الاشتراك
            await page.click('button[aria-label="Subscribe"]')
            print("✅ تم الاشتراك بنجاح!")
        except:
            print("⚠️ زر الاشتراك غير موجود أو تم الاشتراك مسبقاً.")
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_bot())
