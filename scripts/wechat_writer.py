#!/usr/bin/env python3
"""公众号 AI 写作脚本 - 极简版"""
import os, requests, json, re

# ========== 配置（只改这4项） ==========
OPENAI_API_KEY = "sk-xxx"
SERPER_API_KEY = "xxx"          # serper.dev，可选
WECHAT_APPID = "wx-xxx"
WECHAT_SECRET = "xxx"
AUTHOR = "你的笔名"

# ========== AI 调用 ==========
def ask(system, user, temp=0.7):
    r = requests.post("https://api.openai.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {OPENAI_API_KEY}", "Content-Type": "application/json"},
        json={"model": "gpt-4o", "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}], "temperature": temp},
        timeout=120).json()
    return r["choices"][0]["message"]["content"]

# ========== 微信 API ==========
def get_token():
    url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={WECHAT_APPID}&secret={WECHAT_SECRET}"
    return requests.get(url, timeout=30).json()["access_token"]

def upload_thumb(token, path="cover.jpg"):
    url = f"https://api.weixin.qq.com/cgi-bin/material/add_material?access_token={token}&type=thumb"
    with open(path, "rb") as f:
        return requests.post(url, files={"media": f}, timeout=30).json()["media_id"]

def push_draft(token, title, html, thumb_id):
    url = f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={token}"
    data = {"articles": [{"title": title, "author": AUTHOR, "content": html, "thumb_media_id": thumb_id, "show_cover_pic": 1, "need_open_comment": 1}]}
    return requests.post(url, data=json.dumps(data, ensure_ascii=False).encode(), timeout=30).json().get("media_id")

# ========== Markdown 转 HTML ==========
def md2html(md):
    h = md
    h = re.sub(r'^### (.+)$', r'<h3 style="font-size:17px;font-weight:bold;margin:18px 0 8px;">\1</h3>', h, flags=re.M)
    h = re.sub(r'^## (.+)$', r'<h2 style="font-size:19px;font-weight:bold;margin:22px 0 10px;color:#1a1a1a;">\1</h2>', h, flags=re.M)
    h = re.sub(r'^# (.+)$', r'<h1 style="font-size:22px;font-weight:bold;margin:25px 0 12px;color:#000;">\1</h1>', h, flags=re.M)
    h = re.sub(r'\*\*(.+?)\*\*', r'<strong style="color:#1a1a1a;">\1</strong>', h)
    paras = []
    for line in h.split('\n'):
        line = line.strip()
        if not line or line.startswith('---'): continue
        if line.startswith('<h') or line.startswith('<strong'):
            paras.append(line)
        else:
            paras.append(f'<p style="font-size:16px;line-height:1.8;color:#333;margin:10px 0;">{line}</p>')
    return '\n'.join(paras)

# ========== 主流程 ==========
def run(topic):
    print(f"🚀 开始写作：{topic}\n")

    # 搜素材
    materials = ""
    if SERPER_API_KEY:
        resp = requests.post("https://google.serper.dev/search",
            headers={"X-API-KEY": SERPER_API_KEY, "Content-Type": "application/json"},
            json={"q": topic, "num": 5}, timeout=30).json()
        materials = "\n".join([f"- {x['title']}: {x.get('snippet','')}" for x in resp.get("organic", [])[:5]])
        print("🔍 素材已搜集")

    # 写标题
    print("🏷️ 生成标题...")
    title = ask("你是爆款标题专家，只输出最终选定的标题，不解释。",
        f"选题：{topic}\n素材：{materials[:500]}\n请写5个高点击率标题，选最好的1个只输出标题本身：", 0.9).strip().replace('"','').replace("'","")
    print(f"标题：{title}\n")

    # 写正文
    print("✍️ 写正文...")
    article = ask("你是资深公众号写手，口语化、短句、有节奏、去AI味、多用案例。",
        f"选题：{topic}\n素材参考：{materials}\n请写1500-2000字公众号文章。要求：开头50字内抓人；每段最多3行；关键句加粗**；有案例数据；结尾给可执行建议；Markdown格式。", 0.8)
    print("✅ 正文完成\n")

    # 转 HTML
    print("📱 排版...")
    html = md2html(article)

    # 推送
    print("📤 推草稿箱...")
    token = get_token()
    thumb = upload_thumb(token)
    draft_id = push_draft(token, title, html, thumb)
    print(f"\n🎉 完成！草稿 ID：{draft_id}")
    print(f"标题：{title}")
    print("👉 公众号后台 → 草稿箱 → 查看发布")

    os.makedirs("articles", exist_ok=True)
    with open(f"articles/{topic[:15]}.md", "w") as f:
        f.write(f"# {title}\n\n{article}")

if __name__ == "__main__":
    run(input("输入选题：").strip())
