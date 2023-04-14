import aiohttp
import random


emoji = ["☣️", "🗡️", "⚔️", "🛡️", "🔫", "💥", "⭐", "⚡", "🔥", "🤺", "🏹", "💀", "☠️", "🏴‍☠️"]
headers = {
  'authority': 'plarium.com',
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9,ml;q=0.8',
  'app_id': '0',
  'content-length': '0',
  'content-type': 'application/json',
  'cookie': 'flp=https%3a%2f%2fplarium.com%2fen%2fresource%2fgenerator%2fnickname-generator%2f; gu={"q":"","lp":"https%3a%2f%2fplarium.com%2fen%2fresource%2fgenerator%2fnickname-generator%2f","rt":"Portal","r":"https%3a%2f%2fwww.google.com%2f","t":1681464769,"i":0}; href=; pp_uq=5007fe1c-a104-4287-be42-c160839ae3a2; l_ref=https%3a%2f%2fwww.google.com%2f; or_id=oid9552125628.1681463869; _gcl_au=1.1.1305378602.1681463872; _gid=GA1.2.1195131978.1681463873; ln_or=eyI1MjU3NDgxIjoiZCJ9; optiMonkSession=1681463874; optiMonkClientId=3e13cf2a-3c33-d83b-91b7-36c6b67d7485; optiMonkEmbedded185011=N4IgFghgzgMglgWzgFwEoFMIGMzoCYgBcAZhADZToC+QA===; datadome=4hFDV9VpqI9Ars7faTGYKEtVggzrorEKakdITvCm_GwZTSutVMupbT-ySB-jMtOdgJr~MxqUYIfFcjfiyUNrGlmJ9QRMM8E7vg5urXl9mL03OeveV2q3aD2JqgvGKGfN; _ga_5FNDF9DMY8=GS1.1.1681463872.1.1.1681463926.6.0.0; _ga=GA1.1.oid9552125628.1681463869; _uetsid=3c596bc0daa511ed904f47681073a271; _uetvid=3c5999b0daa511ed932ec361be4c008d',
  'dnt': '1',
  'game_id': '0',
  'language_id': '1',
  'origin': 'https://plarium.com',
  'referer': 'https://plarium.com/en/resource/generator/nickname-generator/',
  'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'sitemap_id': '1',
  'theme_id': '1',
  'time-zone': '-3',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}


async def Generator(type, gender):
    url = f"https://plarium.com/services/api/nicknames/new/create?group={type}&gender={gender}"
    # Setting the payload with prompts
    payload = {}

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=payload) as resp:
            response = await resp.json()
            results = f"\n".join([f"{random.choice(emoji)} <code>{name}</code>" for name in response])
            result = f"Click👆 on the names to copy\n\n{results}\n\nClick <i>🔄 Regenerate</i> for new names"
    return result
