import unittest
import json

# ==========================================
# חלק 1: לוגיקה של ניתוח נתוני אבטחה
# ==========================================

def load_raw_data():
    return [
        {"country": "Israel", "threat_level": "High", "type": "Cyber"},
        {"country": "USA", "threat_level": "Medium", "type": "Infrastructure"},
        {"country": "Japan", "threat_level": "Low", "type": "Cyber"},
        {"country": "Germany", "threat_level": "Medium", "type": "Phishing"}
    ]

def process_security_data(data):
    high_threats = [item for item in data if item['threat_level'] == 'High']
    return {
        "total_events": len(data),
        "high_priority_count": len(high_threats),
        "status": "Analysis Complete"
    }

def generate_html_report(summary, raw_data):
    """מייצר קובץ HTML מעוצב עם תוצאות הניתוח"""
    
    # יצירת שורות הטבלה מהנתונים
    table_rows = ""
    for item in raw_data:
        color = "red" if item['threat_level'] == "High" else "orange" if item['threat_level'] == "Medium" else "green"
        table_rows += f"""
        <tr>
            <td>{item['country']}</td>
            <td style="color: {color}; font-weight: bold;">{item['threat_level']}</td>
            <td>{item['type']}</td>
        </tr>
        """

    html_template = f"""
    <!DOCTYPE html>
    <html lang="he" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <title>דוח אבטחה גלובלי</title>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f0f2f5; margin: 40px; text-align: center; }}
            .container {{ background: white; padding: 20px; border-radius: 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); max-width: 800px; margin: auto; }}
            h1 {{ color: #1a73e8; }}
            .summary-box {{ display: flex; justify-content: space-around; margin-bottom: 30px; }}
            .stat {{ background: #e8f0fe; padding: 15px; border-radius: 10px; min-width: 150px; }}
            .stat span {{ display: block; font-size: 24px; font-weight: bold; color: #1a73e8; }}
            table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
            th, td {{ border: 1px solid #ddd; padding: 12px; text-align: center; }}
            th {{ background-color: #1a73e8; color: white; }}
            tr:nth-child(even) {{ background-color: #f9f9f9; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>דוח ניתוח אבטחה גלובלי</h1>
            <div class="summary-box">
                <div class="stat">אירועים סה"כ <span>{summary['total_events']}</span></div>
                <div class="stat">איומים גבוהים <span>{summary['high_priority_count']}</span></div>
            </div>
            <table>
                <thead>
                    <tr>
                        <th>מדינה</th>
                        <th>רמת איום</th>
                        <th>סוג איום</th>
                    </tr>
                </thead>
                <tbody>
                    {table_rows}
                </tbody>
            </table>
            <p style="margin-top: 20px; color: #666;">סטטוס: {summary['status']}</p>
        </div>
    </body>
    </html>
    """
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_template)
    print("HTML Report generated successfully as 'index.html'")

# ==========================================
# חלק 2: טסטים והרצה
# ==========================================

class TestGlobalSecurity(unittest.TestCase):
    def test_logic(self):
        data = load_raw_data()
        self.assertTrue(len(data) > 0)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGlobalSecurity)
    result = unittest.TextTestRunner().run(suite)
    
    if result.wasSuccessful():
        raw_data = load_raw_data()
        summary = process_security_data(raw_data)
        generate_html_report(summary, raw_data)
    else:
        exit(1)
