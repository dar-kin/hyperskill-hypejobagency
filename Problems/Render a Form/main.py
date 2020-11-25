template = """
<form>{% csrf_token %}
  <ul> {{promo_code_form.as_ul}} </ul>
</form>
"""
