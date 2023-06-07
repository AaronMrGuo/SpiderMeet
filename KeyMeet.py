
def KeyMeet(title):
    """
    检查标题是否符合规则。

    根据指定的规则，检查标题中是否包含特定的关键词，并根据匹配结果返回相应的值。

    Args:
        title (str): 待检查的标题字符串。

    Returns:
        str or None: 根据匹配结果返回不同的值。如果标题中包含任何一个 'not_meeting_key' 中的关键词，
        返回 None；如果标题中包含任何一个 'meeting_key' 中的关键词，返回标题本身；否则返回 None。

    """
    not_meeting_key = ['征文通知', '征文', '讲座通知', '邀请函', '支持函', '招商函', '圆满落幕']
    meeting_key = ['研讨会', '培训班', '会议', '大会', '论坛', '交流会', '峰会', '年会', '沙龙']

    for keyword in not_meeting_key:
        if keyword in title:
            return None

    for keyword in meeting_key:
        if keyword in title:
            title = title.strip()
            return title

    return None


"""
规则：
    title包含的关键词：not_meeeting_key = ['征文通知', '征文', '讲座通知', '邀请函', '支持函', '招商函']   返回None
    title包含的关键词：meeting_key = ['研讨会', '培训班', '会议', '大会', '论坛', '交流会', '峰会', '年会'] 返回title
例：
    title='生声不息-肿瘤系统淋巴瘤研讨会 支持函' 返回 None
    title='生声不息-肿瘤系统淋巴瘤研讨会'       返回 None
"""


