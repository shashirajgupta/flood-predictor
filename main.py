from flask import Flask, render_template, request, jsonify
from predict_flood import predict_flood
from get_weather_data import get_weather, get_weather1
from chatbot_agent import ask_gemini_bot
from alerting_agent import send_alert_email
from field_support_agent import report_status

app = Flask(__name__)

ALERT_EMAIL = "tearfultunes7@gmail.com"  # <-- Set your target email
ALERT_SUBJECT = "🚨 Emergency Alert"
ALERT_KEYWORDS = ["flood warning", "evacuation", "danger", "emergency", "high risk","report"]

def check_for_emergency(text):
    """Check if the input contains critical keywords."""
    return any(keyword in text.lower() for keyword in ALERT_KEYWORDS)

def handle_report_command(user_input):
    """
    Parse and handle 'report' command like:
    report village3 road is blocked and people stranded
    """
    try:
        parts = user_input.split()
        location = parts[1]
        message = " ".join(parts[2:])
        reply = report_status(location, message)
        return reply
    except Exception:
        return "⚠️ Invalid format. Use: report [location] [message]"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    weather = None

    # Manual form input
    if request.method == "POST":
        city = request.form.get("city")
        weather_data = get_weather1(city)


        if weather_data["success"]:
            result = predict_flood(
                weather_data["rainfall"],
                weather_data["temperature"],
                weather_data["humidity"],
                weather_data["water_level"]
            )
            weather = weather_data
        else:
            result = f"❌ Error: {weather_data['error']}"
    
    # Live weather input
    if request.method == "GET" and request.args.get("live"):
        weather = get_weather()
        print(f"[INFO] 📍 Detected Location: {weather['city']}")
        result = predict_flood(weather["rainfall"], weather["temperature"], weather["humidity"], weather["water_level"])

    return render_template("index.html", result=result, weather=weather)
@app.route("/chatbot", methods=["POST"])
def chatbot():
    user_msg = request.json.get("message", "").strip()

    if not user_msg:
        return jsonify({"reply": "⚠️ Please enter a message."})

    # Field update
    if user_msg.lower().startswith("report "):
        reply = handle_report_command(user_msg)
        return jsonify({"reply": reply})

    # Emergency alert detection
    if check_for_emergency(user_msg):
        ai_response = ask_gemini_bot(user_msg)
        send_alert_email(ALERT_SUBJECT, ai_response, ALERT_EMAIL)
        return jsonify({"reply": f"{ai_response} 📧 Emergency alert sent."})

    # Default: General chat
    reply = ask_gemini_bot(user_msg)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
