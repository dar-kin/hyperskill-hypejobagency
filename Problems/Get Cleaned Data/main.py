def get_cleaned_data(raw_data):
    form = PromoCodeForm(raw_data)
    if form.is_valid():
        return form.cleaned_data
    else:
        return {}
