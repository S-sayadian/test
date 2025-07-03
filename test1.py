import json

def main(req, res):
    if req.method == "POST":
        return res.json({
            "message": "درخواست POST بدون بدنه با موفقیت دریافت شد!",
            "status": "success"
        })
    else:
        return res.json({
            "message": "فقط درخواست‌های POST پشتیبانی می‌شوند!",
            "status": "error"
        }, status=405)