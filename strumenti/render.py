import asyncio
import pathlib
from playwright.async_api import async_playwright

ROOT = pathlib.Path(__file__).resolve().parent


async def _render(jobs):
    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files"])
        page = await browser.new_page(device_scale_factor=1)
        for name, html, w, h in jobs:
            hp = ROOT / "html" / f"{name}.html"
            hp.write_text(html, encoding="utf-8")
            await page.set_viewport_size({"width": w, "height": h})
            await page.goto(hp.as_uri())
            await page.evaluate("document.fonts.ready")
            await page.wait_for_timeout(120)
            await page.screenshot(path=str(ROOT / "png" / f"{name}.png"), clip={"x": 0, "y": 0, "width": w, "height": h})
        await browser.close()


def render(jobs):
    asyncio.run(_render(jobs))
