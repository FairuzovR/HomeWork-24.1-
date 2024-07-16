from rest_framework.serializers import ValidationError

required_text = "https://www.youtube.com/"


def validate_urls(urls):
    if not required_text in urls.lower():
        raise ValidationError("Небоходимо ипользовать ссылку на платформу youtube")
