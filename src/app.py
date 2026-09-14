from flask import Flask, render_template, request
from detection import analyze_image
import os

# ==============================
# PATH SETUP
# ==============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "../uploads")

# ==============================
# FLASK INIT
# ==============================
app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create uploads folder if not exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ==============================
# HOME PAGE
# ==============================
@app.route("/")
def home():
    return render_template("index.html")

# ==============================
# UPLOAD + ANALYSIS
# ==============================
@app.route("/upload", methods=["POST"])
def upload():

    print("📩 Upload request received")

    file = request.files.get("file")

    if file is None or file.filename == "":
        print("❌ No file selected")
        return render_template("index.html")

    # Save file
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    print("📁 File saved:", filepath)

    # Run full analysis (AI + Copy-Move + Splicing)
    try:
        result = analyze_image(filepath)
        print("✅ Analysis completed")
    except Exception as e:
        print("❌ Error during analysis:", e)
        result = {
            "AI Generated": "Error",
            "Risk Score": 0,
            "Copy-Move": "Error",
            "Splicing": "Error",
            "Recommendation": "Processing Failed"
        }

    # Path for displaying image in browser
    image_path = "uploads/" + file.filename

    return render_template(
        "result.html",
        result=result,
        image_path=image_path
    )

# ==============================
# RUN SERVER
# ==============================
if __name__ == "__main__":
    print("🚀 Server running on http://127.0.0.1:8080")
    app.run(debug=True, host="0.0.0.0", port=8080)