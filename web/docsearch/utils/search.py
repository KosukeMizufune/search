import re

from docsearch.models import File


def search_text(pattern):
    target_files = [obj.filename for obj in File.objects.all() if re.search(pattern, obj.text)]
    return target_files
