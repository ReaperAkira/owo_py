from win10toast import ToastNotifier

# Khởi tạo trình thông báo
toaster = ToastNotifier()

# Tùy chỉnh thông báo
toaster.show_toast(
    title="OwO Ban check",
    msg="OH SHIT SOLVE CAPTCHA AND RESTART BOT",
    icon_path= 'OwO.ico',
    duration=5,
    threaded=True,
)


