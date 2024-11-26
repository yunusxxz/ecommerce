import re

from django import template

register = template.Library()


@register.filter
def to_capitalize(value: str, sep=" "):
    words = value.split(sep)
    return " ".join([word[0].upper() + word[1:] for word in words])


@register.filter
def to_slug(value: str):
    slug = value.lower()
    slug = (slug.replace("ş", "s")
            .replace("ç", "c")
            .replace("ı", "i")
            .replace("ğ", "g")
            .replace("ö", "o")
            .replace("ü", "u"))
    slug = re.sub(r"[^\w\s-]", "", slug).replace(" ", "-")
    slug = re.sub(r"-+", "-", slug)
    return slug.strip("-")