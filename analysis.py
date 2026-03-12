import os
import time
import json
import webbrowser
import feedparser
from datetime import datetime, timezone

# ==========================================
# PART 1: ADVANCED REAL-TIME RSS SCRAPING
# ==========================================

def scrape_security_news():
    """
    סורק נתוני RSS ממספר מקורות כדי להבטיח זרימת מידע שוטפת מהשעה האחרונה
    """
    print(">>> [SYSTEM] INITIATING GLOBAL SATELLITE UPLINK...")
    
    # שימוש ב-BBC World News - מתעדכן בתדירות גבוהה מאוד
    rss_urls = [
        "http://feeds.bbci.co.uk/news/world/rss.xml",
        "https://www.reutersagency.com/feed/?best-topics=political-general&post_type=best"
    ]
    
    security_events = []
    keywords = ['security', 'attack', 'military', 'cyber', 'war', 'threat', 'intelligence', 'conflict', 'missile', 'drone', 'strike', 'forces', 'police', 'bomb']
    
    for url in rss_urls:
        try:
            print(f">>> [UPLINK] CONNECTING TO NODE: {url[:30]}...")
            feed = feedparser.parse(url)
            
            for entry in feed.entries:
                title = entry.title
                summary = entry.summary if 'summary' in entry else ""
                combined_text = (title + " " + summary).lower()
                link = entry.link if 'link' in entry else "#"
                
                # חישוב זמן - כמה דקות עברו מאז הפרסום
                if 'published_parsed' in entry and entry.published_parsed:
                    pub_dt = datetime.fromtimestamp(time.mktime(entry.published_parsed), timezone.utc)
                    now_dt = datetime.now(timezone.utc)
                    diff_minutes = int((now_dt - pub_dt).total_seconds() / 60)
                else:
                    diff_minutes = 0

                # נסנן רק דברים מה-24 שעות האחרונות, אבל נדגיש את מה שקרה בשעה האחרונה
                if diff_minutes > 1440: # יותר מ-24 שעות
                    continue

                # בדיקת איומים
                is_threat = any(key in combined_text for key in keywords)
                threat_level = "LOW"
                if is_threat:
                    threat_level = "HIGH" if any(x in combined_text for x in ['attack', 'war', 'killed', 'explosion', 'strike', 'missile']) else "MEDIUM"
                
                # יצירת אובייקט האירוע
                security_events.append({
                    "id": f"EVT-{abs(hash(title)) % 1000000:06d}",
                    "title": title,
                    "description": summary[:150] + "..." if len(summary) > 150 else summary,
                    "threat_level": threat_level,
                    "minutes_ago": diff_minutes,
                    "time_label": "JUST NOW" if diff_minutes < 10 else f"{diff_minutes} MINS AGO",
                    "link": link
                })

        except Exception as e:
            print(f">>> [ERROR] NODE FAILURE: {e}")

    # מיון מהחדש לישן
    security_events = sorted(security_events, key=lambda x: x['minutes_ago'])
    
    if not security_events:
        return load_fallback_data()
        
    print(f">>> [SUCCESS] {len(security_events)} TRANSMISSIONS DECODED.")
    return security_events[:30] # ניקח את ה-30 הכי חדשים כדי לא להעמיס

def load_fallback_data():
    return [{
        "id": "SYS-000000", "title": "SYSTEM STANDBY - NO LIVE FEEDS DETECTED", 
        "description": "Satellite uplink disrupted. Waiting for telemetry...",
        "threat_level": "LOW", "minutes_ago": 0, "time_label": "0 MINS AGO", "link": "#"
    }]

# ==========================================
# PART 2: PROCESSING & INSANE UI GENERATION
# ==========================================

def process_security_data(data):
    high_threats = [item for item in data if item['threat_level'] == 'HIGH']
    recent_threats = [item for item in data if item['minutes_ago'] <= 60] # מהשעה האחרונה
    
    if len(high_threats) > 3:
        alert_level = "DEFCON 1 - CRITICAL"
        color = "#ff003c"
    elif len(high_threats) > 0:
        alert_level = "DEFCON 2 - ELEVATED"
        color = "#ff6600"
    else:
        alert_level = "DEFCON 4 - SECURE"
        color = "#00ff66"

    return {
        "total_nodes": len(data),
        "alert_level": alert_level,
        "main_color": color,
        "critical_incidents": len(high_threats),
        "last_hour_count": len(recent_threats),
        "system_status": "ONLINE // SATELLITE SYNC OK"
    }

def generate_nasa_report(summary, raw_data):
    # אנו מעבירים את הנתונים כ-JSON לתוך ה-HTML כדי ש-JavaScript יוכל לייצר אנימציות דינמיות
    events_json = json.dumps(raw_data)
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>OSN GLOBAL COMMAND</title>
        <link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;500;600;700&family=Share+Tech+Mono&display=swap" rel="stylesheet">
        <style>
            :root {{
                --bg: #050a0f;
                --panel-bg: rgba(10, 16, 26, 0.8);
                --cyan: #00f3ff;
                --red: #ff003c;
                --green: #00ff66;
                --yellow: #ffd700;
                --alert: {summary['main_color']};
            }}
            
            * {{ box-sizing: border-box; margin: 0; padding: 0; }}
            
            body {{
                background-color: var(--bg);
                color: #fff;
                font-family: 'Rajdhani', sans-serif;
                overflow-x: hidden;
                background-image: 
                    linear-gradient(rgba(0, 243, 255, 0.03) 1px, transparent 1px),
                    linear-gradient(90deg, rgba(0, 243, 255, 0.03) 1px, transparent 1px);
                background-size: 30px 30px;
            }}

            /* אפקט מסך ישן / סריקה */
            .scanlines {{
                position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
                background: linear-gradient(to bottom, rgba(255,255,255,0), rgba(255,255,255,0) 50%, rgba(0,0,0,0.1) 50%, rgba(0,0,0,0.1));
                background-size: 100% 4px; pointer-events: none; z-index: 999;
            }}

            header {{
                display: flex; justify-content: space-between; align-items: center;
                padding: 20px 40px; border-bottom: 2px solid var(--alert);
                background: linear-gradient(90deg, rgba(255,0,60,0.1) 0%, transparent 100%);
                box-shadow: 0 0 20px rgba(255,0,60,0.2);
            }}

            .logo-area h1 {{
                font-family: 'Share Tech Mono', monospace; font-size: 2.5rem; letter-spacing: 4px;
                color: var(--cyan); text-shadow: 0 0 10px var(--cyan); margin-bottom: 5px;
            }}
            
            .live-indicator {{
                display: inline-block; width: 10px; height: 10px; background: var(--red);
                border-radius: 50%; margin-right: 10px; box-shadow: 0 0 10px var(--red);
                animation: blink 1s infinite;
            }}

            .clock {{ font-family: 'Share Tech Mono'; font-size: 1.5rem; color: var(--cyan); }}

            .dashboard {{
                display: grid; grid-template-columns: 300px 1fr; gap: 20px; padding: 20px 40px; height: calc(100vh - 160px);
            }}

            /* פאנל שמאלי - סטטוס מערכת */
            .sidebar {{
                display: flex; flex-direction: column; gap: 20px;
            }}

            .status-card {{
                background: var(--panel-bg); border: 1px solid rgba(0, 243, 255, 0.2);
                border-left: 4px solid var(--alert); padding: 20px; position: relative;
            }}
            .status-card h3 {{ color: rgba(255,255,255,0.5); font-size: 1rem; letter-spacing: 2px; margin-bottom: 10px; }}
            .status-card .value {{ font-family: 'Share Tech Mono'; font-size: 2.5rem; color: var(--alert); text-shadow: 0 0 10px var(--alert); }}
            
            /* תצוגת הרדאר הקטנה */
            .radar-box {{ height: 200px; display: flex; align-items: center; justify-content: center; position: relative; overflow: hidden; border: 1px solid var(--cyan); background: rgba(0, 243, 255, 0.05); }}
            .radar {{ width: 150px; height: 150px; border-radius: 50%; border: 1px solid rgba(0,243,255,0.3); position: relative; }}
            .radar::after {{
                content: ''; position: absolute; top: 50%; left: 50%; width: 50%; height: 50%;
                background: conic-gradient(from 0deg, transparent 70%, rgba(0, 243, 255, 0.8) 100%);
                transform-origin: 0 0; animation: scan 4s linear infinite;
            }}

            /* פאנל ימני - הכתבות חיות */
            .news-feed {{
                display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
                gap: 15px; overflow-y: auto; padding-right: 10px;
            }}
            
            .news-feed::-webkit-scrollbar {{ width: 8px; }}
            .news-feed::-webkit-scrollbar-track {{ background: rgba(0,0,0,0.5); }}
            .news-feed::-webkit-scrollbar-thumb {{ background: var(--cyan); }}

            .news-card {{
                background: var(--panel-bg); border: 1px solid rgba(255,255,255,0.1);
                padding: 15px; display: flex; flex-direction: column; justify-content: space-between;
                transition: all 0.3s ease; position: relative; overflow: hidden;
            }}
            .news-card:hover {{ transform: translateY(-5px); box-shadow: 0 5px 15px rgba(0,0,0,0.5); }}
            .news-card::before {{ content: ''; position: absolute; top: 0; left: 0; width: 4px; height: 100%; }}
            
            .threat-HIGH {{ border-color: rgba(255,0,60,0.4); }}
            .threat-HIGH::before {{ background: var(--red); box-shadow: 0 0 15px var(--red); }}
            .threat-HIGH .card-title {{ color: var(--red); }}
            
            .threat-MEDIUM {{ border-color: rgba(255,215,0,0.4); }}
            .threat-MEDIUM::before {{ background: var(--yellow); }}
            .threat-MEDIUM .card-title {{ color: var(--yellow); }}
            
            .threat-LOW {{ border-color: rgba(0,243,255,0.4); }}
            .threat-LOW::before {{ background: var(--cyan); }}
            
            .card-meta {{ display: flex; justify-content: space-between; font-family: 'Share Tech Mono'; font-size: 0.85rem; color: rgba(255,255,255,0.6); margin-bottom: 10px; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 5px; }}
            .time-badge {{ color: var(--cyan); background: rgba(0, 243, 255, 0.1); padding: 2px 6px; border-radius: 3px; }}
            .card-title {{ font-size: 1.2rem; font-weight: 600; margin-bottom: 10px; line-height: 1.3; }}
            .card-desc {{ font-size: 0.9rem; color: rgba(255,255,255,0.7); line-height: 1.4; }}

            /* טייקר חדשות למטה */
            .ticker-wrap {{
                position: fixed; bottom: 0; width: 100%; height: 40px; background: #000;
                border-top: 2px solid var(--cyan); display: flex; align-items: center; overflow: hidden;
            }}
            .ticker-title {{ background: var(--cyan); color: #000; padding: 0 20px; font-weight: bold; height: 100%; display: flex; align-items: center; z-index: 10; font-family: 'Share Tech Mono'; }}
            .ticker-move {{ display: inline-block; white-space: nowrap; padding-left: 100%; animation: ticker 40s linear infinite; font-family: 'Share Tech Mono'; }}
            .ticker-item {{ margin-right: 50px; color: #fff; }}
            .ticker-item span {{ color: var(--red); margin-right: 10px; }}

            @keyframes blink {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0.3; }} }}
            @keyframes scan {{ 100% {{ transform: rotate(360deg); }} }}
            @keyframes ticker {{ 0% {{ transform: translate3d(0, 0, 0); }} 100% {{ transform: translate3d(-100%, 0, 0); }} }}
        </style>
    </head>
    <body>
        <div class="scanlines"></div>
        
        <header>
            <div class="logo-area">
                <h1>OSN COMMAND CENTER</h1>
                <div style="font-family: 'Share Tech Mono'; color: rgba(255,255,255,0.6);">
                    <span class="live-indicator"></span>LIVE SATELLITE FEED // INTERCEPTING GLOBAL COMMS
                </div>
            </div>
            <div class="clock" id="live-clock">00:00:00 UTC</div>
        </header>

        <div class="dashboard">
            <div class="sidebar">
                <div class="status-card" style="border-left-color: {summary['main_color']};">
                    <h3>THREAT ASSESSMENT</h3>
                    <div class="value" style="color: {summary['main_color']}; text-shadow: 0 0 10px {summary['main_color']}; font-size: 2rem;">
                        {summary['alert_level']}
                    </div>
                </div>
                
                <div class="status-card" style="border-left-color: var(--cyan);">
                    <h3>TOTAL INTERCEPTS (LAST HR)</h3>
                    <div class="value" style="color: var(--cyan);">{summary['last_hour_count']}</div>
                </div>
                
                <div class="status-card" style="border-left-color: var(--red);">
                    <h3>CRITICAL INCIDENTS</h3>
                    <div class="value" style="color: var(--red);">{summary['critical_incidents']}</div>
                </div>

                <div class="radar-box">
                    <div class="radar"></div>
                    <div style="position:absolute; color:var(--cyan); font-family:'Share Tech Mono'; font-size:0.8rem; bottom: 10px;">SCANNING FREQUENCIES...</div>
                </div>
            </div>

            <div class="news-feed" id="news-container">
                <!-- Data will be injected here by JS -->
            </div>
        </div>

        <div class="ticker-wrap">
            <div class="ticker-title">RAW DATA FEED</div>
            <div class="ticker-move" id="ticker-container">
                <!-- Ticker items will be injected here -->
            </div>
        </div>

        <script>
            // Data from Python Backend
            const rawData = {events_json};
            
            // Live Clock
            function updateClock() {{
                const now = new Date();
                document.getElementById('live-clock').innerText = now.toISOString().substring(11, 19) + ' LOCAL';
            }}
            setInterval(updateClock, 1000);
            updateClock();

            // Render News Cards
            const container = document.getElementById('news-container');
            const ticker = document.getElementById('ticker-container');
            
            let tickerHTML = '';

            rawData.forEach((item, index) => {{
                // Build Card
                const card = document.createElement('div');
                card.className = `news-card threat-${{item.threat_level}}`;
                card.style.animationDelay = `${{index * 0.1}}s`;
                
                card.innerHTML = `
                    <div>
                        <div class="card-meta">
                            <span>ID: ${{item.id}}</span>
                            <span class="time-badge">${{item.time_label}}</span>
                        </div>
                        <div class="card-title">${{item.title}}</div>
                        <div class="card-desc">${{item.description}}</div>
                    </div>
                    <div style="margin-top: 15px; text-align: right;">
                        <span style="font-family: 'Share Tech Mono'; font-size: 0.8rem; color: rgba(255,255,255,0.4);">
                            THREAT: <span style="color: var(--${{item.threat_level === 'HIGH' ? 'red' : item.threat_level === 'MEDIUM' ? 'yellow' : 'cyan'}})">[${{item.threat_level}}]</span>
                        </span>
                    </div>
                `;
                container.appendChild(card);

                // Build Ticker Item
                tickerHTML += `<span class="ticker-item"><span>[${{item.time_label}}]</span> ${{item.title}}</span>`;
            }});

            ticker.innerHTML = tickerHTML;
        </script>
    </body>
    </html>
    """
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    return os.path.abspath("index.html")

if __name__ == "__main__":
    raw_data = scrape_security_news()
    summary = process_security_data(raw_data)
    report_path = generate_nasa_report(summary, raw_data)
    
    # פתיחה אוטומטית רק אם אתה מריץ מקומית. ב-GitHub Actions זה פשוט ישמור את הקובץ.
    try:
        webbrowser.open('file://' + report_path)
    except:
        pass
