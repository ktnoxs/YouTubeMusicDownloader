import re


def remove_urls(string):
    """
    주어진 텍스트에서 url 주소를 공백으로 치환합니다.
    :param string: url을 삭제할 텍스트
    :return: url이 공백으로 치환된 텍스트
    """
    # 정규 표현식을 사용하여 http:// 또는 https://로 시작하는 URL을 찾습니다.
    url_pattern = re.compile(r'http[s]?://\S+')
    # URL을 빈 문자열로 대체합니다.
    return url_pattern.sub('', string)


def to_fullwidth(string):
    """
    주어진 텍스트의 모든 문자를 전각 문자로 변환합니다.
    :param string: 변환할 텍스트
    :return: 전각 문자로 변환된 텍스트
    """
    invalid_chars = r'[<>:"/\|?*]'
    result = []
    for char in string:
        if char in invalid_chars:
            result.append(chr(ord(char) + 0xFEE0))
        else:
            result.append(char)
    return ''.join(result)
