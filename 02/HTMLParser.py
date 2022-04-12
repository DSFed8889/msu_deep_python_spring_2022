def parse_html(html_str: str, open_tag_callback, data_callback, close_tag_callback):
    i = 0
    while i < len(html_str):
        tag_start = html_str.find('<', i, len(html_str))
        if tag_start == -1:
            if data_callback is not None:
                data_callback(html_str[i:len(html_str)])
            break
        if tag_start != i:
            if data_callback is not None:
                data_callback(html_str[i:tag_start])
        tag_end = html_str.find('>', tag_start, len(html_str))
        if tag_end == -1:
            if data_callback is not None:
                data_callback(html_str[i:len(html_str)])
            break
        if html_str[tag_start+1] == '/':
            if close_tag_callback is not None:
                close_tag_callback(html_str[tag_start + 2:tag_end].split(maxsplit=1))
        else:
            if open_tag_callback is not None:
                open_tag_callback(html_str[tag_start + 1:tag_end].split(maxsplit=1))
        i = tag_end + 1
