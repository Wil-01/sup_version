

import os
import openai
import eel

eel.init('web')
# openai.api_key = "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"


@eel.expose
def verify_api_key(key):
    openai.api_key = key
    try:
        response = openai.Completion.create(
                model="text-davinci-003",
                prompt='Bonjour' ,
                temperature=0,
                max_tokens=120,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0,
                stop=["###"]
            )
        if response['choices'][0]['finish_reason'] == "stop":
            print("La clé API est valide et fonctionnelle.")
            return True
        else:
            print("La clé API est invalide.")
            return False
    except Exception as e:
        print("Une erreur s'est produite lors de la vérification de la clé API :", str(key))
        return False



def get_open(prompt):
    max_tokens = 400
    try: 
        while True:
            print('je commence')
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                temperature=0,
                max_tokens=max_tokens,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0,
                stop=["###"]
            )

            if response['choices'][0]['finish_reason'] == "stop":
                return response['choices'][0]['text']
            else:
                max_tokens *= 2
    except:
        return '500'


@eel.expose
def create_module(module_name='test', description="module de test odoo" ):
    # Demander le nom du module à l'utilisateur
    # module_name = input("Veuillez entrer le nom du module Odoo 15 : ")
    # description = input("Veuillez entrer la description du module Odoo 15 : ")

    # Générer le contenu du model.py à partir de la description
    model_prompt = f"""### Quel est le contenu du fichier models.py pour la création d'un module Odoo 15 de {description} ? Utilise au moins trois models Odoo\n###
    envoie juste le contenu exemple du fichier complet sans phrase explicative ni phrase introductive \n ###
    """
    model_content = get_open(model_prompt)
    if model_content == '500':
        return False
    print('model_content')

    # Générer le contenu du view.xml à partir du model.py
    view_prompt = f"""### en te basant sur le code d'un module Odoo 15 suivant :\n###\n{model_content}\n###\n Quel est le contenu du fichier view.xml  ? je veux une view liste, et un formulaire pour chaque models ainsi que des elements de menu\n###
    envoie juste le contenu exemple du fichier complet sans phrase explicative ni phrase introductive \n ###
    """
    view_content = get_open(view_prompt)
    if view_content == '500':
        return False
    print('view_content')
    # if view_content == '500':
    #     print("Une erreur s'est produite lors de la génération du contenu de view.xml.")
    #     return

    # Générer le contenu du ir.model.access.csv à partir du model.py et du view.xml
    access_prompt = f"""### en te basant sur le code d'un module Odoo 15 suivant :\n###\n{model_content}\n###\n Quel est le contenu du fichier ir.model.access.csv  ?\n###
    envoie juste le contenu exemple du fichier complet sans phrase explicative ni phrase introductive \n ###
    """
    access_content = get_open(access_prompt)
    if access_content == '500':
        return False
    print(access_content)
    access_content = access_content.replace(' ','')
    print(access_content)
    print('access_content')
    # Générer le contenu du manifest à partir du model.py et du __manifest__.py
    manifest_prompt = f"""### en te basant sur le code d'un module Odoo 15 suivant :\n###\n{model_content} et sachant que j'ai un fichier views/view.xml et  security/ir.model.access.csv \n###\n Quel est le contenu du fichier __manifest__.py ?\n###
    envoie juste le contenu exemple du fichier complet sans phrase explicative ni phrase introductive \n ###
    """
    manifest_content = get_open(manifest_prompt)
    if manifest_content == '500':
        return False
    print('manifest_content')

    # if access_content == '500':
    #     print("Une erreur s'est produite lors de la génération du contenu de ir.model.access.csv.")
    #     return

    # Créer le dossier du module
    module_path = os.path.join(os.getcwd(), module_name)
    os.makedirs(module_path)

    # Créer les fichiers et dossiers requis dans le module
    init_file = os.path.join(module_path, '__init__.py')
    manifest_file = os.path.join(module_path, '__manifest__.py')
    models_dir = os.path.join(module_path, 'models')
    models_init_file = os.path.join(models_dir, '__init__.py')
    model_file = os.path.join(models_dir, 'model.py')
    security_dir = os.path.join(module_path, 'security')
    security_access_file = os.path.join(security_dir, 'ir.model.access.csv')
    views_dir = os.path.join(module_path, 'views')
    view_file = os.path.join(views_dir, 'view.xml')

    # Créer les dossiers
    os.makedirs(models_dir)
    os.makedirs(security_dir)
    os.makedirs(views_dir)

    # Créer les fichiers
    # open(init_file, 'a').close()

#     manifest = {
#     'name': f"{module_name}",

#     'summary': f"""{description}""",

#     'description': f"""{description}""",

#     'author': "My Company",
#     'website': "https://www.yourcompany.com",

#     # Categories can be used to filter modules in modules listing
#     # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
#     # for the full list
#     'category': 'Uncategorized',
#     'version': '0.1',

#     # any module necessary for this one to work correctly
#     'depends': ['base'],

#     # always loaded
#     'data': [
#         'security/ir.model.access.csv',
#         'views/views.xml',
#     ],
   
# }



    with open (init_file, 'w')  as file:
        file.write("\nfrom . import models")

    with open (models_init_file, 'w')  as file:
        file.write("\nfrom . import model")
    
    with open (manifest_file, 'w')  as file:
        file.write(manifest_content)

    with open(model_file, 'w') as file:
        file.write(model_content)
    with open(view_file, 'w') as file:
        file.write(view_content)
    with open(security_access_file, 'w') as file:
        file.write(access_content)

    print("Le module Odoo 15 a été créé avec succès.")

    return  True

# Appeler la fonction pour créer le module
# create_module()

eel.start('index.html', mode='default')