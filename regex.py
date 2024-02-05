import re

# text = "John Doe"
# pattern = r"(\w+) (\w+)"
# match = re.search(pattern, text)

# if match:
#     prenom = match.group(1)
#     nom = match.group(2)
#     print("Nom:", nom)
#     print("Prénom:", prenom)
# else:
#     print("Aucune correspondance trouvée.")



# email = "JohnDoe@gmail.com"
# pattern = r"@(\S+)"
# match = re.search(pattern, email)

# if match:
#     domaine = match.group(1)
#     print("Domaine:", domaine)
# else:
#     print("Aucune correspondance trouvée.")


import re

email_template = "Bonjour, <nom> de <ville>!"
variables = {
    "<nom>": "Alice",
    "<ville>": "Paris"
}
result = email_template
for balise, valeur in variables.items():
    result = re.sub(re.escape(balise), valeur, result)

print(result)

