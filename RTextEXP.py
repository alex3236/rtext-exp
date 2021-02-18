from mcdreforged.api.rtext import *
from re import search


PLUGIN_METADATA = {
    'id': 'rtext_exp',
    'version': '0.0.1',
    'name': 'RText Exp',
    'description': 'RText表达式实现，支持鼠标悬停、分段设置',
    'author': 'Alex3236',
    'link': 'https://github.com/eagle3236'
}


def rtext_formmat(text: str, new=True):
    if '||' not in text:
        return text
    if '//' in text:
        rtext_list = []
        for i in text.split('//'):
            rtext_list.append(rtext_formmat(i, new=False))
        rtext_list.append('\n')
        return RTextList(*rtext_list)
    text = text.split('||')
    rtext_express = text[1]
    style = search(r"%s=['\"](.*?)['\"]", rtext_express)
    color = search(r"%c=['\"](.*?)['\"]", rtext_express)
    hover = search(r"%h=['\"](.*?)['\"]", rtext_express)
    text = RText(text[0])
    if style is not None:
        for i in style.group(1).split(' '):
            if i in RStyle.__members__:
                text.set_styles(eval(f'RStyle.{i}'))
    if color is not None:
        color = color.group(1)
        if color in RColor.__members__:
            text.set_color(eval(f'RColor.{color}'))
    if hover is not None:
        text.set_hover_text(hover.group(1))
    return RTextList(text, '\n') if new else text