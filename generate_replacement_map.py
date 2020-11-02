import json

replacement_map = {}

with open('OneDark.json') as f:
    one_dark = json.load(f)

colors = one_dark['colors']
for k, v in colors.items():
    replacement_map[v] = v

token_colors = one_dark['tokenColors']
for token_color in token_colors:
    settings = token_color['settings']
    if 'foreground' in settings:
        replacement_map[settings['foreground']] = settings['foreground']
    if 'background' in settings:
        replacement_map[settings['background']] = settings['background']   


with open('replacement_map.json', 'w') as f:
    json.dump(replacement_map, f, indent=4)