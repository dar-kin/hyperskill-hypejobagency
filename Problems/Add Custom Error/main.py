def add_custom_errors(promo_code_form):
    code_data = promo_code_form.data.get('code')
    if promo_code_form.is_valid():
        if not code_data.startswith("2020"):
            promo_code_form.add_error("code", "promo code is expired")
        if not code_data.endswith("django"):
            promo_code_form.add_error("code", "checksum is invalid")
