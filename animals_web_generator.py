from modules.load_data import load_data

animals = load_data('animals_data.json')

def load_and_rewrite_html(path_input:str, path_output: str) -> None:
    with open(path_input,'r') as file_in:
        html = file_in.read()
    html = html.replace('__REPLACE_ANIMALS_INFO__',generate_unsorted_list())
    with open(path_output,'w') as file_out:
        file_out.write(html)
        
def generate_unsorted_list():
    html_string = ''
    for animal in animals:
        type_failsave = animal["characteristics"].get('type',None)
        nam, die, loc = animal['name'], animal['characteristics']['diet'], animal['locations'][0], 
        typ_ext = "\n<strong>Type: </strong>\n" + type_failsave + '<br>' if type_failsave is not None else ""
        html_string += f'<li class="cards__item"><div class="card__title">{nam}</div>\n<p class="card__text">\n<strong>Diet: </strong>{die}<br>\n<strong>Location: </strong>{loc}<br>{typ_ext}\n</p>\n</li>\n'
    return html_string

if __name__ == '__main__':
    
    load_and_rewrite_html('animals_template.html','animals.html')
    
    for animal in animals:

        name = animal["name"]
        diet = animal["characteristics"].get('diet',None)
        location = animal["locations"][0]
        ttype = animal["characteristics"].get('type',None)
        print(f'{name}\n{diet}\n{location}{"\n" + ttype if ttype is not None else ""}\n')