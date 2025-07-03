import json

def main(context):
    print(f"Context: {context.__dict__}")
    print(f"Request Method: {context.req.method}")
    print(f"Request Body: {context.req.body}")
    if context.req.method == "POST":
        return context.res.json({
            "message": "درخواست POST بدون بدنه با موفقیت دریافت شد!",
            "status": "success"
        })
    else:
        return context.res.json({
            "message": "فقط درخواست‌های POST پشتیبانی می‌شوند!",
            "status": "error"
        }, status=405)