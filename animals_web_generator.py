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
        html_string += f"<li class=\"cards__item\">{animal['name']}<br>\n{animal['characteristics']['diet']}<br>\n{animal['locations'][0]}<br>\n{"\n" + type_failsave + '<br>' if type_failsave is not None else ""}\n</li>\n"
    return html_string

if __name__ == '__main__':
    
    load_and_rewrite_html('animals_template.html','animals.html')
    
    for animal in animals:

        name = animal["name"]
        diet = animal["characteristics"].get('diet',None)
        location = animal["locations"][0]
        ttype = animal["characteristics"].get('type',None)
        print(f'{name}\n{diet}\n{location}{"\n" + ttype if ttype is not None else ""}\n')